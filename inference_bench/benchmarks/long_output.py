from __future__ import annotations

import concurrent.futures
import hashlib

import openai

from . import register
from .base import Benchmark, BenchmarkResult

FEW_SHOT_EXAMPLES = [
    ("1 * 12345 =", "12345"),
    ("1 * 987654 =", "987654"),
    ("1 * 11223344556677 =", "11223344556677"),
]

SYSTEM_PROMPT = (
    "You are a calculator. Compute the answer to each math equation. "
    "Respond with only the numerical answer, nothing else.\n\n"
    "Examples:\n\n"
    + "\n\n".join(f"Q: {q}\nA: {a}" for q, a in FEW_SHOT_EXAMPLES)
)

NUM_REQUESTS = 1000
MAX_WORKERS = 64


def _make_big_number(length: int, seed: int = 0) -> str:
    out: list[str] = []
    i = 0
    while len(out) < length:
        h = hashlib.sha256(f"{seed}:{i}".encode()).hexdigest()
        for ch in h:
            if ch.isdigit() and len(out) < length:
                out.append(ch)
        i += 1
    if out[0] == "0":
        out[0] = "1"
    return "".join(out)


def _check_prefix(response: str, expected: str) -> bool:
    digits = "".join(ch for ch in response if ch.isdigit())
    return digits.startswith(expected)


def _generate_test_cases(n: int) -> list[str]:
    cases = []
    for i in range(n):
        length = 25 + (i % 176)
        cases.append(_make_big_number(length, seed=i))
    return cases


@register("long_output")
class LongOutputBenchmark(Benchmark):
    name = "long_output"
    description = "1 × <huge number> × 10k requests (64 concurrent) — tests decode throughput under load"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = self._make_client(api_base)
        result = BenchmarkResult(name=self.name)

        test_cases = _generate_test_cases(NUM_REQUESTS)
        completed = [0]

        def _do_request(idx: int):
            big_num = test_cases[idx]
            equation = f"1 * {big_num} ="
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Q: {equation}\nA:"},
            ]
            response_text, metrics = self._stream_request(
                client, model, messages, temperature=0.0,
                max_tokens=len(big_num) // 3 + 16,
            )
            metrics.correct = _check_prefix(response_text, big_num)
            completed[0] += 1
            if self.verbose and completed[0] % 1000 == 0:
                print(f"  [{self.name}] Progress: {completed[0]}/{NUM_REQUESTS}")
            return metrics

        if self.verbose:
            print(f"  [{self.name}] Sending {NUM_REQUESTS} requests with {MAX_WORKERS} workers...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            futures = [pool.submit(_do_request, i) for i in range(NUM_REQUESTS)]
            for f in concurrent.futures.as_completed(futures):
                result.raw_requests.append(f.result())

        correct = sum(1 for r in result.raw_requests if r.correct)
        print(f"  [{self.name}] Done: {correct}/{NUM_REQUESTS} correct")
        result.summarize()
        return result
