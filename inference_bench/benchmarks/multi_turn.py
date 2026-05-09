from __future__ import annotations

import openai

from . import register
from .base import Benchmark, BenchmarkResult, check_answer

MATH_TURNS = [
    ("8 + 13 =", 21),
    ("95 - 38 =", 57),
    ("6 * 14 =", 84),
    ("72 / 9 =", 8),
    ("234 + 567 =", 801),
    ("1024 - 512 =", 512),
    ("33 * 11 =", 363),
    ("450 / 15 =", 30),
]


@register("multi_turn")
class MultiTurnBenchmark(Benchmark):
    name = "multi_turn"
    description = "8-turn growing conversation of math equations — tests KV cache management"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = openai.OpenAI(base_url=api_base, api_key="not-needed", timeout=300)
        result = BenchmarkResult(name=self.name)

        messages: list[dict] = [
            {"role": "system", "content": "You are a calculator. Respond with only the numerical answer, nothing else."},
        ]

        for turn, (equation, expected) in enumerate(MATH_TURNS):
            messages.append({"role": "user", "content": equation})
            print(f"  [{self.name}] Turn {turn + 1}/{len(MATH_TURNS)}: {equation}")

            response_text, metrics = self._stream_request(
                client, model, messages, temperature=0.0, max_tokens=512
            )
            metrics.correct = check_answer(response_text, expected)
            result.raw_requests.append(metrics)

            messages.append({"role": "assistant", "content": response_text})
            approx_ctx = sum(len(m["content"].split()) for m in messages)
            status = "PASS" if metrics.correct else f"FAIL (expected {expected}, got: {response_text.strip()[:40]})"
            print(
                f"    TTFT={metrics.ttft_ms:.0f}ms  "
                f"E2E={metrics.e2e_latency_ms:.0f}ms  "
                f"tokens={metrics.output_tokens}  "
                f"~ctx_words={approx_ctx}  "
                f"{status}"
            )

        result.summarize()

        ttfts = [r.ttft_ms for r in result.raw_requests]
        if len(ttfts) >= 2:
            result.metrics["ttft_first_turn_ms"] = ttfts[0]
            result.metrics["ttft_last_turn_ms"] = ttfts[-1]
            result.metrics["ttft_growth_ratio"] = ttfts[-1] / ttfts[0] if ttfts[0] > 0 else 0
        return result
