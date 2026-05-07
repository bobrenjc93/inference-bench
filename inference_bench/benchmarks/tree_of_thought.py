from __future__ import annotations

import concurrent.futures
import openai

from . import register
from .base import Benchmark, BenchmarkResult, RequestMetrics

PROBLEM = (
    "I need to move a stack of 4 discs from peg A to peg C using peg B as auxiliary, "
    "following the Tower of Hanoi rules (only one disc at a time, never place a larger "
    "disc on a smaller one). What is the sequence of moves?"
)

BRANCHES = 4
DEPTH = 3


@register("tree_of_thought")
class TreeOfThoughtBenchmark(Benchmark):
    name = "tree_of_thought"
    description = "Branching concurrent requests (4-wide x 3-deep) — tests scheduling"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = openai.OpenAI(base_url=api_base, api_key="not-needed")
        result = BenchmarkResult(name=self.name)

        current_candidates = [PROBLEM]

        for depth in range(DEPTH):
            print(
                f"  [{self.name}] Depth {depth + 1}/{DEPTH}: "
                f"expanding {len(current_candidates)} candidate(s) x {BRANCHES} branches"
            )
            all_branches: list[str] = []
            depth_metrics: list[RequestMetrics] = []

            for cand_idx, candidate in enumerate(current_candidates):
                if depth == 0:
                    gen_prompt = (
                        f"Problem: {candidate}\n\n"
                        f"Propose a distinct approach to solving this problem. "
                        f"Think step by step. Approach #{cand_idx + 1}:"
                    )
                else:
                    gen_prompt = (
                        f"Here is a partial solution approach:\n{candidate}\n\n"
                        f"Continue this approach with the next steps. "
                        f"Think carefully about what comes next:"
                    )

                branch_messages = [
                    {"role": "system", "content": "You are a careful problem solver. Show your reasoning step by step."},
                    {"role": "user", "content": gen_prompt},
                ]

                def _generate(msgs, idx):
                    text, metrics = self._stream_request(
                        client, model, msgs, temperature=0.7, max_tokens=300
                    )
                    print(
                        f"    branch {idx + 1}: "
                        f"TTFT={metrics.ttft_ms:.0f}ms  "
                        f"E2E={metrics.e2e_latency_ms:.0f}ms  "
                        f"tps={metrics.throughput_tps:.1f}"
                    )
                    return text, metrics

                with concurrent.futures.ThreadPoolExecutor(max_workers=BRANCHES) as pool:
                    futures = [
                        pool.submit(_generate, branch_messages, b)
                        for b in range(BRANCHES)
                    ]
                    for f in concurrent.futures.as_completed(futures):
                        text, metrics = f.result()
                        all_branches.append(text)
                        depth_metrics.append(metrics)
                        result.raw_requests.append(metrics)

            eval_prompt = (
                "Evaluate these approaches and pick the single best one. "
                "Reply with ONLY the text of the best approach, nothing else.\n\n"
            )
            for i, branch in enumerate(all_branches):
                eval_prompt += f"--- Approach {i + 1} ---\n{branch}\n\n"

            eval_messages = [
                {"role": "system", "content": "You are a judge evaluating problem-solving approaches."},
                {"role": "user", "content": eval_prompt},
            ]

            print(f"  [{self.name}] Depth {depth + 1}: evaluating {len(all_branches)} branches")
            best_text, eval_metrics = self._stream_request(
                client, model, eval_messages, temperature=0.0, max_tokens=400
            )
            result.raw_requests.append(eval_metrics)
            current_candidates = [best_text]

        result.summarize()
        return result
