# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.8s (0.7m)** | `390fed4` |
| vllm         |    168.5s (2.8m) | `3775d5f` |
| sglang       |    158.6s (2.6m) | `7820dc6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     147.4 | **140.6** |
| TPOT median (ms)          |            - |  **47.6** |      77.9 |
| E2E median (ms)           |            - | **194.5** |     218.3 |
| Throughput median (tok/s) |            - |   **7.2** |       5.6 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
ine 17245, in <module>
[rank3]:     raise SystemExit(main())
[rank3]:                      ^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank3]:     serve(config)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank3]:     engine = build_engine(config)
[rank3]:              ^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank3]:     return OpenAICompletionEngine(
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank3]:     self._warmup_tensor_parallel_model()
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank3]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank3]:     dist.barrier(group=control_group)
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank3]:     return func(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank3]:     work.wait()
[rank3]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:78] Timed out waiting 1800000ms for recv operation to complete
[rank4]: Traceback (most recent call last):
[rank4]:   File "<frozen runpy>", line 198, in _run_module_as_main
[rank4]:   File "<frozen runpy>", line 88, in _run_code
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17245, in <module>
[rank4]:     raise SystemExit(main())
[rank4]:                      ^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank4]:     serve(config)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank4]:     engine = build_engine(config)
[rank4]:              ^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank4]:     return OpenAICompletionEngine(
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank4]:     self._warmup_tensor_parallel_model()
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank4]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank4]:     dist.barrier(group=control_group)
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank4]:     return func(*args, **kwargs)
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank4]:     work.wait()
[rank4]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:129] Timed out waiting 1800000ms for send operation to complete
[rank5]:[E703 17:54:18.884325830 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 17:54:18.884528282 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 17:54:18.885028751 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E703 17:54:18.885229863 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 56390, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 17:54:18.885602805 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 17:54:18.890523705 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 17:54:18.890685055 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[E703 17:54:18.122082307 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 0] Observed flight recorder dump signal from another rank via TCPStore.
[rank0]:[E703 17:54:18.122312280 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E703 17:54:18.122743436 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E703 17:54:18.128934371 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 0] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank0]:[E703 17:54:18.129046747 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 17:54:20.705647947 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 17:54:21.884000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 17:54:21.888000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 17:54:21.892000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 17:54:21.899000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
W0703 17:54:21.900000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1728 closing signal SIGTERM
E0703 17:54:25.355000 925 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 5 (pid: 1726) of binary: /workspace/submit-7e2c4824/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1020, in <module>
    main()
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1016, in main
    run(args)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
torchinferno.openai_server FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1721)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1721
[2]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 2 (local_rank: 2)
  exitcode  : -15 (pid: 1723)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1723
[4]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1724)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1724
[5]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 4 (local_rank: 4)
  exitcode  : -15 (pid: 1725)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1725
[6]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 6 (local_rank: 6)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
[7]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1728)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1728
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_17:54:21
  host      : gpu-dev-7e2c4824
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **198.4** |  213.9 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **221.5** |  380.5 |
| Throughput median (tok/s) |            - |   **4.5** |    2.6 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
ine 17245, in <module>
[rank3]:     raise SystemExit(main())
[rank3]:                      ^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank3]:     serve(config)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank3]:     engine = build_engine(config)
[rank3]:              ^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank3]:     return OpenAICompletionEngine(
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank3]:     self._warmup_tensor_parallel_model()
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank3]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank3]:     dist.barrier(group=control_group)
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank3]:     return func(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank3]:     work.wait()
[rank3]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:78] Timed out waiting 1800000ms for recv operation to complete
[rank4]: Traceback (most recent call last):
[rank4]:   File "<frozen runpy>", line 198, in _run_module_as_main
[rank4]:   File "<frozen runpy>", line 88, in _run_code
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17245, in <module>
[rank4]:     raise SystemExit(main())
[rank4]:                      ^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank4]:     serve(config)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank4]:     engine = build_engine(config)
[rank4]:              ^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank4]:     return OpenAICompletionEngine(
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank4]:     self._warmup_tensor_parallel_model()
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank4]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank4]:     dist.barrier(group=control_group)
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank4]:     return func(*args, **kwargs)
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank4]:     work.wait()
[rank4]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:129] Timed out waiting 1800000ms for send operation to complete
[rank5]:[E703 17:54:18.884325830 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 17:54:18.884528282 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 17:54:18.885028751 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E703 17:54:18.885229863 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 56390, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 17:54:18.885602805 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 17:54:18.890523705 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 17:54:18.890685055 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[E703 17:54:18.122082307 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 0] Observed flight recorder dump signal from another rank via TCPStore.
[rank0]:[E703 17:54:18.122312280 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E703 17:54:18.122743436 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E703 17:54:18.128934371 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 0] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank0]:[E703 17:54:18.129046747 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 17:54:20.705647947 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 17:54:21.884000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 17:54:21.888000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 17:54:21.892000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 17:54:21.899000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
W0703 17:54:21.900000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1728 closing signal SIGTERM
E0703 17:54:25.355000 925 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 5 (pid: 1726) of binary: /workspace/submit-7e2c4824/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1020, in <module>
    main()
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1016, in main
    run(args)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
torchinferno.openai_server FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1721)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1721
[2]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 2 (local_rank: 2)
  exitcode  : -15 (pid: 1723)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1723
[4]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1724)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1724
[5]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 4 (local_rank: 4)
  exitcode  : -15 (pid: 1725)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1725
[6]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 6 (local_rank: 6)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
[7]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1728)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1728
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_17:54:21
  host      : gpu-dev-7e2c4824
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **121.1** |  168.0 |
| TPOT median (ms)          |            - |  **68.5** |  102.7 |
| E2E median (ms)           |            - | **189.9** |  273.9 |
| Throughput median (tok/s) |            - |   **6.9** |    4.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
ine 17245, in <module>
[rank3]:     raise SystemExit(main())
[rank3]:                      ^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank3]:     serve(config)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank3]:     engine = build_engine(config)
[rank3]:              ^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank3]:     return OpenAICompletionEngine(
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank3]:     self._warmup_tensor_parallel_model()
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank3]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank3]:     dist.barrier(group=control_group)
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank3]:     return func(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank3]:     work.wait()
[rank3]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:78] Timed out waiting 1800000ms for recv operation to complete
[rank4]: Traceback (most recent call last):
[rank4]:   File "<frozen runpy>", line 198, in _run_module_as_main
[rank4]:   File "<frozen runpy>", line 88, in _run_code
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17245, in <module>
[rank4]:     raise SystemExit(main())
[rank4]:                      ^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank4]:     serve(config)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank4]:     engine = build_engine(config)
[rank4]:              ^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank4]:     return OpenAICompletionEngine(
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank4]:     self._warmup_tensor_parallel_model()
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank4]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank4]:     dist.barrier(group=control_group)
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank4]:     return func(*args, **kwargs)
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank4]:     work.wait()
[rank4]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:129] Timed out waiting 1800000ms for send operation to complete
[rank5]:[E703 17:54:18.884325830 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 17:54:18.884528282 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 17:54:18.885028751 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E703 17:54:18.885229863 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 56390, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 17:54:18.885602805 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 17:54:18.890523705 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 17:54:18.890685055 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[E703 17:54:18.122082307 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 0] Observed flight recorder dump signal from another rank via TCPStore.
[rank0]:[E703 17:54:18.122312280 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E703 17:54:18.122743436 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E703 17:54:18.128934371 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 0] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank0]:[E703 17:54:18.129046747 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 17:54:20.705647947 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 17:54:21.884000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 17:54:21.888000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 17:54:21.892000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 17:54:21.899000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
W0703 17:54:21.900000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1728 closing signal SIGTERM
E0703 17:54:25.355000 925 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 5 (pid: 1726) of binary: /workspace/submit-7e2c4824/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1020, in <module>
    main()
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1016, in main
    run(args)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
torchinferno.openai_server FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1721)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1721
[2]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 2 (local_rank: 2)
  exitcode  : -15 (pid: 1723)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1723
[4]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1724)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1724
[5]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 4 (local_rank: 4)
  exitcode  : -15 (pid: 1725)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1725
[6]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 6 (local_rank: 6)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
[7]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1728)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1728
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_17:54:21
  host      : gpu-dev-7e2c4824
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **61.9** |   73.4 |
| TPOT median (ms)          |            - | **29.6** |   56.9 |
| E2E median (ms)           |            - | **84.0** |  137.3 |
| Throughput median (tok/s) |            - | **14.4** |   10.0 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
ine 17245, in <module>
[rank3]:     raise SystemExit(main())
[rank3]:                      ^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank3]:     serve(config)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank3]:     engine = build_engine(config)
[rank3]:              ^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank3]:     return OpenAICompletionEngine(
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank3]:     self._warmup_tensor_parallel_model()
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank3]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank3]:     dist.barrier(group=control_group)
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank3]:     return func(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank3]:     work.wait()
[rank3]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:78] Timed out waiting 1800000ms for recv operation to complete
[rank4]: Traceback (most recent call last):
[rank4]:   File "<frozen runpy>", line 198, in _run_module_as_main
[rank4]:   File "<frozen runpy>", line 88, in _run_code
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17245, in <module>
[rank4]:     raise SystemExit(main())
[rank4]:                      ^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank4]:     serve(config)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank4]:     engine = build_engine(config)
[rank4]:              ^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank4]:     return OpenAICompletionEngine(
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank4]:     self._warmup_tensor_parallel_model()
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank4]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank4]:     dist.barrier(group=control_group)
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank4]:     return func(*args, **kwargs)
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank4]:     work.wait()
[rank4]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:129] Timed out waiting 1800000ms for send operation to complete
[rank5]:[E703 17:54:18.884325830 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 17:54:18.884528282 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 17:54:18.885028751 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E703 17:54:18.885229863 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 56390, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 17:54:18.885602805 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 17:54:18.890523705 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 17:54:18.890685055 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[E703 17:54:18.122082307 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 0] Observed flight recorder dump signal from another rank via TCPStore.
[rank0]:[E703 17:54:18.122312280 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E703 17:54:18.122743436 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E703 17:54:18.128934371 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 0] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank0]:[E703 17:54:18.129046747 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 17:54:20.705647947 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 17:54:21.884000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 17:54:21.888000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 17:54:21.892000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 17:54:21.899000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
W0703 17:54:21.900000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1728 closing signal SIGTERM
E0703 17:54:25.355000 925 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 5 (pid: 1726) of binary: /workspace/submit-7e2c4824/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1020, in <module>
    main()
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1016, in main
    run(args)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
torchinferno.openai_server FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1721)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1721
[2]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 2 (local_rank: 2)
  exitcode  : -15 (pid: 1723)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1723
[4]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1724)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1724
[5]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 4 (local_rank: 4)
  exitcode  : -15 (pid: 1725)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1725
[6]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 6 (local_rank: 6)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
[7]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1728)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1728
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_17:54:21
  host      : gpu-dev-7e2c4824
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      81.2 | **71.7** |
| TPOT median (ms)          |            - |  **15.1** |     22.5 |
| E2E median (ms)           |            - | **623.2** |    860.9 |
| Throughput median (tok/s) |            - |  **56.7** |     41.5 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
ine 17245, in <module>
[rank3]:     raise SystemExit(main())
[rank3]:                      ^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank3]:     serve(config)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank3]:     engine = build_engine(config)
[rank3]:              ^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank3]:     return OpenAICompletionEngine(
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank3]:     self._warmup_tensor_parallel_model()
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank3]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank3]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank3]:     dist.barrier(group=control_group)
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank3]:     return func(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank3]:     work.wait()
[rank3]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:78] Timed out waiting 1800000ms for recv operation to complete
[rank4]: Traceback (most recent call last):
[rank4]:   File "<frozen runpy>", line 198, in _run_module_as_main
[rank4]:   File "<frozen runpy>", line 88, in _run_code
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17245, in <module>
[rank4]:     raise SystemExit(main())
[rank4]:                      ^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 17240, in main
[rank4]:     serve(config)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12214, in serve
[rank4]:     engine = build_engine(config)
[rank4]:              ^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12199, in build_engine
[rank4]:     return OpenAICompletionEngine(
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 2978, in __init__
[rank4]:     self._warmup_tensor_parallel_model()
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 7754, in _warmup_tensor_parallel_model
[rank4]:     _sync_tensor_parallel_command(self.model, self.device, cuda_sync=False)
[rank4]:   File "/workspace/submit-7e2c4824/builds/torchinferno/src/torchinferno/openai_server.py", line 12718, in _sync_tensor_parallel_command
[rank4]:     dist.barrier(group=control_group)
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank4]:     return func(*args, **kwargs)
[rank4]:            ^^^^^^^^^^^^^^^^^^^^^
[rank4]:   File "/usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py", line 5237, in barrier
[rank4]:     work.wait()
[rank4]: RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/unbound_buffer.cc:129] Timed out waiting 1800000ms for send operation to complete
[rank5]:[E703 17:54:18.884325830 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 17:54:18.884528282 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 17:54:18.885028751 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E703 17:54:18.885229863 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 56390, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 17:54:18.885602805 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 17:54:18.890523705 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 17:54:18.890685055 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[E703 17:54:18.122082307 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 0] Observed flight recorder dump signal from another rank via TCPStore.
[rank0]:[E703 17:54:18.122312280 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E703 17:54:18.122743436 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E703 17:54:18.128934371 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 0] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank0]:[E703 17:54:18.129046747 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 17:54:20.705647947 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 17:54:21.884000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 17:54:21.887000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 17:54:21.888000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 17:54:21.892000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 17:54:21.899000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
W0703 17:54:21.900000 925 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1728 closing signal SIGTERM
E0703 17:54:25.355000 925 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 5 (pid: 1726) of binary: /workspace/submit-7e2c4824/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1020, in <module>
    main()
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1016, in main
    run(args)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
torchinferno.openai_server FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1721)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1721
[2]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 2 (local_rank: 2)
  exitcode  : -15 (pid: 1723)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1723
[4]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1724)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1724
[5]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 4 (local_rank: 4)
  exitcode  : -15 (pid: 1725)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1725
[6]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 6 (local_rank: 6)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
[7]:
  time      : 2026-07-03_17:54:25
  host      : gpu-dev-7e2c4824
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1728)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1728
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_17:54:21
  host      : gpu-dev-7e2c4824
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **122.0** |  133.6 |
| TPOT median (ms)          |            - |  **32.2** |   52.0 |
| E2E median (ms)           |            - | **262.6** |  374.2 |
| Throughput median (tok/s) |            - |  **18.0** |   12.9 |
| Correctness               |            - |       99% |    99% |
