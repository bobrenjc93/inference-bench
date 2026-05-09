from __future__ import annotations

import openai

from . import register
from .base import Benchmark, BenchmarkResult, check_answer

FEW_SHOT_EXAMPLES = [
    {"question": "15 + 27 =", "answer": 42},
    {"question": "198 - 53 =", "answer": 145},
    {"question": "12 * 14 =", "answer": 168},
    {"question": "225 / 9 =", "answer": 25},
    {"question": "347 + 258 =", "answer": 605},
]

TEST_QUESTIONS = [
    ("23 + 47 =", 70),
    ("156 - 89 =", 67),
    ("12 * 15 =", 180),
    ("144 / 12 =", 12),
    ("500 + 378 =", 878),
    ("1000 - 247 =", 753),
    ("25 * 16 =", 400),
    ("256 / 8 =", 32),
]


@register("few_shot")
class FewShotBenchmark(Benchmark):
    name = "few_shot"
    description = "5-shot math equations — long input, short output, tests prefill speed"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = self._make_client(api_base)
        result = BenchmarkResult(name=self.name)

        example_text = "\n\n".join(
            f"Q: {ex['question']}\nA: {ex['answer']}" for ex in FEW_SHOT_EXAMPLES
        )
        system_prompt = (
            "You are a calculator. Compute the answer to each math equation. "
            "Respond with only the numerical answer, nothing else.\n\n"
            "Examples:\n\n" + example_text
        )

        for i, (question, expected) in enumerate(TEST_QUESTIONS):
            print(f"  [{self.name}] Request {i + 1}/{len(TEST_QUESTIONS)}: {question}")
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Q: {question}\nA:"},
            ]
            response_text, metrics = self._stream_request(
                client, model, messages, temperature=0.0, max_tokens=256
            )
            metrics.correct = check_answer(response_text, expected)
            result.raw_requests.append(metrics)
            status = "PASS" if metrics.correct else f"FAIL (expected {expected}, got: {response_text.strip()[:40]})"
            print(
                f"    TTFT={metrics.ttft_ms:.0f}ms  "
                f"E2E={metrics.e2e_latency_ms:.0f}ms  "
                f"tokens={metrics.output_tokens}  "
                f"tps={metrics.throughput_tps:.1f}  "
                f"{status}"
            )

        result.summarize()
        return result
