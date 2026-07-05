from __future__ import annotations

import concurrent.futures
import threading

from inference_bench.benchmarks.base import Benchmark, BenchmarkResult


class _FakeClient:
    def __init__(self, ident: int) -> None:
        self.ident = ident
        self.closed = False

    def close(self) -> None:
        self.closed = True


class _ClientBenchmark(Benchmark):
    name = "client-test"
    description = "client helper test"

    def __init__(self) -> None:
        self.created: list[_FakeClient] = []

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        raise NotImplementedError

    def _make_client(self, api_base: str) -> _FakeClient:  # type: ignore[override]
        del api_base
        client = _FakeClient(len(self.created))
        self.created.append(client)
        open_clients = getattr(self, "_open_clients", None)
        if open_clients is None:
            open_clients = []
            self._open_clients = open_clients
        open_clients.append(client)
        return client


def test_thread_local_client_factory_uses_one_client_per_worker_thread() -> None:
    benchmark = _ClientBenchmark()
    client_for_thread = benchmark._make_thread_local_client_factory("http://example.test/v1")
    ready = threading.Barrier(4)

    def use_client_twice() -> tuple[int, int]:
        ready.wait(timeout=5.0)
        first = client_for_thread()
        second = client_for_thread()
        return first.ident, second.ident

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        identities = list(pool.map(lambda _: use_client_twice(), range(4)))

    assert all(first == second for first, second in identities)
    assert len({first for first, _ in identities}) == 4
    assert len(benchmark.created) == 4

    benchmark._close_open_clients()

    assert all(client.closed for client in benchmark.created)
