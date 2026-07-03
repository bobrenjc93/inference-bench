# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **23.6s (0.4m)** | `390fed4` |
| vllm         |    214.1s (3.6m) | `3775d5f` |
| sglang       |    164.2s (2.7m) | `486bcb4` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     153.0 | **148.5** |
| TPOT median (ms)          |            - |  **55.0** |      78.1 |
| E2E median (ms)           |            - | **205.8** |     229.0 |
| Throughput median (tok/s) |            - |   **7.0** |       5.4 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 from another rank via TCPStore.
[rank3]:[E703 15:37:17.178057290 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 3] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 15:37:17.178099253 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 15:37:17.178116623 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E703 15:37:17.178360488 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178377689 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 15:37:17.178404831 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 15:37:17.178428962 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178677976 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E703 15:37:17.178786223 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 15:37:17.178883309 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 15:37:17.178922121 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 15:37:17.179008206 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 6] Observed flight recorder dump signal from another rank via TCPStore.
[rank6]:[E703 15:37:17.179206018 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 15:37:17.179616962 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 15:37:17.182070226 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 15:37:17.182181542 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 15:37:17.182737945 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 15:37:17.182873793 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 15:37:17.183015542 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank3]:[E703 15:37:17.183108227 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank6]:[E703 15:37:17.184134157 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank6]:[E703 15:37:17.184308287 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank5]:[E703 15:37:17.186855637 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 15:37:17.186978664 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 15:37:17.195328505 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 15:37:17.195460473 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 15:37:19.669182747 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 15:37:21.320000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1847 closing signal SIGTERM
W0703 15:37:21.322000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1848 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1849 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1851 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1852 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1853 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1854 closing signal SIGTERM
E0703 15:37:24.512000 1051 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 3 (pid: 1850) of binary: /workspace/submit-5cac713d/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1847)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1847
[2]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1848) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1849) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1851) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1852) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1853) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1854)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1854
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_15:37:21
  host      : gpu-dev-5cac713d
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1850) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **183.1** |  219.6 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **206.5** |  376.9 |
| Throughput median (tok/s) |            - |   **4.8** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 from another rank via TCPStore.
[rank3]:[E703 15:37:17.178057290 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 3] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 15:37:17.178099253 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 15:37:17.178116623 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E703 15:37:17.178360488 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178377689 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 15:37:17.178404831 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 15:37:17.178428962 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178677976 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E703 15:37:17.178786223 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 15:37:17.178883309 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 15:37:17.178922121 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 15:37:17.179008206 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 6] Observed flight recorder dump signal from another rank via TCPStore.
[rank6]:[E703 15:37:17.179206018 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 15:37:17.179616962 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 15:37:17.182070226 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 15:37:17.182181542 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 15:37:17.182737945 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 15:37:17.182873793 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 15:37:17.183015542 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank3]:[E703 15:37:17.183108227 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank6]:[E703 15:37:17.184134157 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank6]:[E703 15:37:17.184308287 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank5]:[E703 15:37:17.186855637 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 15:37:17.186978664 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 15:37:17.195328505 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 15:37:17.195460473 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 15:37:19.669182747 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 15:37:21.320000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1847 closing signal SIGTERM
W0703 15:37:21.322000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1848 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1849 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1851 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1852 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1853 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1854 closing signal SIGTERM
E0703 15:37:24.512000 1051 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 3 (pid: 1850) of binary: /workspace/submit-5cac713d/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1847)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1847
[2]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1848) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1849) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1851) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1852) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1853) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1854)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1854
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_15:37:21
  host      : gpu-dev-5cac713d
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1850) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     173.7 | **165.6** |
| TPOT median (ms)          |            - |  **54.3** |     109.5 |
| E2E median (ms)           |            - | **220.0** |     278.9 |
| Throughput median (tok/s) |            - |   **6.2** |       4.9 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 from another rank via TCPStore.
[rank3]:[E703 15:37:17.178057290 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 3] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 15:37:17.178099253 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 15:37:17.178116623 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E703 15:37:17.178360488 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178377689 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 15:37:17.178404831 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 15:37:17.178428962 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178677976 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E703 15:37:17.178786223 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 15:37:17.178883309 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 15:37:17.178922121 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 15:37:17.179008206 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 6] Observed flight recorder dump signal from another rank via TCPStore.
[rank6]:[E703 15:37:17.179206018 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 15:37:17.179616962 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 15:37:17.182070226 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 15:37:17.182181542 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 15:37:17.182737945 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 15:37:17.182873793 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 15:37:17.183015542 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank3]:[E703 15:37:17.183108227 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank6]:[E703 15:37:17.184134157 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank6]:[E703 15:37:17.184308287 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank5]:[E703 15:37:17.186855637 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 15:37:17.186978664 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 15:37:17.195328505 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 15:37:17.195460473 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 15:37:19.669182747 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 15:37:21.320000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1847 closing signal SIGTERM
W0703 15:37:21.322000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1848 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1849 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1851 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1852 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1853 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1854 closing signal SIGTERM
E0703 15:37:24.512000 1051 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 3 (pid: 1850) of binary: /workspace/submit-5cac713d/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1847)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1847
[2]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1848) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1849) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1851) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1852) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1853) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1854)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1854
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_15:37:21
  host      : gpu-dev-5cac713d
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1850) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **62.4** |   72.9 |
| TPOT median (ms)          |            - | **30.4** |   66.8 |
| E2E median (ms)           |            - | **84.9** |  149.5 |
| Throughput median (tok/s) |            - | **14.1** |    9.5 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 from another rank via TCPStore.
[rank3]:[E703 15:37:17.178057290 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 3] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 15:37:17.178099253 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 15:37:17.178116623 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E703 15:37:17.178360488 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178377689 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 15:37:17.178404831 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 15:37:17.178428962 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178677976 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E703 15:37:17.178786223 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 15:37:17.178883309 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 15:37:17.178922121 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 15:37:17.179008206 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 6] Observed flight recorder dump signal from another rank via TCPStore.
[rank6]:[E703 15:37:17.179206018 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 15:37:17.179616962 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 15:37:17.182070226 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 15:37:17.182181542 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 15:37:17.182737945 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 15:37:17.182873793 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 15:37:17.183015542 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank3]:[E703 15:37:17.183108227 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank6]:[E703 15:37:17.184134157 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank6]:[E703 15:37:17.184308287 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank5]:[E703 15:37:17.186855637 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 15:37:17.186978664 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 15:37:17.195328505 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 15:37:17.195460473 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 15:37:19.669182747 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 15:37:21.320000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1847 closing signal SIGTERM
W0703 15:37:21.322000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1848 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1849 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1851 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1852 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1853 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1854 closing signal SIGTERM
E0703 15:37:24.512000 1051 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 3 (pid: 1850) of binary: /workspace/submit-5cac713d/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1847)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1847
[2]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1848) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1849) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1851) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1852) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1853) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1854)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1854
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_15:37:21
  host      : gpu-dev-5cac713d
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1850) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      80.3 | **73.0** |
| TPOT median (ms)          |            - |  **15.1** |     22.3 |
| E2E median (ms)           |            - | **638.6** |    874.0 |
| Throughput median (tok/s) |            - |  **57.2** |     41.5 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 from another rank via TCPStore.
[rank3]:[E703 15:37:17.178057290 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 3] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 15:37:17.178099253 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank5]:[E703 15:37:17.178116623 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 5] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E703 15:37:17.178360488 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178377689 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 15:37:17.178404831 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 15:37:17.178428962 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 15:37:17.178677976 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E703 15:37:17.178786223 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 15:37:17.178883309 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 15:37:17.178922121 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 15:37:17.179008206 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 6] Observed flight recorder dump signal from another rank via TCPStore.
[rank6]:[E703 15:37:17.179206018 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56118, last completed NCCL work: 56118.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 15:37:17.179616962 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 15:37:17.182070226 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 15:37:17.182181542 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 15:37:17.182737945 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 15:37:17.182873793 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 15:37:17.183015542 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank3]:[E703 15:37:17.183108227 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank6]:[E703 15:37:17.184134157 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank6]:[E703 15:37:17.184308287 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank5]:[E703 15:37:17.186855637 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 15:37:17.186978664 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 15:37:17.195328505 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 15:37:17.195460473 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 15:37:19.669182747 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 15:37:21.320000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1847 closing signal SIGTERM
W0703 15:37:21.322000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1848 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1849 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1851 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1852 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1853 closing signal SIGTERM
W0703 15:37:21.323000 1051 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1854 closing signal SIGTERM
E0703 15:37:24.512000 1051 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 3 (pid: 1850) of binary: /workspace/submit-5cac713d/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1847)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1847
[2]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1848) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1849) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1851) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1852) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1853) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_15:37:24
  host      : gpu-dev-5cac713d
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1854)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1854
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_15:37:21
  host      : gpu-dev-5cac713d
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1850) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **130.5** |  135.9 |
| TPOT median (ms)          |            - |  **31.0** |   55.3 |
| E2E median (ms)           |            - | **271.2** |  381.6 |
| Throughput median (tok/s) |            - |  **17.9** |   12.8 |
| Correctness               |            - |       99% |    99% |
