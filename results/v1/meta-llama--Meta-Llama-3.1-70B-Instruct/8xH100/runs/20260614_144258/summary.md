# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jun 14 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |          0/4 |  0/4 |    0/4 |
| self_consistency |          0/4 |  0/4 |    0/4 |
| multi_turn       |          0/4 |  0/4 |    0/4 |
| tree_of_thought  |          0/4 |  0/4 |    0/4 |
| long_output      |          0/4 |  0/4 |    0/4 |
| **Total**        |         0/20 | 0/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     458.0s (7.6m) | `a102128` |
| vllm         |   1390.8s (23.2m) | `c621af1` |
| sglang       | **191.4s (3.2m)** | `582bd23` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  162.7 |
| TPOT median (ms)          |            - |    - |   78.8 |
| E2E median (ms)           |            - |    - |  239.7 |
| Throughput median (tok/s) |            - |    - |    5.1 |
| Correctness               |            - |    - |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36424)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36424)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)         self.scope, self.receive, self.send
(APIServer pid=36424)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)     )
(APIServer pid=36424)     ^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36424)     return await self.app(scope, receive, send)
(APIServer pid=36424)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36424)     await super().__call__(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36424)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36424)     raise exc
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36424)     await self.app(scope, receive, _send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36424)     await self.app(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36424)     handler, is_templated = self._get_handler(request)
(APIServer pid=36424)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36424)     route_name = routing.get_route_name(request)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36424)     route_name = _get_route_name(scope, routes)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36424)     route_name = route.path
(APIServer pid=36424)                  ^^^^^^^^^^
(APIServer pid=36424) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  210.5 |
| TPOT median (ms)          |            - |    - |    0.0 |
| E2E median (ms)           |            - |    - |  352.9 |
| Throughput median (tok/s) |            - |    - |    2.8 |
| Correctness               |            - |    - |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36424)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36424)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)         self.scope, self.receive, self.send
(APIServer pid=36424)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)     )
(APIServer pid=36424)     ^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36424)     return await self.app(scope, receive, send)
(APIServer pid=36424)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36424)     await super().__call__(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36424)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36424)     raise exc
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36424)     await self.app(scope, receive, _send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36424)     await self.app(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36424)     handler, is_templated = self._get_handler(request)
(APIServer pid=36424)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36424)     route_name = routing.get_route_name(request)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36424)     route_name = _get_route_name(scope, routes)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36424)     route_name = route.path
(APIServer pid=36424)                  ^^^^^^^^^^
(APIServer pid=36424) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  174.7 |
| TPOT median (ms)          |            - |    - |   96.6 |
| E2E median (ms)           |            - |    - |  274.0 |
| Throughput median (tok/s) |            - |    - |    4.8 |
| Correctness               |            - |    - |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36424)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36424)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)         self.scope, self.receive, self.send
(APIServer pid=36424)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)     )
(APIServer pid=36424)     ^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36424)     return await self.app(scope, receive, send)
(APIServer pid=36424)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36424)     await super().__call__(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36424)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36424)     raise exc
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36424)     await self.app(scope, receive, _send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36424)     await self.app(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36424)     handler, is_templated = self._get_handler(request)
(APIServer pid=36424)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36424)     route_name = routing.get_route_name(request)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36424)     route_name = _get_route_name(scope, routes)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36424)     route_name = route.path
(APIServer pid=36424)                  ^^^^^^^^^^
(APIServer pid=36424) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |   86.9 |
| TPOT median (ms)          |            - |    - |   55.4 |
| E2E median (ms)           |            - |    - |  155.6 |
| Throughput median (tok/s) |            - |    - |    9.1 |
| Correctness               |            - |    - |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36424)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36424)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)         self.scope, self.receive, self.send
(APIServer pid=36424)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)     )
(APIServer pid=36424)     ^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36424)     return await self.app(scope, receive, send)
(APIServer pid=36424)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36424)     await super().__call__(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36424)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36424)     raise exc
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36424)     await self.app(scope, receive, _send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36424)     await self.app(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36424)     handler, is_templated = self._get_handler(request)
(APIServer pid=36424)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36424)     route_name = routing.get_route_name(request)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36424)     route_name = _get_route_name(scope, routes)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36424)     route_name = route.path
(APIServer pid=36424)                  ^^^^^^^^^^
(APIServer pid=36424) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |   67.8 |
| TPOT median (ms)          |            - |    - |   22.9 |
| E2E median (ms)           |            - |    - |  851.9 |
| Throughput median (tok/s) |            - |    - |   40.9 |
| Correctness               |            - |    - |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-3f385118:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-3f385118:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36424)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36424)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)         self.scope, self.receive, self.send
(APIServer pid=36424)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)     )
(APIServer pid=36424)     ^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36424)     return await self.app(scope, receive, send)
(APIServer pid=36424)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36424)     await super().__call__(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36424)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36424)     raise exc
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36424)     await self.app(scope, receive, _send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36424)     await self.app(scope, receive, send)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36424)     handler, is_templated = self._get_handler(request)
(APIServer pid=36424)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36424)     route_name = routing.get_route_name(request)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36424)     route_name = _get_route_name(scope, routes)
(APIServer pid=36424)   File "/workspace/submit-3f385118/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36424)     route_name = route.path
(APIServer pid=36424)                  ^^^^^^^^^^
(APIServer pid=36424) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  140.5 |
| TPOT median (ms)          |            - |    - |   50.7 |
| E2E median (ms)           |            - |    - |  374.8 |
| Throughput median (tok/s) |            - |    - |   12.5 |
| Correctness               |            - |    - |    99% |
