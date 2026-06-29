from __future__ import annotations

import re

from inference_bench.benchmarks.base import RequestMetrics
from inference_bench.benchmarks.long_output import LongOutputBenchmark


def test_long_output_records_request_shape_metadata(monkeypatch) -> None:
    monkeypatch.setattr("inference_bench.benchmarks.long_output.NUM_REQUESTS", 3)
    monkeypatch.setattr("inference_bench.benchmarks.long_output.MAX_WORKERS", 1)

    benchmark = LongOutputBenchmark()

    def stream_request(client, model, messages, *, temperature, max_tokens):  # noqa: ANN001
        del client, model, temperature
        content = messages[-1]["content"]
        match = re.search(r"Q: 1 \* ([0-9]+) =", content)
        assert match is not None
        digits = match.group(1)
        assert max_tokens == len(digits) // 3 + 16
        return digits, RequestMetrics(ttft_ms=1.0, output_tokens=len(digits))

    monkeypatch.setattr(benchmark, "_make_client", lambda api_base: object())
    monkeypatch.setattr(benchmark, "_close_client", lambda client: None)
    monkeypatch.setattr(benchmark, "_stream_request", stream_request)

    result = benchmark.run("http://example.invalid/v1", "model")

    by_idx = {metrics.metadata["request_idx"]: metrics for metrics in result.raw_requests}
    assert sorted(by_idx) == [0, 1, 2]
    for request_idx, metrics in by_idx.items():
        expected_len = 25 + request_idx
        assert metrics.metadata["digit_len"] == expected_len
        assert metrics.metadata["max_tokens"] == expected_len // 3 + 16
        assert metrics.correct is True
