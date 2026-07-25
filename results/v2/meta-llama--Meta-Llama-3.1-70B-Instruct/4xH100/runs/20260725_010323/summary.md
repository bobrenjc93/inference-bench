# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `bc2ec7444e006a919dc6a1cfd7d1bed3b540704e`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** vllm=4/4, sglang=4/4
- **Observed GPU products:** vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`afbd005dede8e1fb6e3963386ddc41b232662a65`; vllm=`318b527cc2d1f672683407be05ea26a2cf1f3ea6` + build patch `d22bf8e0c0e1802dc97fcb8743d32ecc762682c00f595f2b82434af9f0b94ca6`; sglang=`95865de24f2e6a18e9df1ea0a567933c3bb57379` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 6:03 PM PT, Jul 24 2026

## Integrity Warnings

- **torchinferno:** TorchInferno score-facing cache integrity could not be verified (queue profile is missing). Treat TorchInferno metrics in this run as not comparable.
- **torchinferno:** Provider reported benchmark or deployment errors under the result eligibility policy.
- **torchinferno:** Benchmark 'few_shot' has no completed result.
- **torchinferno:** Benchmark 'self_consistency' has no completed result.
- **torchinferno:** Benchmark 'multi_turn' has no completed result.
- **torchinferno:** Benchmark 'tree_of_thought' has no completed result.
- **torchinferno:** Benchmark 'long_output' has no completed result.

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          N/C |       2/4 |    2/4 |
| self_consistency |          N/C |   **3/4** |    0/4 |
| multi_turn       |          N/C |   **3/4** |    1/4 |
| tree_of_thought  |          N/C |   **4/4** |    0/4 |
| long_output      |          N/C |   **3/4** |    1/4 |
| **Total**        |          N/C | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.
N/C = excluded from scoring because integrity validation did not pass.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     283.0s (4.7m) | `afbd005` |
| vllm         | **199.1s (3.3m)** | `318b527` |
| sglang       |     260.4s (4.3m) | `95865de` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |    106.4 |  **81.6** |
| TPOT median (ms)          |            - | **51.3** |      72.9 |
| E2E median (ms)           |            - |    152.3 | **143.0** |
| Throughput median (tok/s) |            - | **10.0** |       9.4 |
| Correctness               |            - |      98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
sed across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E725 02:39:40.652862705 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E725 02:39:41.236667746 ProcessGroupNCCL.cpp:1914] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 39892, last completed NCCL work: 39891.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E725 02:39:41.236830486 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E725 02:39:41.244128842 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:10212
#3 _decode_linear_all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3399
#4 <lambda> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3176
#5 _profile_block from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3972
#6 _mlp_project_decode_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3174
#7 forward_prefill_packed_fa3 from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2364
#8 _prefill_token_bucket_fa3_compute from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7753
#9 _capture_token_bucket_prefill_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8009
#10 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7849
#11 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#12 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#13 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#14 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#15 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#16 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#17 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#18 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#19 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#20 _run_code from <frozen runpy>:88
#21 _run_module_as_main from <frozen runpy>:198

[rank2]:[E725 02:39:41.250064633 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank1]:[E725 02:39:41.276054820 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank0]:[F725 02:47:41.268394894 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank3]:[F725 02:47:41.270717775 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F725 02:47:41.273829861 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F725 02:47:41.302399705 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
W0725 02:52:42.657000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1730 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1731 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
E0725 02:52:43.388000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 0 (pid: 1729) of binary: /workspace/submit-008082cf/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
=====================================================
torchinferno.openai_server FAILED
-----------------------------------------------------
Failures:
[1]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1730)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1730
[2]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1731)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1731
[3]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1732
-----------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-25_02:52:42
  host      : gpu-dev-008082cf
  rank      : 0 (local_rank: 0)
  exitcode  : -6 (pid: 1729)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1729
=====================================================
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **105.7** |  134.4 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **124.9** |  210.8 |
| Throughput median (tok/s) |            - |   **8.0** |    4.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
sed across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E725 02:39:40.652862705 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E725 02:39:41.236667746 ProcessGroupNCCL.cpp:1914] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 39892, last completed NCCL work: 39891.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E725 02:39:41.236830486 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E725 02:39:41.244128842 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:10212
#3 _decode_linear_all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3399
#4 <lambda> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3176
#5 _profile_block from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3972
#6 _mlp_project_decode_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3174
#7 forward_prefill_packed_fa3 from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2364
#8 _prefill_token_bucket_fa3_compute from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7753
#9 _capture_token_bucket_prefill_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8009
#10 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7849
#11 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#12 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#13 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#14 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#15 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#16 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#17 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#18 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#19 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#20 _run_code from <frozen runpy>:88
#21 _run_module_as_main from <frozen runpy>:198

[rank2]:[E725 02:39:41.250064633 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank1]:[E725 02:39:41.276054820 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank0]:[F725 02:47:41.268394894 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank3]:[F725 02:47:41.270717775 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F725 02:47:41.273829861 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F725 02:47:41.302399705 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
W0725 02:52:42.657000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1730 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1731 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
E0725 02:52:43.388000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 0 (pid: 1729) of binary: /workspace/submit-008082cf/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
=====================================================
torchinferno.openai_server FAILED
-----------------------------------------------------
Failures:
[1]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1730)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1730
[2]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1731)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1731
[3]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1732
-----------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-25_02:52:42
  host      : gpu-dev-008082cf
  rank      : 0 (local_rank: 0)
  exitcode  : -6 (pid: 1729)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1729
=====================================================
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |     101.4 | **84.9** |
| TPOT median (ms)          |            - |  **54.2** |     84.9 |
| E2E median (ms)           |            - | **147.7** |    154.3 |
| Throughput median (tok/s) |            - |   **9.6** |      8.7 |
| Correctness               |            - |       98% |      98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
sed across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E725 02:39:40.652862705 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E725 02:39:41.236667746 ProcessGroupNCCL.cpp:1914] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 39892, last completed NCCL work: 39891.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E725 02:39:41.236830486 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E725 02:39:41.244128842 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:10212
#3 _decode_linear_all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3399
#4 <lambda> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3176
#5 _profile_block from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3972
#6 _mlp_project_decode_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3174
#7 forward_prefill_packed_fa3 from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2364
#8 _prefill_token_bucket_fa3_compute from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7753
#9 _capture_token_bucket_prefill_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8009
#10 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7849
#11 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#12 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#13 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#14 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#15 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#16 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#17 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#18 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#19 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#20 _run_code from <frozen runpy>:88
#21 _run_module_as_main from <frozen runpy>:198

[rank2]:[E725 02:39:41.250064633 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank1]:[E725 02:39:41.276054820 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank0]:[F725 02:47:41.268394894 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank3]:[F725 02:47:41.270717775 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F725 02:47:41.273829861 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F725 02:47:41.302399705 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
W0725 02:52:42.657000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1730 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1731 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
E0725 02:52:43.388000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 0 (pid: 1729) of binary: /workspace/submit-008082cf/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
=====================================================
torchinferno.openai_server FAILED
-----------------------------------------------------
Failures:
[1]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1730)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1730
[2]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1731)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1731
[3]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1732
-----------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-25_02:52:42
  host      : gpu-dev-008082cf
  rank      : 0 (local_rank: 0)
  exitcode  : -6 (pid: 1729)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1729
=====================================================
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **48.8** |   55.2 |
| TPOT median (ms)          |            - | **34.2** |  170.7 |
| E2E median (ms)           |            - | **72.7** |  241.1 |
| Throughput median (tok/s) |            - | **16.8** |    5.6 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
sed across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E725 02:39:40.652862705 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E725 02:39:41.236667746 ProcessGroupNCCL.cpp:1914] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 39892, last completed NCCL work: 39891.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E725 02:39:41.236830486 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E725 02:39:41.244128842 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:10212
#3 _decode_linear_all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3399
#4 <lambda> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3176
#5 _profile_block from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3972
#6 _mlp_project_decode_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3174
#7 forward_prefill_packed_fa3 from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2364
#8 _prefill_token_bucket_fa3_compute from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7753
#9 _capture_token_bucket_prefill_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8009
#10 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7849
#11 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#12 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#13 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#14 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#15 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#16 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#17 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#18 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#19 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#20 _run_code from <frozen runpy>:88
#21 _run_module_as_main from <frozen runpy>:198

[rank2]:[E725 02:39:41.250064633 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank1]:[E725 02:39:41.276054820 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank0]:[F725 02:47:41.268394894 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank3]:[F725 02:47:41.270717775 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F725 02:47:41.273829861 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F725 02:47:41.302399705 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
W0725 02:52:42.657000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1730 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1731 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
E0725 02:52:43.388000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 0 (pid: 1729) of binary: /workspace/submit-008082cf/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
=====================================================
torchinferno.openai_server FAILED
-----------------------------------------------------
Failures:
[1]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1730)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1730
[2]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1731)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1731
[3]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1732
-----------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-25_02:52:42
  host      : gpu-dev-008082cf
  rank      : 0 (local_rank: 0)
  exitcode  : -6 (pid: 1729)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1729
=====================================================
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      62.7 | **56.7** |
| TPOT median (ms)          |            - |  **21.2** |     31.2 |
| E2E median (ms)           |            - | **811.5** |   1108.1 |
| Throughput median (tok/s) |            - |  **43.8** |     31.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
sed across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank1]:[E725 02:39:40.652862705 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E725 02:39:41.236667746 ProcessGroupNCCL.cpp:1914] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 39892, last completed NCCL work: 39891.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E725 02:39:41.236830486 ProcessGroupNCCL.cpp:1628] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[E725 02:39:41.244128842 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:10212
#3 _decode_linear_all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3399
#4 <lambda> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3176
#5 _profile_block from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3972
#6 _mlp_project_decode_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:3174
#7 forward_prefill_packed_fa3 from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2364
#8 _prefill_token_bucket_fa3_compute from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7753
#9 _capture_token_bucket_prefill_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8009
#10 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7849
#11 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#12 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#13 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#14 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#15 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#16 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#17 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#18 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#19 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#20 _run_code from <frozen runpy>:88
#21 _run_module_as_main from <frozen runpy>:198

[rank2]:[E725 02:39:41.250064633 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank1]:[E725 02:39:41.276054820 ProcessGroupNCCL.cpp:733] Stack trace of the failed collective: 
#0 all_reduce from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/distributed_c10d.py:3068
#1 wrapper from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/c10d_logger.py:83
#2 _capture_succeeded_on_all_ranks from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:246
#3 try_prefill_token_bucket_fa3_graph from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7871
#4 decorate_context from /workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py:124
#5 _warmup_token_bucket_fa3_prefill_graphs from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3956
#6 _warmup_unified_scheduler_cache from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:3746
#7 _warmup_tensor_parallel_model from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:9365
#8 __init__ from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:2871
#9 build_engine from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13868
#10 serve from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:13883
#11 main from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19456
#12 <module> from /workspace/submit-008082cf/builds/v3/torchinferno/src/torchinferno/openai_server.py:19461
#13 _run_code from <frozen runpy>:88
#14 _run_module_as_main from <frozen runpy>:198

[rank0]:[F725 02:47:41.268394894 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank3]:[F725 02:47:41.270717775 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F725 02:47:41.273829861 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F725 02:47:41.302399705 ProcessGroupNCCL.cpp:1653] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
W0725 02:52:42.657000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1730 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1731 closing signal SIGTERM
W0725 02:52:42.658000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
E0725 02:52:43.388000 1234 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 0 (pid: 1729) of binary: /workspace/submit-008082cf/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-008082cf/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
=====================================================
torchinferno.openai_server FAILED
-----------------------------------------------------
Failures:
[1]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1730)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1730
[2]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1731)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1731
[3]:
  time      : 2026-07-25_02:52:43
  host      : gpu-dev-008082cf
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1732
-----------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-25_02:52:42
  host      : gpu-dev-008082cf
  rank      : 0 (local_rank: 0)
  exitcode  : -6 (pid: 1729)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1729
=====================================================
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      85.0 | **82.6** |
| TPOT median (ms)          |            - |  **32.2** |     72.0 |
| E2E median (ms)           |            - | **261.8** |    371.5 |
| Throughput median (tok/s) |            - |  **17.7** |     11.9 |
| Correctness               |            - |       98% |      99% |
