from __future__ import annotations

import argparse
import threading
import time
import uuid
from contextlib import asynccontextmanager
from typing import Any

import aiohttp
import msgspec
import uvicorn
import zmq
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response, StreamingResponse

try:
    from .vllm_disagg_protocol import make_prefill_request
except ImportError:
    from vllm_disagg_protocol import make_prefill_request


class _ServiceRegistry:
    def __init__(self, *, ttl_s: float = 5.0):
        self._ttl_s = ttl_s
        self._prefill: dict[str, tuple[str, float]] = {}
        self._decode: dict[str, tuple[str, float]] = {}
        self._lock = threading.Lock()
        self._request_count = 0

    def register(self, message: bytes) -> tuple[str, str, bool]:
        data = msgspec.msgpack.decode(message)
        if not isinstance(data, dict):
            raise ValueError("registration payload must be an object")
        role = self._as_text(data.get("type"))
        http_address = self._as_text(data.get("http_address"))
        zmq_address = self._as_text(data.get("zmq_address"))
        if role not in {"P", "D"} or not http_address or not zmq_address:
            raise ValueError(f"invalid registration payload: {data!r}")
        with self._lock:
            target = self._prefill if role == "P" else self._decode
            added = http_address not in target
            target[http_address] = (zmq_address, time.monotonic() + self._ttl_s)
            self._remove_expired_locked()
        return role, http_address, added

    def pair(self) -> tuple[tuple[str, str], tuple[str, str]]:
        with self._lock:
            self._remove_expired_locked()
            if not self._prefill or not self._decode:
                raise LookupError("prefill and decode instances have not both registered")
            prefill = list(self._prefill.items())
            decode = list(self._decode.items())
            index = self._request_count
            self._request_count += 1
            prefill_http, (prefill_zmq, _) = prefill[index % len(prefill)]
            decode_http, (decode_zmq, _) = decode[index % len(decode)]
            return (prefill_http, prefill_zmq), (decode_http, decode_zmq)

    def decode_http_address(self) -> str:
        with self._lock:
            self._remove_expired_locked()
            if not self._decode:
                raise LookupError("no decode instance has registered")
            return next(iter(self._decode))

    def counts(self) -> tuple[int, int]:
        with self._lock:
            self._remove_expired_locked()
            return len(self._prefill), len(self._decode)

    def _remove_expired_locked(self) -> None:
        now = time.monotonic()
        for instances in (self._prefill, self._decode):
            expired = [
                address
                for address, (_, expires_at) in instances.items()
                if expires_at <= now
            ]
            for address in expired:
                instances.pop(address, None)

    @staticmethod
    def _as_text(value: Any) -> str:
        if isinstance(value, bytes):
            return value.decode("utf-8")
        return str(value or "")


class _RequestAudit:
    def __init__(self):
        self._lock = threading.Lock()
        self._counts = {
            "request_pairs": 0,
            "prefill_completed": 0,
            "decode_started": 0,
            "decode_completed": 0,
            "decode_aborted": 0,
            "upstream_errors": 0,
        }

    def increment(self, name: str) -> None:
        with self._lock:
            self._counts[name] += 1

    def snapshot(self) -> dict[str, int]:
        with self._lock:
            return dict(self._counts)


def _start_registration_service(
    registry: _ServiceRegistry,
    *,
    host: str,
    port: int,
) -> threading.Thread:
    def listen() -> None:
        context = zmq.Context.instance()
        router = context.socket(zmq.ROUTER)
        router.setsockopt(zmq.LINGER, 0)
        router.bind(f"tcp://{host}:{port}")
        print(f"[vllm-disagg-proxy] Registration service: tcp://{host}:{port}", flush=True)
        while True:
            frames = router.recv_multipart()
            if not frames:
                continue
            try:
                role, address, added = registry.register(frames[-1])
            except Exception as exc:
                print(f"[vllm-disagg-proxy] Invalid registration: {exc}", flush=True)
                continue
            if added:
                role_name = "prefill" if role == "P" else "decode"
                print(
                    f"[vllm-disagg-proxy] Registered {role_name} instance {address}",
                    flush=True,
                )

    thread = threading.Thread(target=listen, name="vllm-disagg-registry", daemon=True)
    thread.start()
    return thread


@asynccontextmanager
async def _lifespan(app: FastAPI):
    timeout = aiohttp.ClientTimeout(total=6 * 60 * 60)
    connector = aiohttp.TCPConnector(limit=0, limit_per_host=0)
    app.state.session = aiohttp.ClientSession(
        timeout=timeout,
        connector=connector,
        auto_decompress=False,
    )
    try:
        yield
    finally:
        await app.state.session.close()


app = FastAPI(lifespan=_lifespan)
_registry: _ServiceRegistry | None = None
_audit = _RequestAudit()


def _active_registry() -> _ServiceRegistry:
    if _registry is None:
        raise RuntimeError("service registry has not been initialized")
    return _registry


def _forward_headers(request: Request, request_id: str) -> dict[str, str]:
    headers = {"X-Request-Id": request_id}
    authorization = request.headers.get("authorization")
    if authorization:
        headers["Authorization"] = authorization
    return headers


def _response_headers(response: aiohttp.ClientResponse) -> dict[str, str]:
    allowed = {"cache-control", "content-encoding", "content-type", "x-request-id"}
    return {
        key: value
        for key, value in response.headers.items()
        if key.lower() in allowed
    }


async def _error_or_none(response: aiohttp.ClientResponse) -> Response | None:
    if 200 <= response.status < 300:
        return None
    body = await response.read()
    headers = _response_headers(response)
    response.release()
    return Response(content=body, status_code=response.status, headers=headers)


@app.get("/health")
async def health() -> Response:
    prefill_count, decode_count = _active_registry().counts()
    status = 200 if prefill_count and decode_count else 503
    return JSONResponse(
        {
            "prefill_instances": prefill_count,
            "decode_instances": decode_count,
            **_audit.snapshot(),
        },
        status_code=status,
    )


@app.get("/v1/models")
async def models(request: Request) -> Response:
    try:
        decode_address = _active_registry().decode_http_address()
    except LookupError as exc:
        return JSONResponse({"error": str(exc)}, status_code=503)
    session: aiohttp.ClientSession = request.app.state.session
    async with session.get(
        f"http://{decode_address}/v1/models",
        headers={
            "Authorization": request.headers.get("authorization", "Bearer EMPTY")
        },
    ) as upstream:
        body = await upstream.read()
        return Response(
            content=body,
            status_code=upstream.status,
            headers=_response_headers(upstream),
        )


@app.post("/v1/completions")
@app.post("/v1/chat/completions")
async def completions(request: Request) -> Response:
    try:
        request_data = await request.json()
    except Exception as exc:
        return JSONResponse({"error": f"invalid JSON request: {exc}"}, status_code=400)
    if not isinstance(request_data, dict):
        return JSONResponse({"error": "request body must be an object"}, status_code=400)
    try:
        (prefill_http, prefill_zmq), (decode_http, decode_zmq) = (
            _active_registry().pair()
        )
    except LookupError as exc:
        return JSONResponse({"error": str(exc)}, status_code=503)
    _audit.increment("request_pairs")

    request_id = (
        f"___prefill_addr_{prefill_zmq}___decode_addr_{decode_zmq}_"
        f"{uuid.uuid4().hex}"
    )
    headers = _forward_headers(request, request_id)
    prefill_request = make_prefill_request(request_data)

    session: aiohttp.ClientSession = request.app.state.session
    async with session.post(
        f"http://{prefill_http}{request.url.path}",
        json=prefill_request,
        headers=headers,
    ) as prefill_response:
        prefill_error = await _error_or_none(prefill_response)
        if prefill_error is not None:
            _audit.increment("upstream_errors")
            return prefill_error
        await prefill_response.read()
    _audit.increment("prefill_completed")

    _audit.increment("decode_started")
    decode_response = await session.post(
        f"http://{decode_http}{request.url.path}",
        json=request_data,
        headers=headers,
    )
    decode_error = await _error_or_none(decode_response)
    if decode_error is not None:
        _audit.increment("upstream_errors")
        return decode_error

    async def stream_decode_response():
        completed = False
        try:
            async for chunk in decode_response.content.iter_any():
                yield chunk
            completed = True
        finally:
            decode_response.release()
            _audit.increment("decode_completed" if completed else "decode_aborted")

    return StreamingResponse(
        stream_decode_response(),
        status_code=decode_response.status,
        headers=_response_headers(decode_response),
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="vLLM P2P NCCL disaggregation proxy")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--registration-host", default="127.0.0.1")
    parser.add_argument("--registration-port", type=int, required=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    global _registry
    _registry = _ServiceRegistry()
    _start_registration_service(
        _registry,
        host=args.registration_host,
        port=args.registration_port,
    )
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
