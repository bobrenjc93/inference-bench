from __future__ import annotations

import os
import re
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

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
    throughput_tps: float = 0.0
    correct: bool | None = None
    response_text: str | None = None


@dataclass
class BenchmarkResult:
    name: str
    metrics: dict[str, float] = field(default_factory=dict)
    raw_requests: list[RequestMetrics] = field(default_factory=list)

    def summarize(self) -> dict[str, float]:
        if not self.raw_requests:
            return self.metrics
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
        return openai.OpenAI(
            base_url=api_base,
            api_key="not-needed",
            timeout=300.0,
            http_client=http_client,
        )

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
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )

        first_token_seen = False
        for chunk in stream:
            delta = chunk.choices[0].delta if chunk.choices else None
            if delta and delta.content:
                if not first_token_seen:
                    metrics.ttft_ms = (time.perf_counter() - start) * 1000
                    first_token_seen = True
                chunks.append(delta.content)

        end = time.perf_counter()
        metrics.e2e_latency_ms = (end - start) * 1000
        metrics.output_tokens = len(chunks)

        if metrics.output_tokens > 1 and metrics.ttft_ms > 0:
            decode_time_ms = metrics.e2e_latency_ms - metrics.ttft_ms
            metrics.tpot_ms = decode_time_ms / (metrics.output_tokens - 1)

        if metrics.e2e_latency_ms > 0 and metrics.output_tokens > 0:
            metrics.throughput_tps = metrics.output_tokens / (metrics.e2e_latency_ms / 1000)

        full_text = "".join(chunks)
        if self.debug:
            metrics.response_text = full_text

        return full_text, metrics
