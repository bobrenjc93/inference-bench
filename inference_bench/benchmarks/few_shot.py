from __future__ import annotations

import concurrent.futures
import random

from . import register
from .base import Benchmark, BenchmarkResult, check_answer

FEW_SHOT_EXAMPLES = [
    {"question": "15 + 27 =", "answer": 42},
    {"question": "198 - 53 =", "answer": 145},
    {"question": "12 * 14 =", "answer": 168},
    {"question": "225 / 9 =", "answer": 25},
    {"question": "347 + 258 =", "answer": 605},
]

NUM_REQUESTS = 1000
MAX_WORKERS = 64


def _generate_questions(n: int, seed: int = 42) -> list[tuple[str, int]]:
    rng = random.Random(seed)
    questions = []
    for _ in range(n):
        op = rng.choice(["+", "-", "*", "/"])
        if op == "/":
            b = rng.randint(2, 50)
            a = b * rng.randint(2, 50)
            answer = a // b
        elif op == "*":
            a = rng.randint(2, 99)
            b = rng.randint(2, 99)
            answer = a * b
        elif op == "-":
            a = rng.randint(50, 2000)
            b = rng.randint(1, a)
            answer = a - b
        else:
            a = rng.randint(1, 2000)
            b = rng.randint(1, 2000)
            answer = a + b
        questions.append((f"{a} {op} {b} =", answer))
    return questions


@register("few_shot")
class FewShotBenchmark(Benchmark):
    name = "few_shot"
    description = "5-shot math × 10k requests (64 concurrent) — tests prefill speed under load"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client_for_thread = self._make_thread_local_client_factory(api_base)
        result = BenchmarkResult(name=self.name)

        example_text = "\n\n".join(
            f"Q: {ex['question']}\nA: {ex['answer']}" for ex in FEW_SHOT_EXAMPLES
        )
        system_prompt = (
            "You are a calculator. Compute the answer to each math equation. "
            "Respond with only the numerical answer, nothing else.\n\n"
            "Examples:\n\n" + example_text
        )

        questions = _generate_questions(NUM_REQUESTS)

        def _do_request(idx: int):
            client = client_for_thread()
            question, expected = questions[idx]
            if self.verbose and idx % 1000 == 0:
                print(f"  [{self.name}] Progress: {idx}/{NUM_REQUESTS}")
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Q: {question}\nA:"},
            ]
            response_text, metrics = self._stream_request(
                client, model, messages, temperature=0.0, max_tokens=256
            )
            metrics.metadata["request_idx"] = idx
            metrics.correct = check_answer(response_text, expected)
            return metrics

        if self.verbose:
            print(f"  [{self.name}] Sending {NUM_REQUESTS} requests with {MAX_WORKERS} workers...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            futures = [pool.submit(_do_request, i) for i in range(NUM_REQUESTS)]
            for f in concurrent.futures.as_completed(futures):
                result.raw_requests.append(f.result())

        correct = sum(1 for r in result.raw_requests if r.correct)
        print(f"  [{self.name}] Done: {correct}/{NUM_REQUESTS} correct")
        result.summarize(**self._summary_tokenizer_kwargs(model))
        self._close_open_clients()
        return result
