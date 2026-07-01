# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:18 PM PT, Jul 1 2026

## Scorecard

| Benchmark        | torchinferno | vllm |    sglang |
| :--------------- | -----------: | ---: | --------: |
| few_shot         |      **4/4** |  0/4 |       0/4 |
| self_consistency |      **3/4** |  0/4 |       0/4 |
| multi_turn       |          1/4 |  0/4 |   **3/4** |
| tree_of_thought  |          1/4 |  0/4 |   **3/4** |
| long_output      |          0/4 |  0/4 |   **4/4** |
| **Total**        |         9/20 | 0/20 | **10/20** |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **51.2s (0.9m)** | `3af4940` |
| vllm         |    475.9s (7.9m) | `4787f2d` |
| sglang       |    328.8s (5.5m) | `5ae214f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |    **154.1** |    - |  156.4 |
| TPOT median (ms)          |     **49.0** |    - |   73.4 |
| E2E median (ms)           |    **196.5** |    - |  227.9 |
| Throughput median (tok/s) |      **5.9** |    - |    5.2 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7206:8921 [6] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO comm 0x1e76c590 rank 6 nranks 8 cudaDev 6 busId b9000 - Abort COMPLETE
[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-809ee492:7202:7202 [2] NCCL INFO comm 0x33eb8a30 rank 2 nranks 8 cudaDev 2 busId 75000 - Destroy COMPLETE
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nRanks 8 cudaDev 2 busId 75000 - Abort START
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:8927 [2] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nranks 8 cudaDev 2 busId 75000 - Abort COMPLETE
gpu-dev-809ee492:7205:7205 [5] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) ERROR 07-01 21:37:22 [multiproc_executor.py:284] Worker proc VllmWorker-5 died unexpectedly, shutting down executor.
(EngineCore pid=7001) INFO 07-01 21:37:22 [multiproc_executor.py:426] [shutdown] Executor: waiting for worker exit count=8
gpu-dev-809ee492:7203:7203 [3] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7201:7201 [1] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7207:7207 [7] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7200:7200 [0] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7202:7202 [2] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7204:7204 [4] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7206:7206 [6] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) Process EngineCore:
(EngineCore pid=7001) Traceback (most recent call last):
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore pid=7001)     self.run()
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore pid=7001)     self._target(*self._args, **self._kwargs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1235, in run_engine_core
(EngineCore pid=7001)     raise e
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1200, in run_engine_core
(EngineCore pid=7001)     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore pid=7001)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 966, in __init__
(EngineCore pid=7001)     super().__init__(
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 133, in __init__
(EngineCore pid=7001)     kv_cache_config = self._initialize_kv_caches(vllm_config)
(EngineCore pid=7001)                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 321, in _initialize_kv_caches
(EngineCore pid=7001)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/abstract.py", line 124, in initialize_from_config
(EngineCore pid=7001)     compilation_times: list[CompilationTimes] = self.collective_rpc(
(EngineCore pid=7001)                                                 ^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 402, in collective_rpc
(EngineCore pid=7001)     return future if non_block else future.result()
(EngineCore pid=7001)                                     ^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 91, in result
(EngineCore pid=7001)     return super().result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 449, in result
(EngineCore pid=7001)     return self.__get_result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
(EngineCore pid=7001)     raise self._exception
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 95, in _wait_for_response
(EngineCore pid=7001)     response = self.aggregate(self.get_response())
(EngineCore pid=7001)                               ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 391, in get_response
(EngineCore pid=7001)     raise RuntimeError(
(EngineCore pid=7001) RuntimeError: Worker failed with error 'The buffer size in the given workspace is insufficient for the given problem size. Buffer: 1048576 bytes, Required: 4194304 bytes.', please check the stack trace above for the root cause
(APIServer pid=6602) Traceback (most recent call last):
(APIServer pid=6602)   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=6602)   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 732, in <module>
(APIServer pid=6602)     uvloop.run(run_server(args))
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run
(APIServer pid=6602)     return __asyncio.run(
(APIServer pid=6602)            ^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run
(APIServer pid=6602)     return runner.run(main)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
(APIServer pid=6602)     return self._loop.run_until_complete(task)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=6602)     return await main
(APIServer pid=6602)            ^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 692, in run_server
(APIServer pid=6602)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 706, in run_server_worker
(APIServer pid=6602)     async with build_async_engine_client(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 100, in build_async_engine_client
(APIServer pid=6602)     async with build_async_engine_client_from_engine_args(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 136, in build_async_engine_client_from_engine_args
(APIServer pid=6602)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=6602)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 217, in from_vllm_config
(APIServer pid=6602)     return cls(
(APIServer pid=6602)            ^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 146, in __init__
(APIServer pid=6602)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=6602)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 132, in make_async_mp_client
(APIServer pid=6602)     return AsyncMPClient(*client_args)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 963, in __init__
(APIServer pid=6602)     super().__init__(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 573, in __init__
(APIServer pid=6602)     with launch_core_engines(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 144, in __exit__
(APIServer pid=6602)     next(self.gen)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1213, in launch_core_engines
(APIServer pid=6602)     wait_for_engine_startup(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1272, in wait_for_engine_startup
(APIServer pid=6602)     raise RuntimeError(
(APIServer pid=6602) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
/usr/lib/python3.12/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 8 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |    **160.7** |    - |  232.2 |
| TPOT median (ms)          |          0.0 |    - |    0.0 |
| E2E median (ms)           |    **173.8** |    - |  388.4 |
| Throughput median (tok/s) |      **5.8** |    - |    2.6 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7206:8921 [6] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO comm 0x1e76c590 rank 6 nranks 8 cudaDev 6 busId b9000 - Abort COMPLETE
[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-809ee492:7202:7202 [2] NCCL INFO comm 0x33eb8a30 rank 2 nranks 8 cudaDev 2 busId 75000 - Destroy COMPLETE
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nRanks 8 cudaDev 2 busId 75000 - Abort START
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:8927 [2] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nranks 8 cudaDev 2 busId 75000 - Abort COMPLETE
gpu-dev-809ee492:7205:7205 [5] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) ERROR 07-01 21:37:22 [multiproc_executor.py:284] Worker proc VllmWorker-5 died unexpectedly, shutting down executor.
(EngineCore pid=7001) INFO 07-01 21:37:22 [multiproc_executor.py:426] [shutdown] Executor: waiting for worker exit count=8
gpu-dev-809ee492:7203:7203 [3] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7201:7201 [1] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7207:7207 [7] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7200:7200 [0] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7202:7202 [2] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7204:7204 [4] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7206:7206 [6] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) Process EngineCore:
(EngineCore pid=7001) Traceback (most recent call last):
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore pid=7001)     self.run()
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore pid=7001)     self._target(*self._args, **self._kwargs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1235, in run_engine_core
(EngineCore pid=7001)     raise e
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1200, in run_engine_core
(EngineCore pid=7001)     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore pid=7001)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 966, in __init__
(EngineCore pid=7001)     super().__init__(
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 133, in __init__
(EngineCore pid=7001)     kv_cache_config = self._initialize_kv_caches(vllm_config)
(EngineCore pid=7001)                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 321, in _initialize_kv_caches
(EngineCore pid=7001)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/abstract.py", line 124, in initialize_from_config
(EngineCore pid=7001)     compilation_times: list[CompilationTimes] = self.collective_rpc(
(EngineCore pid=7001)                                                 ^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 402, in collective_rpc
(EngineCore pid=7001)     return future if non_block else future.result()
(EngineCore pid=7001)                                     ^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 91, in result
(EngineCore pid=7001)     return super().result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 449, in result
(EngineCore pid=7001)     return self.__get_result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
(EngineCore pid=7001)     raise self._exception
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 95, in _wait_for_response
(EngineCore pid=7001)     response = self.aggregate(self.get_response())
(EngineCore pid=7001)                               ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 391, in get_response
(EngineCore pid=7001)     raise RuntimeError(
(EngineCore pid=7001) RuntimeError: Worker failed with error 'The buffer size in the given workspace is insufficient for the given problem size. Buffer: 1048576 bytes, Required: 4194304 bytes.', please check the stack trace above for the root cause
(APIServer pid=6602) Traceback (most recent call last):
(APIServer pid=6602)   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=6602)   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 732, in <module>
(APIServer pid=6602)     uvloop.run(run_server(args))
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run
(APIServer pid=6602)     return __asyncio.run(
(APIServer pid=6602)            ^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run
(APIServer pid=6602)     return runner.run(main)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
(APIServer pid=6602)     return self._loop.run_until_complete(task)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=6602)     return await main
(APIServer pid=6602)            ^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 692, in run_server
(APIServer pid=6602)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 706, in run_server_worker
(APIServer pid=6602)     async with build_async_engine_client(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 100, in build_async_engine_client
(APIServer pid=6602)     async with build_async_engine_client_from_engine_args(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 136, in build_async_engine_client_from_engine_args
(APIServer pid=6602)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=6602)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 217, in from_vllm_config
(APIServer pid=6602)     return cls(
(APIServer pid=6602)            ^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 146, in __init__
(APIServer pid=6602)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=6602)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 132, in make_async_mp_client
(APIServer pid=6602)     return AsyncMPClient(*client_args)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 963, in __init__
(APIServer pid=6602)     super().__init__(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 573, in __init__
(APIServer pid=6602)     with launch_core_engines(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 144, in __exit__
(APIServer pid=6602)     next(self.gen)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1213, in launch_core_engines
(APIServer pid=6602)     wait_for_engine_startup(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1272, in wait_for_engine_startup
(APIServer pid=6602)     raise RuntimeError(
(APIServer pid=6602) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
/usr/lib/python3.12/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 8 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm |    sglang |
| :------------------------ | -----------: | ---: | --------: |
| TTFT median (ms)          |        296.3 |    - | **170.8** |
| TPOT median (ms)          |     **62.2** |    - |     108.7 |
| E2E median (ms)           |        349.8 |    - | **282.2** |
| Throughput median (tok/s) |          4.2 |    - |   **4.8** |
| Correctness               |          98% |    - |       98% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7206:8921 [6] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO comm 0x1e76c590 rank 6 nranks 8 cudaDev 6 busId b9000 - Abort COMPLETE
[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-809ee492:7202:7202 [2] NCCL INFO comm 0x33eb8a30 rank 2 nranks 8 cudaDev 2 busId 75000 - Destroy COMPLETE
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nRanks 8 cudaDev 2 busId 75000 - Abort START
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:8927 [2] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nranks 8 cudaDev 2 busId 75000 - Abort COMPLETE
gpu-dev-809ee492:7205:7205 [5] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) ERROR 07-01 21:37:22 [multiproc_executor.py:284] Worker proc VllmWorker-5 died unexpectedly, shutting down executor.
(EngineCore pid=7001) INFO 07-01 21:37:22 [multiproc_executor.py:426] [shutdown] Executor: waiting for worker exit count=8
gpu-dev-809ee492:7203:7203 [3] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7201:7201 [1] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7207:7207 [7] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7200:7200 [0] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7202:7202 [2] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7204:7204 [4] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7206:7206 [6] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) Process EngineCore:
(EngineCore pid=7001) Traceback (most recent call last):
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore pid=7001)     self.run()
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore pid=7001)     self._target(*self._args, **self._kwargs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1235, in run_engine_core
(EngineCore pid=7001)     raise e
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1200, in run_engine_core
(EngineCore pid=7001)     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore pid=7001)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 966, in __init__
(EngineCore pid=7001)     super().__init__(
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 133, in __init__
(EngineCore pid=7001)     kv_cache_config = self._initialize_kv_caches(vllm_config)
(EngineCore pid=7001)                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 321, in _initialize_kv_caches
(EngineCore pid=7001)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/abstract.py", line 124, in initialize_from_config
(EngineCore pid=7001)     compilation_times: list[CompilationTimes] = self.collective_rpc(
(EngineCore pid=7001)                                                 ^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 402, in collective_rpc
(EngineCore pid=7001)     return future if non_block else future.result()
(EngineCore pid=7001)                                     ^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 91, in result
(EngineCore pid=7001)     return super().result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 449, in result
(EngineCore pid=7001)     return self.__get_result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
(EngineCore pid=7001)     raise self._exception
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 95, in _wait_for_response
(EngineCore pid=7001)     response = self.aggregate(self.get_response())
(EngineCore pid=7001)                               ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 391, in get_response
(EngineCore pid=7001)     raise RuntimeError(
(EngineCore pid=7001) RuntimeError: Worker failed with error 'The buffer size in the given workspace is insufficient for the given problem size. Buffer: 1048576 bytes, Required: 4194304 bytes.', please check the stack trace above for the root cause
(APIServer pid=6602) Traceback (most recent call last):
(APIServer pid=6602)   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=6602)   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 732, in <module>
(APIServer pid=6602)     uvloop.run(run_server(args))
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run
(APIServer pid=6602)     return __asyncio.run(
(APIServer pid=6602)            ^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run
(APIServer pid=6602)     return runner.run(main)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
(APIServer pid=6602)     return self._loop.run_until_complete(task)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=6602)     return await main
(APIServer pid=6602)            ^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 692, in run_server
(APIServer pid=6602)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 706, in run_server_worker
(APIServer pid=6602)     async with build_async_engine_client(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 100, in build_async_engine_client
(APIServer pid=6602)     async with build_async_engine_client_from_engine_args(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 136, in build_async_engine_client_from_engine_args
(APIServer pid=6602)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=6602)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 217, in from_vllm_config
(APIServer pid=6602)     return cls(
(APIServer pid=6602)            ^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 146, in __init__
(APIServer pid=6602)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=6602)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 132, in make_async_mp_client
(APIServer pid=6602)     return AsyncMPClient(*client_args)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 963, in __init__
(APIServer pid=6602)     super().__init__(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 573, in __init__
(APIServer pid=6602)     with launch_core_engines(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 144, in __exit__
(APIServer pid=6602)     next(self.gen)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1213, in launch_core_engines
(APIServer pid=6602)     wait_for_engine_startup(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1272, in wait_for_engine_startup
(APIServer pid=6602)     raise RuntimeError(
(APIServer pid=6602) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
/usr/lib/python3.12/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 8 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm |    sglang |
| :------------------------ | -----------: | ---: | --------: |
| TTFT median (ms)          |        137.7 |    - |  **85.8** |
| TPOT median (ms)          |     **37.3** |    - |      42.8 |
| E2E median (ms)           |        161.3 |    - | **140.4** |
| Throughput median (tok/s) |          8.1 |    - |   **9.7** |
| Correctness               |          97% |    - |       97% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7206:8921 [6] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO comm 0x1e76c590 rank 6 nranks 8 cudaDev 6 busId b9000 - Abort COMPLETE
[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-809ee492:7202:7202 [2] NCCL INFO comm 0x33eb8a30 rank 2 nranks 8 cudaDev 2 busId 75000 - Destroy COMPLETE
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nRanks 8 cudaDev 2 busId 75000 - Abort START
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:8927 [2] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nranks 8 cudaDev 2 busId 75000 - Abort COMPLETE
gpu-dev-809ee492:7205:7205 [5] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) ERROR 07-01 21:37:22 [multiproc_executor.py:284] Worker proc VllmWorker-5 died unexpectedly, shutting down executor.
(EngineCore pid=7001) INFO 07-01 21:37:22 [multiproc_executor.py:426] [shutdown] Executor: waiting for worker exit count=8
gpu-dev-809ee492:7203:7203 [3] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7201:7201 [1] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7207:7207 [7] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7200:7200 [0] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7202:7202 [2] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7204:7204 [4] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7206:7206 [6] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) Process EngineCore:
(EngineCore pid=7001) Traceback (most recent call last):
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore pid=7001)     self.run()
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore pid=7001)     self._target(*self._args, **self._kwargs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1235, in run_engine_core
(EngineCore pid=7001)     raise e
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1200, in run_engine_core
(EngineCore pid=7001)     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore pid=7001)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 966, in __init__
(EngineCore pid=7001)     super().__init__(
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 133, in __init__
(EngineCore pid=7001)     kv_cache_config = self._initialize_kv_caches(vllm_config)
(EngineCore pid=7001)                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 321, in _initialize_kv_caches
(EngineCore pid=7001)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/abstract.py", line 124, in initialize_from_config
(EngineCore pid=7001)     compilation_times: list[CompilationTimes] = self.collective_rpc(
(EngineCore pid=7001)                                                 ^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 402, in collective_rpc
(EngineCore pid=7001)     return future if non_block else future.result()
(EngineCore pid=7001)                                     ^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 91, in result
(EngineCore pid=7001)     return super().result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 449, in result
(EngineCore pid=7001)     return self.__get_result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
(EngineCore pid=7001)     raise self._exception
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 95, in _wait_for_response
(EngineCore pid=7001)     response = self.aggregate(self.get_response())
(EngineCore pid=7001)                               ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 391, in get_response
(EngineCore pid=7001)     raise RuntimeError(
(EngineCore pid=7001) RuntimeError: Worker failed with error 'The buffer size in the given workspace is insufficient for the given problem size. Buffer: 1048576 bytes, Required: 4194304 bytes.', please check the stack trace above for the root cause
(APIServer pid=6602) Traceback (most recent call last):
(APIServer pid=6602)   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=6602)   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 732, in <module>
(APIServer pid=6602)     uvloop.run(run_server(args))
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run
(APIServer pid=6602)     return __asyncio.run(
(APIServer pid=6602)            ^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run
(APIServer pid=6602)     return runner.run(main)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
(APIServer pid=6602)     return self._loop.run_until_complete(task)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=6602)     return await main
(APIServer pid=6602)            ^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 692, in run_server
(APIServer pid=6602)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 706, in run_server_worker
(APIServer pid=6602)     async with build_async_engine_client(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 100, in build_async_engine_client
(APIServer pid=6602)     async with build_async_engine_client_from_engine_args(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 136, in build_async_engine_client_from_engine_args
(APIServer pid=6602)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=6602)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 217, in from_vllm_config
(APIServer pid=6602)     return cls(
(APIServer pid=6602)            ^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 146, in __init__
(APIServer pid=6602)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=6602)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 132, in make_async_mp_client
(APIServer pid=6602)     return AsyncMPClient(*client_args)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 963, in __init__
(APIServer pid=6602)     super().__init__(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 573, in __init__
(APIServer pid=6602)     with launch_core_engines(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 144, in __exit__
(APIServer pid=6602)     next(self.gen)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1213, in launch_core_engines
(APIServer pid=6602)     wait_for_engine_startup(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1272, in wait_for_engine_startup
(APIServer pid=6602)     raise RuntimeError(
(APIServer pid=6602) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
/usr/lib/python3.12/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 8 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm |    sglang |
| :------------------------ | -----------: | ---: | --------: |
| TTFT median (ms)          |        246.9 |    - |  **82.5** |
| TPOT median (ms)          |         22.4 |    - |  **21.8** |
| E2E median (ms)           |       1051.4 |    - | **875.3** |
| Throughput median (tok/s) |         34.6 |    - |  **41.4** |
| Correctness               |         100% |    - |      100% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7206:8921 [6] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7206:10537 [6] NCCL INFO comm 0x1e76c590 rank 6 nranks 8 cudaDev 6 busId b9000 - Abort COMPLETE
[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-809ee492:7202:7202 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-809ee492:7202:7202 [2] NCCL INFO comm 0x33eb8a30 rank 2 nranks 8 cudaDev 2 busId 75000 - Destroy COMPLETE
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nRanks 8 cudaDev 2 busId 75000 - Abort START
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:64 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:81 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO misc/socket.cc:868 -> 3
gpu-dev-809ee492:7202:8927 [2] NCCL INFO misc/socket.cc:943 -> 3
gpu-dev-809ee492:7202:10538 [2] NCCL INFO comm 0x192f6d70 rank 2 nranks 8 cudaDev 2 busId 75000 - Abort COMPLETE
gpu-dev-809ee492:7205:7205 [5] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) ERROR 07-01 21:37:22 [multiproc_executor.py:284] Worker proc VllmWorker-5 died unexpectedly, shutting down executor.
(EngineCore pid=7001) INFO 07-01 21:37:22 [multiproc_executor.py:426] [shutdown] Executor: waiting for worker exit count=8
gpu-dev-809ee492:7203:7203 [3] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7201:7201 [1] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7207:7207 [7] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7200:7200 [0] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7202:7202 [2] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7204:7204 [4] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
gpu-dev-809ee492:7206:7206 [6] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
(EngineCore pid=7001) Process EngineCore:
(EngineCore pid=7001) Traceback (most recent call last):
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore pid=7001)     self.run()
(EngineCore pid=7001)   File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore pid=7001)     self._target(*self._args, **self._kwargs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1235, in run_engine_core
(EngineCore pid=7001)     raise e
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 1200, in run_engine_core
(EngineCore pid=7001)     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore pid=7001)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 966, in __init__
(EngineCore pid=7001)     super().__init__(
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 133, in __init__
(EngineCore pid=7001)     kv_cache_config = self._initialize_kv_caches(vllm_config)
(EngineCore pid=7001)                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=7001)     return func(*args, **kwargs)
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core.py", line 321, in _initialize_kv_caches
(EngineCore pid=7001)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/abstract.py", line 124, in initialize_from_config
(EngineCore pid=7001)     compilation_times: list[CompilationTimes] = self.collective_rpc(
(EngineCore pid=7001)                                                 ^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 402, in collective_rpc
(EngineCore pid=7001)     return future if non_block else future.result()
(EngineCore pid=7001)                                     ^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 91, in result
(EngineCore pid=7001)     return super().result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 449, in result
(EngineCore pid=7001)     return self.__get_result()
(EngineCore pid=7001)            ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
(EngineCore pid=7001)     raise self._exception
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 95, in _wait_for_response
(EngineCore pid=7001)     response = self.aggregate(self.get_response())
(EngineCore pid=7001)                               ^^^^^^^^^^^^^^^^^^^
(EngineCore pid=7001)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/executor/multiproc_executor.py", line 391, in get_response
(EngineCore pid=7001)     raise RuntimeError(
(EngineCore pid=7001) RuntimeError: Worker failed with error 'The buffer size in the given workspace is insufficient for the given problem size. Buffer: 1048576 bytes, Required: 4194304 bytes.', please check the stack trace above for the root cause
(APIServer pid=6602) Traceback (most recent call last):
(APIServer pid=6602)   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=6602)   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 732, in <module>
(APIServer pid=6602)     uvloop.run(run_server(args))
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run
(APIServer pid=6602)     return __asyncio.run(
(APIServer pid=6602)            ^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run
(APIServer pid=6602)     return runner.run(main)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
(APIServer pid=6602)     return self._loop.run_until_complete(task)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=6602)     return await main
(APIServer pid=6602)            ^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 692, in run_server
(APIServer pid=6602)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 706, in run_server_worker
(APIServer pid=6602)     async with build_async_engine_client(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 100, in build_async_engine_client
(APIServer pid=6602)     async with build_async_engine_client_from_engine_args(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=6602)     return await anext(self.gen)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/entrypoints/openai/api_server.py", line 136, in build_async_engine_client_from_engine_args
(APIServer pid=6602)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=6602)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 217, in from_vllm_config
(APIServer pid=6602)     return cls(
(APIServer pid=6602)            ^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/async_llm.py", line 146, in __init__
(APIServer pid=6602)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=6602)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 132, in make_async_mp_client
(APIServer pid=6602)     return AsyncMPClient(*client_args)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=6602)     return func(*args, **kwargs)
(APIServer pid=6602)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 963, in __init__
(APIServer pid=6602)     super().__init__(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/core_client.py", line 573, in __init__
(APIServer pid=6602)     with launch_core_engines(
(APIServer pid=6602)   File "/usr/lib/python3.12/contextlib.py", line 144, in __exit__
(APIServer pid=6602)     next(self.gen)
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1213, in launch_core_engines
(APIServer pid=6602)     wait_for_engine_startup(
(APIServer pid=6602)   File "/workspace/submit-809ee492/builds/vllm/vllm/v1/engine/utils.py", line 1272, in wait_for_engine_startup
(APIServer pid=6602)     raise RuntimeError(
(APIServer pid=6602) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
/usr/lib/python3.12/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 8 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm |    sglang |
| :------------------------ | -----------: | ---: | --------: |
| TTFT median (ms)          |        199.2 |    - | **145.5** |
| TPOT median (ms)          |     **34.2** |    - |      49.4 |
| E2E median (ms)           |        386.5 |    - | **382.8** |
| Throughput median (tok/s) |         11.7 |    - |  **12.7** |
| Correctness               |          98% |    - |       99% |
