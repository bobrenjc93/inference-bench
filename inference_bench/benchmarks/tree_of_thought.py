from __future__ import annotations

import concurrent.futures
import random

from . import register
from .base import Benchmark, BenchmarkResult, RequestMetrics, check_answer

BRANCHES = 4
DEPTH = 3
NUM_TREES = 32
MAX_TREE_WORKERS = 16
REQUESTS_PER_TREE = sum(
    max(1, BRANCHES // (depth + 1)) * BRANCHES + 1
    for depth in range(DEPTH)
)

SYSTEM_PROMPT = "You are a calculator. Respond with only the numerical answer, nothing else."


def _generate_equations(n: int, seed: int) -> list[tuple[str, int]]:
    rng = random.Random(seed)
    equations = []
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
        equations.append((f"{a} {op} {b} =", answer))
    return equations


@register("tree_of_thought")
class TreeOfThoughtBenchmark(Benchmark):
    name = "tree_of_thought"
    description = "323 tree searches (4-wide × 3-deep, ~10k requests) — tests bursty scheduling under load"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = self._make_client(api_base)
        result = BenchmarkResult(name=self.name)
        completed = [0]

        def _run_tree(tree_idx: int) -> list[RequestMetrics]:
            equations = _generate_equations(50, seed=tree_idx)
            tree_metrics: list[RequestMetrics] = []
            eq_idx = 0
            tree_request_idx = 0

            for depth in range(DEPTH):
                num_candidates = max(1, BRANCHES // (depth + 1))

                for cand_idx in range(num_candidates):
                    def _generate(local_eq_idx, branch_idx, local_request_idx):
                        eq, expected = equations[local_eq_idx % len(equations)]
                        messages = [
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": eq},
                        ]
                        text, metrics = self._stream_request(
                            client, model, messages, temperature=0.7, max_tokens=300
                        )
                        metrics.correct = check_answer(text, expected)
                        metrics.metadata["request_idx"] = (
                            tree_idx * REQUESTS_PER_TREE + local_request_idx
                        )
                        metrics.metadata["tree_idx"] = tree_idx
                        metrics.metadata["depth_idx"] = depth
                        metrics.metadata["candidate_idx"] = cand_idx
                        metrics.metadata["branch_idx"] = branch_idx
                        metrics.metadata["request_kind"] = "branch"
                        return metrics

                    with concurrent.futures.ThreadPoolExecutor(max_workers=BRANCHES) as pool:
                        futures = [
                            pool.submit(_generate, eq_idx + b, b, tree_request_idx + b)
                            for b in range(BRANCHES)
                        ]
                        for f in concurrent.futures.as_completed(futures):
                            tree_metrics.append(f.result())
                    eq_idx += BRANCHES
                    tree_request_idx += BRANCHES

                eval_eq, eval_expected = equations[eq_idx % len(equations)]
                eval_messages = [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": eval_eq},
                ]
                _, eval_metrics = self._stream_request(
                    client, model, eval_messages, temperature=0.0, max_tokens=400
                )
                eval_metrics.correct = check_answer(_, eval_expected)
                eval_metrics.metadata["request_idx"] = (
                    tree_idx * REQUESTS_PER_TREE + tree_request_idx
                )
                eval_metrics.metadata["tree_idx"] = tree_idx
                eval_metrics.metadata["depth_idx"] = depth
                eval_metrics.metadata["request_kind"] = "eval"
                tree_metrics.append(eval_metrics)
                eq_idx += 1
                tree_request_idx += 1

            completed[0] += 1
            if self.verbose and completed[0] % 50 == 0:
                print(f"  [{self.name}] Trees done: {completed[0]}/{NUM_TREES}")
            return tree_metrics

        if self.verbose:
            print(
                f"  [{self.name}] Running {NUM_TREES} trees "
                f"({BRANCHES}-wide × {DEPTH}-deep) with {MAX_TREE_WORKERS} workers..."
            )

        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_TREE_WORKERS) as pool:
            futures = [pool.submit(_run_tree, i) for i in range(NUM_TREES)]
            for f in concurrent.futures.as_completed(futures):
                result.raw_requests.extend(f.result())

        correct = sum(1 for r in result.raw_requests if r.correct)
        print(
            f"  [{self.name}] Done: {len(result.raw_requests)} total requests, "
            f"{correct} correct"
        )
        result.summarize()
        self._close_client(client)
        return result
