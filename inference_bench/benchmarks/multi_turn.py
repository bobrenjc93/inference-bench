from __future__ import annotations

import concurrent.futures
import random

from . import register
from .base import Benchmark, BenchmarkResult, RequestMetrics, check_answer

TURNS_PER_CONVERSATION = 8
NUM_CONVERSATIONS = 125
MAX_WORKERS = 64


def _generate_turns(n: int, seed: int) -> list[tuple[str, int]]:
    rng = random.Random(seed)
    turns = []
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
        turns.append((f"{a} {op} {b} =", answer))
    return turns


@register("multi_turn")
class MultiTurnBenchmark(Benchmark):
    name = "multi_turn"
    description = "1250 concurrent 8-turn conversations (10k requests) — tests KV cache management under load"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client = self._make_client(api_base)
        result = BenchmarkResult(name=self.name)
        completed = [0]

        def _run_conversation(conv_idx: int) -> list[RequestMetrics]:
            turns = _generate_turns(TURNS_PER_CONVERSATION, seed=conv_idx)
            conv_metrics = []
            messages: list[dict] = [
                {"role": "system", "content": "You are a calculator. Respond with only the numerical answer, nothing else."},
            ]
            for turn, (equation, expected) in enumerate(turns):
                messages.append({"role": "user", "content": equation})
                response_text, metrics = self._stream_request(
                    client, model, messages, temperature=0.0, max_tokens=512
                )
                metrics.correct = check_answer(response_text, expected)
                metrics.metadata["request_idx"] = conv_idx * TURNS_PER_CONVERSATION + turn
                metrics.metadata["conversation_idx"] = conv_idx
                metrics.metadata["turn_idx"] = turn
                conv_metrics.append(metrics)
                messages.append({"role": "assistant", "content": response_text})

            completed[0] += 1
            if self.verbose and completed[0] % 100 == 0:
                print(f"  [{self.name}] Conversations done: {completed[0]}/{NUM_CONVERSATIONS}")
            return conv_metrics

        total_requests = NUM_CONVERSATIONS * TURNS_PER_CONVERSATION
        if self.verbose:
            print(
                f"  [{self.name}] Running {NUM_CONVERSATIONS} conversations × "
                f"{TURNS_PER_CONVERSATION} turns = {total_requests} requests "
                f"with {MAX_WORKERS} workers..."
            )

        all_conv_metrics: list[list[RequestMetrics]] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            futures = [pool.submit(_run_conversation, i) for i in range(NUM_CONVERSATIONS)]
            for f in concurrent.futures.as_completed(futures):
                conv_metrics = f.result()
                all_conv_metrics.append(conv_metrics)
                result.raw_requests.extend(conv_metrics)

        result.summarize()

        first_turns = [cm[0].ttft_ms for cm in all_conv_metrics if cm]
        last_turns = [cm[-1].ttft_ms for cm in all_conv_metrics if cm]
        if first_turns and last_turns:
            avg_first = sum(first_turns) / len(first_turns)
            avg_last = sum(last_turns) / len(last_turns)
            result.metrics["ttft_first_turn_ms"] = avg_first
            result.metrics["ttft_last_turn_ms"] = avg_last
            result.metrics["ttft_growth_ratio"] = avg_last / avg_first if avg_first > 0 else 0
            result.metrics["ttft_first_turn_median_ms"] = _median(first_turns)
            result.metrics["ttft_first_turn_p99_ms"] = _p99(first_turns)
            result.metrics["ttft_last_turn_median_ms"] = _median(last_turns)
            result.metrics["ttft_last_turn_p99_ms"] = _p99(last_turns)

        correct = sum(1 for r in result.raw_requests if r.correct)
        print(f"  [{self.name}] Done: {correct}/{total_requests} correct")
        self._close_client(client)
        return result


def _median(values: list[float]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def _p99(values: list[float]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = int(len(ordered) * 0.99)
    return ordered[min(index, len(ordered) - 1)]
