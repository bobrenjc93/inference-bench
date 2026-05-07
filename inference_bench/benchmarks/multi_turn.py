from __future__ import annotations

import openai

from . import register
from .base import Benchmark, BenchmarkResult

CONVERSATION_STARTERS = [
    "Explain what a Turing machine is in simple terms.",
    "How does that relate to modern computers?",
    "What are the practical limits of computation that follow from this?",
    "Can you give a concrete example of an undecidable problem?",
    "How do software engineers deal with these limits in practice?",
    "What about quantum computing — does it change any of these limits?",
    "Summarize our entire conversation in 3 bullet points.",
    "What's one thing most people get wrong about computation?",
]


@register("multi_turn")
class MultiTurnBenchmark(Benchmark):
    name = "multi_turn"
    description = "8-turn growing conversation — tests KV cache management"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = openai.OpenAI(base_url=api_base, api_key="not-needed")
        result = BenchmarkResult(name=self.name)

        messages: list[dict] = [
            {"role": "system", "content": "You are a knowledgeable CS professor. Be concise but thorough."},
        ]

        for turn, user_msg in enumerate(CONVERSATION_STARTERS):
            messages.append({"role": "user", "content": user_msg})
            print(f"  [{self.name}] Turn {turn + 1}/{len(CONVERSATION_STARTERS)}: {user_msg[:60]}")

            response_text, metrics = self._stream_request(
                client, model, messages, temperature=0.0, max_tokens=512
            )
            result.raw_requests.append(metrics)

            messages.append({"role": "assistant", "content": response_text})
            approx_ctx = sum(len(m["content"].split()) for m in messages)
            print(
                f"    TTFT={metrics.ttft_ms:.0f}ms  "
                f"E2E={metrics.e2e_latency_ms:.0f}ms  "
                f"tokens={metrics.output_tokens}  "
                f"~ctx_words={approx_ctx}"
            )

        result.summarize()

        ttfts = [r.ttft_ms for r in result.raw_requests]
        if len(ttfts) >= 2:
            result.metrics["ttft_first_turn_ms"] = ttfts[0]
            result.metrics["ttft_last_turn_ms"] = ttfts[-1]
            result.metrics["ttft_growth_ratio"] = ttfts[-1] / ttfts[0] if ttfts[0] > 0 else 0
        return result
