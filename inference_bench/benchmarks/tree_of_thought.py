from __future__ import annotations

import concurrent.futures
import openai

from . import register
from .base import Benchmark, BenchmarkResult, RequestMetrics, check_answer

EQUATIONS = [
    ("37 + 84 =", 121),
    ("195 - 67 =", 128),
    ("13 * 11 =", 143),
    ("192 / 6 =", 32),
    ("456 + 123 =", 579),
    ("78 - 29 =", 49),
    ("15 * 18 =", 270),
    ("360 / 12 =", 30),
    ("567 + 234 =", 801),
    ("99 * 3 =", 297),
    ("1024 - 256 =", 768),
    ("17 * 19 =", 323),
    ("288 / 16 =", 18),
    ("845 + 155 =", 1000),
    ("729 / 27 =", 27),
]

BRANCHES = 4
DEPTH = 3

SYSTEM_PROMPT = "You are a calculator. Respond with only the numerical answer, nothing else."


@register("tree_of_thought")
class TreeOfThoughtBenchmark(Benchmark):
    name = "tree_of_thought"
    description = "Branching concurrent math requests (4-wide x 3-deep) — tests scheduling"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = self._make_client(api_base)
        result = BenchmarkResult(name=self.name)

        eq_idx = 0

        for depth in range(DEPTH):
            num_candidates = max(1, BRANCHES // (depth + 1))
            print(
                f"  [{self.name}] Depth {depth + 1}/{DEPTH}: "
                f"expanding {num_candidates} candidate(s) x {BRANCHES} branches"
            )
            depth_metrics: list[RequestMetrics] = []

            for cand_idx in range(num_candidates):
                def _generate(local_eq_idx, branch_idx):
                    eq, expected = EQUATIONS[local_eq_idx % len(EQUATIONS)]
                    messages = [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": eq},
                    ]
                    text, metrics = self._stream_request(
                        client, model, messages, temperature=0.7, max_tokens=300
                    )
                    metrics.correct = check_answer(text, expected)
                    status = "PASS" if metrics.correct else f"FAIL (expected {expected}, got: {text.strip()[:40]})"
                    print(
                        f"    branch {branch_idx + 1}: "
                        f"TTFT={metrics.ttft_ms:.0f}ms  "
                        f"E2E={metrics.e2e_latency_ms:.0f}ms  "
                        f"tps={metrics.throughput_tps:.1f}  "
                        f"{status}"
                    )
                    return text, metrics

                with concurrent.futures.ThreadPoolExecutor(max_workers=BRANCHES) as pool:
                    futures = [
                        pool.submit(_generate, eq_idx + b, b)
                        for b in range(BRANCHES)
                    ]
                    for f in concurrent.futures.as_completed(futures):
                        text, metrics = f.result()
                        depth_metrics.append(metrics)
                        result.raw_requests.append(metrics)
                eq_idx += BRANCHES

            eval_eq, eval_expected = EQUATIONS[eq_idx % len(EQUATIONS)]
            eval_messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": eval_eq},
            ]

            print(f"  [{self.name}] Depth {depth + 1}: evaluating ({eval_eq})")
            eval_text, eval_metrics = self._stream_request(
                client, model, eval_messages, temperature=0.0, max_tokens=400
            )
            eval_metrics.correct = check_answer(eval_text, eval_expected)
            result.raw_requests.append(eval_metrics)
            eq_idx += 1

        result.summarize()
        return result
