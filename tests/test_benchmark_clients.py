from __future__ import annotations

import concurrent.futures
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

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


class _StreamingBenchmark(Benchmark):
    name = "streaming-client-test"
    description = "streaming client helper test"

    def run(self, api_base: str, model: str) -> BenchmarkResult:
        raise NotImplementedError


class _ChunkedSSEHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_POST(self) -> None:
        length = int(self.headers.get("content-length", "0"))
        if length:
            self.rfile.read(length)
        self.server.connection_ids.add(id(self.connection))  # type: ignore[attr-defined]
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Transfer-Encoding", "chunked")
        self.send_header("Connection", "keep-alive")
        self.end_headers()
        for payload in (
            b'data: {"choices":[{"delta":{"content":"4"}}]}\n\n',
            b'data: {"choices":[{"delta":{"content":"2"}}]}\n\n',
            b'data: {"choices":[{"delta":{},"finish_reason":"stop"}]}\n\n',
            b"data: [DONE]\n\n",
        ):
            self.wfile.write(f"{len(payload):x}\r\n".encode("ascii") + payload + b"\r\n")
            self.wfile.flush()
        self.wfile.write(b"0\r\n\r\n")
        self.wfile.flush()

    def log_message(self, format: str, *args: object) -> None:
        return


class _ChunkedSSEServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self) -> None:
        super().__init__(("127.0.0.1", 0), _ChunkedSSEHandler)
        self.connection_ids: set[int] = set()


def test_stream_request_drains_chunked_sse_for_keepalive_reuse() -> None:
    server = _ChunkedSSEServer()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    benchmark = _StreamingBenchmark()
    client = benchmark._make_client(f"http://127.0.0.1:{server.server_port}/v1")

    try:
        first_text, first_metrics = benchmark._stream_request(
            client,
            "model",
            [{"role": "user", "content": "one"}],
        )
        second_text, second_metrics = benchmark._stream_request(
            client,
            "model",
            [{"role": "user", "content": "two"}],
        )
    finally:
        benchmark._close_open_clients()
        server.shutdown()
        server.server_close()

    assert first_text == "42"
    assert second_text == "42"
    assert first_metrics.output_tokens == 2
    assert second_metrics.output_tokens == 2
    assert first_metrics.ttft_ms > 0
    assert second_metrics.ttft_ms > 0
    assert len(server.connection_ids) == 1
