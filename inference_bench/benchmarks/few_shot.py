from __future__ import annotations

import openai

from . import register
from .base import Benchmark, BenchmarkResult

FEW_SHOT_EXAMPLES = [
    {
        "question": "What is 127 + 385?",
        "answer": "127 + 385 = 512",
    },
    {
        "question": "A train travels at 60 mph for 2.5 hours. How far does it go?",
        "answer": "Distance = speed × time = 60 × 2.5 = 150 miles",
    },
    {
        "question": "If a shirt costs $25 and is 20% off, what is the sale price?",
        "answer": "Discount = $25 × 0.20 = $5. Sale price = $25 - $5 = $20",
    },
    {
        "question": "What is the area of a circle with radius 7?",
        "answer": "Area = π × r² = π × 49 ≈ 153.94 square units",
    },
    {
        "question": "A bag has 3 red and 5 blue marbles. What is the probability of drawing a red marble?",
        "answer": "P(red) = 3/(3+5) = 3/8 = 0.375",
    },
]

TEST_QUESTIONS = [
    "What is 2^10 - 2^8?",
    "A car uses 8 gallons of gas to travel 240 miles. What is its fuel efficiency in mpg?",
    "If you invest $1000 at 5% simple interest for 3 years, how much interest do you earn?",
    "A rectangle has length 12 and width 8. What is the length of its diagonal?",
    "Three coins are flipped. What is the probability of getting exactly two heads?",
    "A factory produces 450 widgets in 6 hours. How many widgets per minute is that?",
    "What is the sum of the first 20 positive integers?",
    "A pizza is cut into 8 equal slices. If you eat 3 slices, what fraction remains?",
]


@register("few_shot")
class FewShotBenchmark(Benchmark):
    name = "few_shot"
    description = "5-shot math reasoning — long input, short output, tests prefill speed"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = openai.OpenAI(base_url=api_base, api_key="not-needed")
        result = BenchmarkResult(name=self.name)

        example_text = "\n\n".join(
            f"Q: {ex['question']}\nA: {ex['answer']}" for ex in FEW_SHOT_EXAMPLES
        )
        system_prompt = (
            "You are a math tutor. Answer questions step by step, showing your work. "
            "Here are some examples of how to answer:\n\n" + example_text
        )

        for i, question in enumerate(TEST_QUESTIONS):
            print(f"  [{self.name}] Request {i + 1}/{len(TEST_QUESTIONS)}: {question[:60]}")
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Q: {question}\nA:"},
            ]
            _, metrics = self._stream_request(
                client, model, messages, temperature=0.0, max_tokens=256
            )
            result.raw_requests.append(metrics)
            print(
                f"    TTFT={metrics.ttft_ms:.0f}ms  "
                f"E2E={metrics.e2e_latency_ms:.0f}ms  "
                f"tokens={metrics.output_tokens}  "
                f"tps={metrics.throughput_tps:.1f}"
            )

        result.summarize()
        return result
