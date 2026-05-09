from __future__ import annotations

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


TEST_CASES = [
    _make_big_number(25, seed=0),
    _make_big_number(50, seed=1),
    _make_big_number(75, seed=2),
    _make_big_number(100, seed=3),
    _make_big_number(125, seed=4),
    _make_big_number(150, seed=5),
    _make_big_number(175, seed=6),
    _make_big_number(200, seed=7),
]


@register("long_output")
class LongOutputBenchmark(Benchmark):
    name = "long_output"
    description = "1 * <huge number> — forces long token output, tests decode throughput"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = openai.OpenAI(base_url=api_base, api_key="not-needed", timeout=300)
        result = BenchmarkResult(name=self.name)

        for i, big_num in enumerate(TEST_CASES):
            equation = f"1 * {big_num} ="
            print(
                f"  [{self.name}] Request {i + 1}/{len(TEST_CASES)}: "
                f"1 * <{len(big_num)}-digit number> ="
            )
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Q: {equation}\nA:"},
            ]
            response_text, metrics = self._stream_request(
                client, model, messages, temperature=0.0,
                max_tokens=len(big_num) // 3 + 16,
            )
            metrics.correct = _check_prefix(response_text, big_num)
            result.raw_requests.append(metrics)
            status = (
                "PASS" if metrics.correct
                else f"FAIL (got {metrics.output_tokens} tokens: {response_text.strip()[:60]}...)"
            )
            print(
                f"    TTFT={metrics.ttft_ms:.0f}ms  "
                f"E2E={metrics.e2e_latency_ms:.0f}ms  "
                f"tokens={metrics.output_tokens}  "
                f"tps={metrics.throughput_tps:.1f}  "
                f"{status}"
            )

        result.summarize()
        return result
