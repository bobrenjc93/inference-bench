# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, Jun 14 2026

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
| torchinferno |     382.5s (6.4m) | `a102128` |
| vllm         |   1385.9s (23.1m) | `c621af1` |
| sglang       | **187.0s (3.1m)** | `ec36dde` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  148.1 |
| TPOT median (ms)          |            - |    - |   71.4 |
| E2E median (ms)           |            - |    - |  218.8 |
| Throughput median (tok/s) |            - |    - |    5.3 |
| Correctness               |            - |    - |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 14/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36451)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36451)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)         self.scope, self.receive, self.send
(APIServer pid=36451)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)     )
(APIServer pid=36451)     ^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36451)     return await self.app(scope, receive, send)
(APIServer pid=36451)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36451)     await super().__call__(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36451)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36451)     raise exc
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36451)     await self.app(scope, receive, _send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36451)     await self.app(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36451)     handler, is_templated = self._get_handler(request)
(APIServer pid=36451)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36451)     route_name = routing.get_route_name(request)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36451)     route_name = _get_route_name(scope, routes)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36451)     route_name = route.path
(APIServer pid=36451)                  ^^^^^^^^^^
(APIServer pid=36451) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  215.4 |
| TPOT median (ms)          |            - |    - |    0.0 |
| E2E median (ms)           |            - |    - |  361.1 |
| Throughput median (tok/s) |            - |    - |    2.8 |
| Correctness               |            - |    - |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 14/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36451)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36451)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)         self.scope, self.receive, self.send
(APIServer pid=36451)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)     )
(APIServer pid=36451)     ^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36451)     return await self.app(scope, receive, send)
(APIServer pid=36451)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36451)     await super().__call__(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36451)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36451)     raise exc
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36451)     await self.app(scope, receive, _send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36451)     await self.app(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36451)     handler, is_templated = self._get_handler(request)
(APIServer pid=36451)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36451)     route_name = routing.get_route_name(request)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36451)     route_name = _get_route_name(scope, routes)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36451)     route_name = route.path
(APIServer pid=36451)                  ^^^^^^^^^^
(APIServer pid=36451) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  171.1 |
| TPOT median (ms)          |            - |    - |   94.5 |
| E2E median (ms)           |            - |    - |  269.7 |
| Throughput median (tok/s) |            - |    - |    5.0 |
| Correctness               |            - |    - |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 14/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36451)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36451)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)         self.scope, self.receive, self.send
(APIServer pid=36451)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)     )
(APIServer pid=36451)     ^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36451)     return await self.app(scope, receive, send)
(APIServer pid=36451)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36451)     await super().__call__(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36451)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36451)     raise exc
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36451)     await self.app(scope, receive, _send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36451)     await self.app(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36451)     handler, is_templated = self._get_handler(request)
(APIServer pid=36451)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36451)     route_name = routing.get_route_name(request)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36451)     route_name = _get_route_name(scope, routes)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36451)     route_name = route.path
(APIServer pid=36451)                  ^^^^^^^^^^
(APIServer pid=36451) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |   81.8 |
| TPOT median (ms)          |            - |    - |   60.1 |
| E2E median (ms)           |            - |    - |  149.9 |
| Throughput median (tok/s) |            - |    - |    9.2 |
| Correctness               |            - |    - |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 14/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36451)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36451)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)         self.scope, self.receive, self.send
(APIServer pid=36451)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)     )
(APIServer pid=36451)     ^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36451)     return await self.app(scope, receive, send)
(APIServer pid=36451)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36451)     await super().__call__(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36451)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36451)     raise exc
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36451)     await self.app(scope, receive, _send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36451)     await self.app(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36451)     handler, is_templated = self._get_handler(request)
(APIServer pid=36451)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36451)     route_name = routing.get_route_name(request)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36451)     route_name = _get_route_name(scope, routes)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36451)     route_name = route.path
(APIServer pid=36451)                  ^^^^^^^^^^
(APIServer pid=36451) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |   68.3 |
| TPOT median (ms)          |            - |    - |   22.5 |
| E2E median (ms)           |            - |    - |  842.8 |
| Throughput median (tok/s) |            - |    - |   42.0 |
| Correctness               |            - |    - |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 14/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-de887b28:1116:1116 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1117:1117 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1114:1114 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1115:1115 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1118:1118 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1113:1113 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1119:1119 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-de887b28:1112:1112 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

> **vllm error:** `[vllm] Server did not become ready within 1800s.
Last health check: HTTP 500: {"error":{"message":"'_IncludedRouter' object has no attribute 'path'","type":"InternalServerError","param":null,"code":500}}
Log tail:
ages/uvicorn/protocols/http/httptools_impl.py", line 421, in run_asgi
(APIServer pid=36451)     result = await app(  # type: ignore[func-returns-value]
(APIServer pid=36451)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)         self.scope, self.receive, self.send
(APIServer pid=36451)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)     )
(APIServer pid=36451)     ^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 62, in __call__
(APIServer pid=36451)     return await self.app(scope, receive, send)
(APIServer pid=36451)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/fastapi/applications.py", line 1162, in __call__
(APIServer pid=36451)     await super().__call__(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/applications.py", line 90, in __call__
(APIServer pid=36451)     await self.middleware_stack(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
(APIServer pid=36451)     raise exc
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
(APIServer pid=36451)     await self.app(scope, receive, _send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 88, in __call__
(APIServer pid=36451)     await self.app(scope, receive, send)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 131, in __call__
(APIServer pid=36451)     handler, is_templated = self._get_handler(request)
(APIServer pid=36451)                             ~~~~~~~~~~~~~~~~~^^^^^^^^^
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/middleware.py", line 240, in _get_handler
(APIServer pid=36451)     route_name = routing.get_route_name(request)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 75, in get_route_name
(APIServer pid=36451)     route_name = _get_route_name(scope, routes)
(APIServer pid=36451)   File "/workspace/submit-de887b28/builds/vllm/venv/lib/python3.13/site-packages/prometheus_fastapi_instrumentator/routing.py", line 55, in _get_route_name
(APIServer pid=36451)     route_name = route.path
(APIServer pid=36451)                  ^^^^^^^^^^
(APIServer pid=36451) AttributeError: '_IncludedRouter' object has no attribute 'path'
`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  137.0 |
| TPOT median (ms)          |            - |    - |   49.7 |
| E2E median (ms)           |            - |    - |  368.5 |
| Throughput median (tok/s) |            - |    - |   12.9 |
| Correctness               |            - |    - |    99% |
