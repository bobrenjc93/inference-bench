from __future__ import annotations

import json
import os
import re
import threading
import time
from abc import ABC, abstractmethod
from collections.abc import Callable, Iterator
from dataclasses import dataclass, field
from functools import lru_cache
from urllib.parse import urljoin

import httpx
import openai


def check_answer(response: str, expected: int) -> bool:
    return bool(re.search(r'\b' + re.escape(str(expected)) + r'\b', response))


def _env_int(name: str, default: int, *, minimum: int = 1) -> int:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        return max(minimum, int(raw))
    except ValueError:
        return default


@dataclass
class RequestMetrics:
    ttft_ms: float = 0.0
    tpot_ms: float = 0.0
    e2e_latency_ms: float = 0.0
    output_tokens: int = 0
    stream_content_chunks: int = 0
    throughput_tps: float = 0.0
    correct: bool | None = None
    response_text: str | None = None
    metadata: dict[str, int | float | str | bool] = field(default_factory=dict)
    completion_text: str = field(default="", repr=False)


@dataclass
class BenchmarkResult:
    name: str
    metrics: dict[str, float] = field(default_factory=dict)
    raw_requests: list[RequestMetrics] = field(default_factory=list)

    def summarize(
        self,
        *,
        model: str | None = None,
        model_revision: str | None = None,
    ) -> dict[str, float]:
        if not self.raw_requests:
            return self.metrics
        if model:
            tokenizer = _tokenizer_for_model(model, model_revision)
            for request in self.raw_requests:
                request.output_tokens = len(
                    tokenizer.encode(request.completion_text, add_special_tokens=False)
                )
                if request.output_tokens > 1 and request.ttft_ms > 0:
                    decode_time_ms = request.e2e_latency_ms - request.ttft_ms
                    request.tpot_ms = decode_time_ms / (request.output_tokens - 1)
                else:
                    request.tpot_ms = 0.0
                if request.e2e_latency_ms > 0 and request.output_tokens > 0:
                    request.throughput_tps = request.output_tokens / (
                        request.e2e_latency_ms / 1000
                    )
                else:
                    request.throughput_tps = 0.0
        ttfts = [r.ttft_ms for r in self.raw_requests if r.ttft_ms > 0]
        tpots = [r.tpot_ms for r in self.raw_requests if r.tpot_ms > 0]
        e2es = [r.e2e_latency_ms for r in self.raw_requests]
        tps_list = [r.throughput_tps for r in self.raw_requests if r.throughput_tps > 0]
        total_tokens = sum(r.output_tokens for r in self.raw_requests)

        def _median(xs):
            if not xs:
                return 0.0
            s = sorted(xs)
            n = len(s)
            if n % 2 == 1:
                return s[n // 2]
            return (s[n // 2 - 1] + s[n // 2]) / 2

        def _p99(xs):
            if not xs:
                return 0.0
            s = sorted(xs)
            idx = int(len(s) * 0.99)
            return s[min(idx, len(s) - 1)]

        self.metrics = {
            "ttft_median_ms": _median(ttfts),
            "ttft_p99_ms": _p99(ttfts),
            "tpot_median_ms": _median(tpots),
            "tpot_p99_ms": _p99(tpots),
            "e2e_median_ms": _median(e2es),
            "e2e_p99_ms": _p99(e2es),
            "throughput_median_tps": _median(tps_list),
            "total_output_tokens": total_tokens,
            "total_stream_content_chunks": sum(
                request.stream_content_chunks for request in self.raw_requests
            ),
            "num_requests": len(self.raw_requests),
        }

        correct_list = [r.correct for r in self.raw_requests if r.correct is not None]
        if correct_list:
            self.metrics["correctness_rate"] = sum(correct_list) / len(correct_list)

        return self.metrics


class Benchmark(ABC):
    name: str
    description: str
    debug: bool = False
    verbose: bool = False
    authoritative_output_token_count: bool = False
    authoritative_tokenizer_path: str | None = None
    model_revision: str | None = None

    @abstractmethod
    def run(self, api_base: str, model: str) -> BenchmarkResult:
        ...

    def _make_client(self, api_base: str) -> openai.OpenAI:
        max_connections = _env_int("INFERENCE_BENCH_HTTP_MAX_CONNECTIONS", 512, minimum=1)
        max_keepalive = _env_int(
            "INFERENCE_BENCH_HTTP_MAX_KEEPALIVE_CONNECTIONS",
            max_connections,
            minimum=0,
        )
        http_client = httpx.Client(
            timeout=300.0,
            limits=httpx.Limits(
                max_connections=max_connections,
                max_keepalive_connections=min(max_keepalive, max_connections),
            ),
        )
        client = openai.OpenAI(
            base_url=api_base,
            api_key="not-needed",
            timeout=300.0,
            http_client=http_client,
        )
        open_clients = getattr(self, "_open_clients", None)
        if open_clients is None:
            open_clients = []
            self._open_clients = open_clients
        open_clients.append(client)
        return client

    def _summary_tokenizer_kwargs(self, model: str) -> dict[str, str | None]:
        if not self.authoritative_output_token_count:
            return {"model": None, "model_revision": None}
        if self.authoritative_tokenizer_path:
            return {
                "model": self.authoritative_tokenizer_path,
                "model_revision": None,
            }
        return {"model": model, "model_revision": self.model_revision}

    def _make_thread_local_client_factory(self, api_base: str) -> Callable[[], openai.OpenAI]:
        local = threading.local()
        creation_lock = threading.Lock()

        def client_for_thread() -> openai.OpenAI:
            client = getattr(local, "client", None)
            if client is None:
                with creation_lock:
                    client = self._make_client(api_base)
                local.client = client
            return client

        return client_for_thread

    def _close_client(self, client: openai.OpenAI) -> None:
        open_clients = getattr(self, "_open_clients", None)
        if open_clients is not None:
            try:
                open_clients.remove(client)
            except ValueError:
                pass
        close = getattr(client, "close", None)
        if not callable(close):
            return
        try:
            close()
        except Exception:
            if self.debug:
                raise

    def _close_open_clients(self) -> None:
        open_clients = list(getattr(self, "_open_clients", []) or [])
        for client in open_clients:
            self._close_client(client)

    def _stream_request(
        self,
        client: openai.OpenAI,
        model: str,
        messages: list[dict],
        temperature: float = 0.0,
        max_tokens: int = 256,
    ) -> tuple[str, RequestMetrics]:
        """
        Send a streaming chat completion and measure per-token timing.
        Returns (full_response_text, RequestMetrics).
        """
        metrics = RequestMetrics()
        chunks: list[str] = []

        start = time.perf_counter()
        http_client = _openai_http_client(client)
        url = urljoin(str(client.base_url), "chat/completions")
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True,
        }

        first_token_seen = False
        done_seen_s: float | None = None
        with http_client.stream("POST", url, json=payload) as response:
            response.raise_for_status()
            for data in _iter_sse_data(response):
                now = time.perf_counter()
                if data.startswith("[DONE]"):
                    done_seen_s = now
                    continue
                event = json.loads(data)
                if isinstance(event, dict) and event.get("error"):
                    raise RuntimeError(f"stream error: {event['error']}")
                choices = event.get("choices")
                if not isinstance(choices, list) or not choices:
                    continue
                first_choice = choices[0]
                if not isinstance(first_choice, dict):
                    continue
                delta = first_choice.get("delta")
                if not isinstance(delta, dict):
                    continue
                content = delta.get("content")
                if not isinstance(content, str) or not content:
                    continue
                if not first_token_seen:
                    metrics.ttft_ms = (now - start) * 1000
                    first_token_seen = True
                chunks.append(content)

        end = done_seen_s if done_seen_s is not None else time.perf_counter()
        metrics.e2e_latency_ms = (end - start) * 1000
        metrics.output_tokens = len(chunks)
        metrics.stream_content_chunks = len(chunks)

        if metrics.output_tokens > 1 and metrics.ttft_ms > 0:
            decode_time_ms = metrics.e2e_latency_ms - metrics.ttft_ms
            metrics.tpot_ms = decode_time_ms / (metrics.output_tokens - 1)

        if metrics.e2e_latency_ms > 0 and metrics.output_tokens > 0:
            metrics.throughput_tps = metrics.output_tokens / (metrics.e2e_latency_ms / 1000)

        full_text = "".join(chunks)
        metrics.completion_text = full_text
        if self.debug:
            metrics.response_text = full_text

        return full_text, metrics


@lru_cache(maxsize=8)
def _tokenizer_for_model(model: str, revision: str | None):
    from transformers import AutoTokenizer, PreTrainedTokenizerFast

    kwargs = {"revision": revision, "trust_remote_code": True}
    try:
        return AutoTokenizer.from_pretrained(model, **kwargs)
    except (AttributeError, KeyError, ValueError):
        return PreTrainedTokenizerFast.from_pretrained(model, **kwargs)


def _openai_http_client(client: openai.OpenAI) -> httpx.Client:
    http_client = getattr(client, "_client", None)
    if isinstance(http_client, httpx.Client):
        return http_client
    raise TypeError("OpenAI client does not expose a synchronous httpx.Client")


def _iter_sse_data(response: httpx.Response) -> Iterator[str]:
    data_lines: list[str] = []
    for line in response.iter_lines():
        if not line:
            if data_lines:
                yield "\n".join(data_lines)
                data_lines.clear()
            continue
        if line.startswith(":"):
            continue
        name, separator, value = line.partition(":")
        if separator != ":" or name != "data":
            continue
        if value.startswith(" "):
            value = value[1:]
        data_lines.append(value)
    if data_lines:
        yield "\n".join(data_lines)
