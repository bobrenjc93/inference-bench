from __future__ import annotations

import concurrent.futures
import openai

from . import register
from .base import Benchmark, BenchmarkResult, RequestMetrics

REASONING_PROMPT = (
    "Solve this step by step:\n\n"
    "A farmer has 17 sheep. All but 9 die. How many sheep does the farmer have left?\n\n"
    "Think carefully before answering."
)

NUM_SAMPLES = 16
MAX_WORKERS = 16


@register("self_consistency")
class SelfConsistencyBenchmark(Benchmark):
    name = "self_consistency"
    description = "N concurrent identical prompts at temp=0.7 — tests batch throughput and prefix caching"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = openai.OpenAI(base_url=api_base, api_key="not-needed")
        result = BenchmarkResult(name=self.name)

        messages = [
            {"role": "system", "content": "You are a careful reasoning assistant."},
            {"role": "user", "content": REASONING_PROMPT},
        ]

        print(f"  [{self.name}] Sending {NUM_SAMPLES} concurrent requests...")

        def _do_request(idx: int) -> tuple[str, RequestMetrics]:
            text, metrics = self._stream_request(
                client, model, messages, temperature=0.7, max_tokens=256
            )
            print(
                f"    request {idx + 1}/{NUM_SAMPLES} done: "
                f"TTFT={metrics.ttft_ms:.0f}ms  "
                f"E2E={metrics.e2e_latency_ms:.0f}ms  "
                f"tps={metrics.throughput_tps:.1f}"
            )
            return text, metrics

        responses: list[str] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            futures = [pool.submit(_do_request, i) for i in range(NUM_SAMPLES)]
            for f in concurrent.futures.as_completed(futures):
                text, metrics = f.result()
                responses.append(text)
                result.raw_requests.append(metrics)

        unique_answers = len(set(r.strip().split("\n")[-1] for r in responses))
        result.summarize()
        result.metrics["unique_final_answers"] = unique_answers
        print(f"  [{self.name}] {unique_answers} unique final answers across {NUM_SAMPLES} samples")
        return result
