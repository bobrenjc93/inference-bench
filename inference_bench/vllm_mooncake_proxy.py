# SPDX-License-Identifier: Apache-2.0
# Protocol flow adapted from vLLM's Mooncake disaggregated proxy example.
from __future__ import annotations

import argparse
import asyncio
import threading
import uuid
from contextlib import asynccontextmanager
from typing import Any, AsyncIterator

import aiohttp
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, Response, StreamingResponse


class _RequestAudit:
    def __init__(self) -> None:
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

    def snapshot(self, *, ready: bool) -> dict[str, int]:
        with self._lock:
            counts = dict(self._counts)
        counts.update(
            {
                "prefill_instances": int(ready),
                "decode_instances": int(ready),
            }
        )
        return counts


_audit = _RequestAudit()


def _forward_headers(request: Request, request_id: str) -> dict[str, str]:
    headers = {"X-Request-Id": request_id}
    authorization = request.headers.get("authorization")
    if authorization:
        headers["Authorization"] = authorization
    return headers


def _prefill_body(body: dict[str, Any], transfer_id: str) -> dict[str, Any]:
    result = dict(body)
    result["kv_transfer_params"] = {
        "do_remote_decode": True,
        "do_remote_prefill": False,
        "transfer_id": transfer_id,
    }
    result["stream"] = False
    result["max_tokens"] = 1
    if "max_completion_tokens" in result:
        result["max_completion_tokens"] = 1
    result.pop("stream_options", None)
    return result


def _decode_body(
    body: dict[str, Any],
    *,
    transfer_id: str,
    bootstrap_address: str,
    engine_id: str,
) -> dict[str, Any]:
    result = dict(body)
    result["kv_transfer_params"] = {
        "do_remote_decode": False,
        "do_remote_prefill": True,
        "remote_bootstrap_addr": bootstrap_address,
        "remote_engine_id": engine_id,
        "transfer_id": transfer_id,
    }
    return result


def create_app(
    *,
    prefill_url: str,
    decode_url: str,
    bootstrap_port: int,
) -> FastAPI:
    bootstrap_address = f"http://127.0.0.1:{bootstrap_port}"

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        timeout = aiohttp.ClientTimeout(total=None)
        app.state.session = aiohttp.ClientSession(
            timeout=timeout,
            connector=aiohttp.TCPConnector(limit=0),
        )
        app.state.ready = False
        app.state.prefill_engine_id = ""
        try:
            while True:
                try:
                    async with app.state.session.get(
                        f"{prefill_url}/health"
                    ) as prefill_health:
                        prefill_health.raise_for_status()
                    async with app.state.session.get(
                        f"{decode_url}/health"
                    ) as decode_health:
                        decode_health.raise_for_status()
                    async with app.state.session.get(
                        f"{bootstrap_address}/query"
                    ) as query:
                        query.raise_for_status()
                        payload = await query.json()
                    entries = payload.values() if isinstance(payload, dict) else ()
                    engine_id = next(
                        (
                            str(entry.get("engine_id", ""))
                            for entry in entries
                            if isinstance(entry, dict) and entry.get("engine_id")
                        ),
                        "",
                    )
                    if not engine_id:
                        raise RuntimeError("Mooncake bootstrap query omitted engine_id")
                    app.state.prefill_engine_id = engine_id
                    app.state.ready = True
                    break
                except (aiohttp.ClientError, RuntimeError, ValueError):
                    await asyncio.sleep(1)
            yield
        finally:
            await app.state.session.close()

    app = FastAPI(lifespan=lifespan)

    @app.get("/health")
    async def health() -> JSONResponse:
        return JSONResponse(_audit.snapshot(ready=bool(app.state.ready)))

    @app.get("/v1/models")
    async def models(request: Request) -> Response:
        if not app.state.ready:
            raise HTTPException(status_code=503, detail="Service Unavailable")
        async with app.state.session.get(
            f"{decode_url}/v1/models",
            headers=_forward_headers(request, str(uuid.uuid4())),
        ) as upstream:
            payload = await upstream.read()
            return Response(
                payload,
                status_code=upstream.status,
                media_type=upstream.headers.get("content-type"),
            )

    async def post_prefill(
        *,
        endpoint: str,
        body: dict[str, Any],
        headers: dict[str, str],
        transfer_id: str,
    ) -> None:
        try:
            async with app.state.session.post(
                f"{prefill_url}{endpoint}",
                json=_prefill_body(body, transfer_id),
                headers={**headers, "X-data-parallel-rank": "0"},
            ) as response:
                await response.read()
                response.raise_for_status()
            _audit.increment("prefill_completed")
        except BaseException:
            _audit.increment("upstream_errors")
            raise

    async def handle(endpoint: str, request: Request) -> StreamingResponse:
        if not app.state.ready:
            raise HTTPException(status_code=503, detail="Service Unavailable")
        body = await request.json()
        if not isinstance(body, dict):
            raise HTTPException(status_code=400, detail="JSON object required")
        request_id = str(uuid.uuid4())
        transfer_id = f"xfer-{request_id}"
        headers = _forward_headers(request, request_id)
        _audit.increment("request_pairs")
        prefill_task = asyncio.create_task(
            post_prefill(
                endpoint=endpoint,
                body=body,
                headers=headers,
                transfer_id=transfer_id,
            )
        )
        try:
            upstream = await app.state.session.post(
                f"{decode_url}{endpoint}",
                json=_decode_body(
                    body,
                    transfer_id=transfer_id,
                    bootstrap_address=bootstrap_address,
                    engine_id=app.state.prefill_engine_id,
                ),
                headers=headers,
            )
            if upstream.status >= 400:
                detail = (await upstream.text())[:2000]
                upstream.release()
                raise HTTPException(status_code=upstream.status, detail=detail)
            _audit.increment("decode_started")
        except BaseException:
            _audit.increment("upstream_errors")
            if not prefill_task.done():
                prefill_task.cancel()
            await asyncio.gather(prefill_task, return_exceptions=True)
            raise

        async def stream() -> AsyncIterator[bytes]:
            try:
                async for chunk in upstream.content.iter_any():
                    if chunk:
                        yield chunk
                await prefill_task
                _audit.increment("decode_completed")
            except (asyncio.CancelledError, GeneratorExit):
                _audit.increment("decode_aborted")
                raise
            except BaseException:
                _audit.increment("upstream_errors")
                raise
            finally:
                upstream.release()
                if not prefill_task.done():
                    prefill_task.cancel()
                await asyncio.gather(prefill_task, return_exceptions=True)

        return StreamingResponse(
            stream(),
            media_type=upstream.headers.get("content-type", "text/event-stream"),
        )

    @app.post("/v1/completions")
    async def completions(request: Request) -> StreamingResponse:
        return await handle("/v1/completions", request)

    @app.post("/v1/chat/completions")
    async def chat_completions(request: Request) -> StreamingResponse:
        return await handle("/v1/chat/completions", request)

    return app


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--prefill-url", required=True)
    parser.add_argument("--decode-url", required=True)
    parser.add_argument("--bootstrap-port", type=int, required=True)
    args = parser.parse_args()
    app = create_app(
        prefill_url=args.prefill_url,
        decode_url=args.decode_url,
        bootstrap_port=args.bootstrap_port,
    )
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
