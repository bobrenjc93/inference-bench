# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jul 3 2026

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
| torchinferno | **37.7s (0.6m)** | `390fed4` |
| vllm         |    193.4s (3.2m) | `576bf75` |
| sglang       |    158.9s (2.6m) | `0203c60` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     152.1 | **139.9** |
| TPOT median (ms)          |            - |  **56.5** |      78.7 |
| E2E median (ms)           |            - | **204.4** |     212.6 |
| Throughput median (tok/s) |            - |   **7.1** |       5.8 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank4]:[E703 19:54:01.074837389 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 19:54:01.074864660 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 19:54:01.074889492 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 19:54:01.074934955 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 19:54:01.074938485 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 19:54:01.075158078 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.075188990 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 19:54:01.075293226 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E703 19:54:01.075335608 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079045558 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.079050678 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079159914 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079741159 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079776931 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079880097 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079866236 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 19:54:01.080343174 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 19:54:01.080440950 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.084753215 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 19:54:01.084925105 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 19:54:01.085246604 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 19:54:01.088895509 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.089017127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.090815993 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 19:54:01.090944961 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 19:54:02.987437457 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 19:54:05.198000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1720 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 19:54:05.205000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
E0703 19:54:08.482000 924 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 6 (pid: 1726) of binary: /workspace/submit-1898538b/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1720)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1720
[2]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1721) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1723) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1724) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1725) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_19:54:05
  host      : gpu-dev-1898538b
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **138.3** |  217.9 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **224.9** |  371.9 |
| Throughput median (tok/s) |            - |   **4.4** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank4]:[E703 19:54:01.074837389 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 19:54:01.074864660 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 19:54:01.074889492 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 19:54:01.074934955 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 19:54:01.074938485 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 19:54:01.075158078 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.075188990 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 19:54:01.075293226 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E703 19:54:01.075335608 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079045558 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.079050678 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079159914 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079741159 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079776931 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079880097 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079866236 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 19:54:01.080343174 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 19:54:01.080440950 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.084753215 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 19:54:01.084925105 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 19:54:01.085246604 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 19:54:01.088895509 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.089017127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.090815993 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 19:54:01.090944961 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 19:54:02.987437457 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 19:54:05.198000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1720 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 19:54:05.205000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
E0703 19:54:08.482000 924 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 6 (pid: 1726) of binary: /workspace/submit-1898538b/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1720)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1720
[2]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1721) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1723) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1724) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1725) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_19:54:05
  host      : gpu-dev-1898538b
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     173.2 | **163.4** |
| TPOT median (ms)          |            - |  **57.2** |     101.8 |
| E2E median (ms)           |            - | **223.4** |     266.1 |
| Throughput median (tok/s) |            - |   **6.3** |       5.1 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank4]:[E703 19:54:01.074837389 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 19:54:01.074864660 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 19:54:01.074889492 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 19:54:01.074934955 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 19:54:01.074938485 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 19:54:01.075158078 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.075188990 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 19:54:01.075293226 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E703 19:54:01.075335608 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079045558 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.079050678 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079159914 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079741159 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079776931 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079880097 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079866236 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 19:54:01.080343174 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 19:54:01.080440950 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.084753215 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 19:54:01.084925105 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 19:54:01.085246604 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 19:54:01.088895509 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.089017127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.090815993 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 19:54:01.090944961 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 19:54:02.987437457 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 19:54:05.198000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1720 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 19:54:05.205000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
E0703 19:54:08.482000 924 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 6 (pid: 1726) of binary: /workspace/submit-1898538b/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1720)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1720
[2]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1721) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1723) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1724) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1725) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_19:54:05
  host      : gpu-dev-1898538b
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **64.8** |   74.9 |
| TPOT median (ms)          |            - | **30.7** |   63.6 |
| E2E median (ms)           |            - | **88.0** |  149.8 |
| Throughput median (tok/s) |            - | **13.6** |    9.5 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank4]:[E703 19:54:01.074837389 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 19:54:01.074864660 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 19:54:01.074889492 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 19:54:01.074934955 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 19:54:01.074938485 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 19:54:01.075158078 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.075188990 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 19:54:01.075293226 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E703 19:54:01.075335608 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079045558 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.079050678 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079159914 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079741159 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079776931 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079880097 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079866236 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 19:54:01.080343174 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 19:54:01.080440950 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.084753215 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 19:54:01.084925105 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 19:54:01.085246604 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 19:54:01.088895509 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.089017127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.090815993 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 19:54:01.090944961 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 19:54:02.987437457 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 19:54:05.198000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1720 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 19:54:05.205000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
E0703 19:54:08.482000 924 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 6 (pid: 1726) of binary: /workspace/submit-1898538b/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1720)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1720
[2]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1721) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1723) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1724) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1725) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_19:54:05
  host      : gpu-dev-1898538b
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      88.0 | **72.1** |
| TPOT median (ms)          |            - |  **15.1** |     21.8 |
| E2E median (ms)           |            - | **678.1** |    806.0 |
| Throughput median (tok/s) |            - |  **56.0** |     42.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank4]:[E703 19:54:01.074837389 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E703 19:54:01.074864660 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E703 19:54:01.074889492 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E703 19:54:01.074934955 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E703 19:54:01.074938485 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E703 19:54:01.075158078 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.075188990 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank2]:[E703 19:54:01.075293226 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E703 19:54:01.075335608 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079045558 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 6] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.079050678 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank6]:[E703 19:54:01.079159914 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079741159 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 3] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079776931 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 2] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank2]:[E703 19:54:01.079880097 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank3]:[E703 19:54:01.079866236 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank4]:[E703 19:54:01.080343174 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 4] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank4]:[E703 19:54:01.080440950 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.084753215 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 1] Observed flight recorder dump signal from another rank via TCPStore.
[rank1]:[E703 19:54:01.084925105 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from  rank 7 and we will try our best to dump the debug info. Last enqueued NCCL work: 56116, last completed NCCL work: 56116.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E703 19:54:01.085246604 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E703 19:54:01.088895509 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 5] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank5]:[E703 19:54:01.089017127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank1]:[E703 19:54:01.090815993 ProcessGroupNCCL.cpp:1442] [PG ID 0 PG GUID 0(default_pg) Rank 1] Exception thrown when waiting for future Flight recorder dump in heartbeatMonitor: std::future_error: Broken promise
[rank1]:[E703 19:54:01.090944961 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 0, only active collectives: 0
[rank0]:[W703 19:54:02.987437457 ProcessGroupNCCL.cpp:1647] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
W0703 19:54:05.198000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1720 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1721 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1722 closing signal SIGTERM
W0703 19:54:05.202000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1723 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1724 closing signal SIGTERM
W0703 19:54:05.203000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1725 closing signal SIGTERM
W0703 19:54:05.205000 924 torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1727 closing signal SIGTERM
E0703 19:54:08.482000 924 torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: 1) local_rank: 6 (pid: 1726) of binary: /workspace/submit-1898538b/builds/torchinferno/venv/bin/python
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
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1720)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1720
[2]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 1721) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[3]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1722) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[4]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 1723) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[5]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 4 (local_rank: 4)
  exitcode  : 1 (pid: 1724) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[6]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 5 (local_rank: 5)
  exitcode  : 1 (pid: 1725) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
[7]:
  time      : 2026-07-03_19:54:08
  host      : gpu-dev-1898538b
  rank      : 7 (local_rank: 7)
  exitcode  : -15 (pid: 1727)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1727
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-03_19:54:05
  host      : gpu-dev-1898538b
  rank      : 6 (local_rank: 6)
  exitcode  : 1 (pid: 1726) 
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **123.3** |  133.6 |
| TPOT median (ms)          |            - |  **31.9** |   53.2 |
| E2E median (ms)           |            - | **283.7** |  361.3 |
| Throughput median (tok/s) |            - |  **17.5** |   13.1 |
| Correctness               |            - |       98% |    98% |
