from __future__ import annotations

import concurrent.futures

from . import register
from .base import Benchmark, BenchmarkResult, RequestMetrics, check_answer

EQUATION = "17 * 23 ="
EXPECTED_ANSWER = 391

NUM_SAMPLES = 1000
MAX_WORKERS = 128


@register("self_consistency")
class SelfConsistencyBenchmark(Benchmark):
    name = "self_consistency"
    description = "10k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        client_for_thread = self._make_thread_local_client_factory(api_base)
        result = BenchmarkResult(name=self.name)

        messages = [
            {"role": "system", "content": "You are a calculator. Respond with only the numerical answer, nothing else."},
            {"role": "user", "content": EQUATION},
        ]

        if self.verbose:
            print(f"  [{self.name}] Sending {NUM_SAMPLES} concurrent requests with {MAX_WORKERS} workers...")
        completed = [0]

        def _do_request(idx: int) -> tuple[str, RequestMetrics]:
            client = client_for_thread()
            text, metrics = self._stream_request(
                client, model, messages, temperature=0.7, max_tokens=256
            )
            metrics.metadata["request_idx"] = idx
            metrics.correct = check_answer(text, EXPECTED_ANSWER)
            completed[0] += 1
            if self.verbose and completed[0] % 1000 == 0:
                print(f"  [{self.name}] Progress: {completed[0]}/{NUM_SAMPLES}")
            return text, metrics

        responses: list[str] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            futures = [pool.submit(_do_request, i) for i in range(NUM_SAMPLES)]
            for f in concurrent.futures.as_completed(futures):
                text, metrics = f.result()
                responses.append(text)
                result.raw_requests.append(metrics)

        unique_answers = len(set(r.strip().split("\n")[-1] for r in responses))
        result.summarize()
        result.metrics["unique_final_answers"] = unique_answers
        correct_count = sum(1 for r in result.raw_requests if r.correct)
        print(
            f"  [{self.name}] {unique_answers} unique final answers across {NUM_SAMPLES} samples, "
            f"{correct_count}/{NUM_SAMPLES} correct"
        )
        self._close_open_clients()
        return result
