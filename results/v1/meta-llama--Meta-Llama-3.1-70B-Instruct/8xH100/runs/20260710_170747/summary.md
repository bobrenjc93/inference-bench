# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:07 AM PT, Jul 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **36.9s (0.6m)** | `00126b8` |
| vllm         |    297.4s (5.0m) | `c227aaa` |
| sglang       |    211.1s (3.5m) | `7b99900` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      73.8 | **73.6** |
| TPOT median (ms)          |            - |  **37.3** |     66.8 |
| E2E median (ms)           |            - | **103.0** |    128.8 |
| Throughput median (tok/s) |            - |  **12.8** |     10.6 |
| Correctness               |            - |       98% |      98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 3600s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
8 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank2]:[E710 18:00:32.422479216 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 2] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.426182607 ProcessGroupNCCL.cpp:757] [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=59958, OpType=ALLREDUCE, NumelIn=8388608, NumelOut=8388608, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
[rank3]:[E710 18:00:32.426302794 ProcessGroupNCCL.cpp:2395] [PG ID 0 PG GUID 0(default_pg) Rank 3]  failure detected by watchdog at work sequence id: 59958 PG status: last enqueued work: 59998, last completed work: 59957
[rank3]:[E710 18:00:32.427312432 ProcessGroupNCCL.cpp:801] Stack trace of the failed collective: 
#0 all_reduce from /usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py:3174
#1 wrapper from /usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8472
#3 _decode_linear_all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2574
#4 _attention_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2038
#5 forward_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:1986
#6 _forward_prefill_ragged_static from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:5572
#7 _capture_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7445
#8 _run_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7236
#9 try_prefill_ragged_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:6951
#10 _warmup_online_mixed_prefix_suffix_prefill_graphs from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4986
#11 _warmup_unified_scheduler_cache from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4153
#12 _warmup_tensor_parallel_model from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:9334
#13 __init__ from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:3491
#14 build_engine from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13797
#15 serve from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13812
#16 main from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19070
#17 <module> from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19075
#18 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank3]:[E710 18:00:32.427417358 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 3] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.603241927 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E710 18:00:32.603530183 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.686224934 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686262246 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 2] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E710 18:00:32.686365442 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686417085 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E710 18:00:32.686433436 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 7] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E710 18:00:32.686477409 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686652949 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.686716232 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from  rank 3 and we will try our best to dump the debug info. Last enqueued NCCL work: 59957, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686736403 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E710 18:00:32.686795127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E710 18:00:32.686820118 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.687058842 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.690089115 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E710 18:00:32.089607983 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E710 18:00:32.090056919 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[F710 18:08:32.707469047 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank4]:[F710 18:08:32.775586860 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 4] [PG ID 0 PG GUID 0(default_pg) Rank 4] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank5]:[F710 18:08:32.782402239 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 5] [PG ID 0 PG GUID 0(default_pg) Rank 5] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank7]:[F710 18:08:32.789963540 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 7] [PG ID 0 PG GUID 0(default_pg) Rank 7] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank6]:[F710 18:08:32.790053185 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 6] [PG ID 0 PG GUID 0(default_pg) Rank 6] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F710 18:08:32.800745985 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F710 18:08:32.804707381 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank0]:[F710 18:08:33.186771213 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **75.0** |  122.5 |
| TPOT median (ms)          |            - |      0.0 |    0.0 |
| E2E median (ms)           |            - | **94.0** |  207.9 |
| Throughput median (tok/s) |            - | **10.6** |    4.8 |
| Correctness               |            - |     100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 3600s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
8 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank2]:[E710 18:00:32.422479216 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 2] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.426182607 ProcessGroupNCCL.cpp:757] [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=59958, OpType=ALLREDUCE, NumelIn=8388608, NumelOut=8388608, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
[rank3]:[E710 18:00:32.426302794 ProcessGroupNCCL.cpp:2395] [PG ID 0 PG GUID 0(default_pg) Rank 3]  failure detected by watchdog at work sequence id: 59958 PG status: last enqueued work: 59998, last completed work: 59957
[rank3]:[E710 18:00:32.427312432 ProcessGroupNCCL.cpp:801] Stack trace of the failed collective: 
#0 all_reduce from /usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py:3174
#1 wrapper from /usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8472
#3 _decode_linear_all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2574
#4 _attention_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2038
#5 forward_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:1986
#6 _forward_prefill_ragged_static from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:5572
#7 _capture_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7445
#8 _run_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7236
#9 try_prefill_ragged_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:6951
#10 _warmup_online_mixed_prefix_suffix_prefill_graphs from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4986
#11 _warmup_unified_scheduler_cache from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4153
#12 _warmup_tensor_parallel_model from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:9334
#13 __init__ from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:3491
#14 build_engine from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13797
#15 serve from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13812
#16 main from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19070
#17 <module> from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19075
#18 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank3]:[E710 18:00:32.427417358 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 3] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.603241927 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E710 18:00:32.603530183 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.686224934 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686262246 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 2] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E710 18:00:32.686365442 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686417085 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E710 18:00:32.686433436 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 7] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E710 18:00:32.686477409 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686652949 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.686716232 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from  rank 3 and we will try our best to dump the debug info. Last enqueued NCCL work: 59957, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686736403 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E710 18:00:32.686795127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E710 18:00:32.686820118 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.687058842 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.690089115 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E710 18:00:32.089607983 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E710 18:00:32.090056919 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[F710 18:08:32.707469047 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank4]:[F710 18:08:32.775586860 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 4] [PG ID 0 PG GUID 0(default_pg) Rank 4] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank5]:[F710 18:08:32.782402239 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 5] [PG ID 0 PG GUID 0(default_pg) Rank 5] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank7]:[F710 18:08:32.789963540 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 7] [PG ID 0 PG GUID 0(default_pg) Rank 7] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank6]:[F710 18:08:32.790053185 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 6] [PG ID 0 PG GUID 0(default_pg) Rank 6] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F710 18:08:32.800745985 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F710 18:08:32.804707381 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank0]:[F710 18:08:33.186771213 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      84.7 | **79.8** |
| TPOT median (ms)          |            - |  **39.7** |     82.0 |
| E2E median (ms)           |            - | **114.0** |    148.2 |
| Throughput median (tok/s) |            - |  **12.1** |      9.3 |
| Correctness               |            - |       98% |      98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 3600s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
8 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank2]:[E710 18:00:32.422479216 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 2] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.426182607 ProcessGroupNCCL.cpp:757] [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=59958, OpType=ALLREDUCE, NumelIn=8388608, NumelOut=8388608, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
[rank3]:[E710 18:00:32.426302794 ProcessGroupNCCL.cpp:2395] [PG ID 0 PG GUID 0(default_pg) Rank 3]  failure detected by watchdog at work sequence id: 59958 PG status: last enqueued work: 59998, last completed work: 59957
[rank3]:[E710 18:00:32.427312432 ProcessGroupNCCL.cpp:801] Stack trace of the failed collective: 
#0 all_reduce from /usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py:3174
#1 wrapper from /usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8472
#3 _decode_linear_all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2574
#4 _attention_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2038
#5 forward_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:1986
#6 _forward_prefill_ragged_static from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:5572
#7 _capture_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7445
#8 _run_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7236
#9 try_prefill_ragged_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:6951
#10 _warmup_online_mixed_prefix_suffix_prefill_graphs from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4986
#11 _warmup_unified_scheduler_cache from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4153
#12 _warmup_tensor_parallel_model from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:9334
#13 __init__ from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:3491
#14 build_engine from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13797
#15 serve from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13812
#16 main from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19070
#17 <module> from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19075
#18 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank3]:[E710 18:00:32.427417358 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 3] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.603241927 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E710 18:00:32.603530183 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.686224934 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686262246 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 2] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E710 18:00:32.686365442 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686417085 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E710 18:00:32.686433436 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 7] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E710 18:00:32.686477409 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686652949 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.686716232 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from  rank 3 and we will try our best to dump the debug info. Last enqueued NCCL work: 59957, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686736403 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E710 18:00:32.686795127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E710 18:00:32.686820118 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.687058842 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.690089115 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E710 18:00:32.089607983 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E710 18:00:32.090056919 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[F710 18:08:32.707469047 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank4]:[F710 18:08:32.775586860 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 4] [PG ID 0 PG GUID 0(default_pg) Rank 4] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank5]:[F710 18:08:32.782402239 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 5] [PG ID 0 PG GUID 0(default_pg) Rank 5] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank7]:[F710 18:08:32.789963540 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 7] [PG ID 0 PG GUID 0(default_pg) Rank 7] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank6]:[F710 18:08:32.790053185 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 6] [PG ID 0 PG GUID 0(default_pg) Rank 6] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F710 18:08:32.800745985 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F710 18:08:32.804707381 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank0]:[F710 18:08:33.186771213 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **32.1** |   41.0 |
| TPOT median (ms)          |            - | **21.5** |  130.1 |
| E2E median (ms)           |            - | **47.7** |  133.5 |
| Throughput median (tok/s) |            - | **26.1** |   10.9 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 3600s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
8 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank2]:[E710 18:00:32.422479216 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 2] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.426182607 ProcessGroupNCCL.cpp:757] [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=59958, OpType=ALLREDUCE, NumelIn=8388608, NumelOut=8388608, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
[rank3]:[E710 18:00:32.426302794 ProcessGroupNCCL.cpp:2395] [PG ID 0 PG GUID 0(default_pg) Rank 3]  failure detected by watchdog at work sequence id: 59958 PG status: last enqueued work: 59998, last completed work: 59957
[rank3]:[E710 18:00:32.427312432 ProcessGroupNCCL.cpp:801] Stack trace of the failed collective: 
#0 all_reduce from /usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py:3174
#1 wrapper from /usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8472
#3 _decode_linear_all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2574
#4 _attention_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2038
#5 forward_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:1986
#6 _forward_prefill_ragged_static from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:5572
#7 _capture_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7445
#8 _run_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7236
#9 try_prefill_ragged_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:6951
#10 _warmup_online_mixed_prefix_suffix_prefill_graphs from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4986
#11 _warmup_unified_scheduler_cache from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4153
#12 _warmup_tensor_parallel_model from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:9334
#13 __init__ from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:3491
#14 build_engine from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13797
#15 serve from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13812
#16 main from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19070
#17 <module> from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19075
#18 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank3]:[E710 18:00:32.427417358 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 3] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.603241927 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E710 18:00:32.603530183 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.686224934 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686262246 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 2] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E710 18:00:32.686365442 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686417085 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E710 18:00:32.686433436 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 7] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E710 18:00:32.686477409 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686652949 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.686716232 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from  rank 3 and we will try our best to dump the debug info. Last enqueued NCCL work: 59957, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686736403 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E710 18:00:32.686795127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E710 18:00:32.686820118 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.687058842 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.690089115 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E710 18:00:32.089607983 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E710 18:00:32.090056919 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[F710 18:08:32.707469047 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank4]:[F710 18:08:32.775586860 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 4] [PG ID 0 PG GUID 0(default_pg) Rank 4] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank5]:[F710 18:08:32.782402239 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 5] [PG ID 0 PG GUID 0(default_pg) Rank 5] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank7]:[F710 18:08:32.789963540 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 7] [PG ID 0 PG GUID 0(default_pg) Rank 7] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank6]:[F710 18:08:32.790053185 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 6] [PG ID 0 PG GUID 0(default_pg) Rank 6] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F710 18:08:32.800745985 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F710 18:08:32.804707381 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank0]:[F710 18:08:33.186771213 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **45.8** |   49.2 |
| TPOT median (ms)          |            - |  **15.3** |   24.6 |
| E2E median (ms)           |            - | **570.7** |  899.5 |
| Throughput median (tok/s) |            - |  **61.5** |   39.3 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 3600s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
8 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank2]:[E710 18:00:32.422479216 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 2] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.426182607 ProcessGroupNCCL.cpp:757] [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=59958, OpType=ALLREDUCE, NumelIn=8388608, NumelOut=8388608, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
[rank3]:[E710 18:00:32.426302794 ProcessGroupNCCL.cpp:2395] [PG ID 0 PG GUID 0(default_pg) Rank 3]  failure detected by watchdog at work sequence id: 59958 PG status: last enqueued work: 59998, last completed work: 59957
[rank3]:[E710 18:00:32.427312432 ProcessGroupNCCL.cpp:801] Stack trace of the failed collective: 
#0 all_reduce from /usr/local/lib/python3.12/dist-packages/torch/distributed/distributed_c10d.py:3174
#1 wrapper from /usr/local/lib/python3.12/dist-packages/torch/distributed/c10d_logger.py:83
#2 _all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:8472
#3 _decode_linear_all_reduce from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2574
#4 _attention_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:2038
#5 forward_prefill_ragged from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:1986
#6 _forward_prefill_ragged_static from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:5572
#7 _capture_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7445
#8 _run_ragged_prefill_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:7236
#9 try_prefill_ragged_logits_graph from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/models/llama3/tensor_parallel.py:6951
#10 _warmup_online_mixed_prefix_suffix_prefill_graphs from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4986
#11 _warmup_unified_scheduler_cache from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:4153
#12 _warmup_tensor_parallel_model from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:9334
#13 __init__ from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:3491
#14 build_engine from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13797
#15 serve from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:13812
#16 main from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19070
#17 <module> from /workspace/submit-bd371d5d/builds/torchinferno/src/torchinferno/openai_server.py:19075
#18 _run_code from <frozen runpy>:88
#19 _run_module_as_main from <frozen runpy>:198

[rank3]:[E710 18:00:32.427417358 ProcessGroupNCCL.cpp:2732] [PG ID 0 PG GUID 0(default_pg) Rank 3] First PG on this rank to signal dumping.
[rank3]:[E710 18:00:32.603241927 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 3] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank3]:[E710 18:00:32.603530183 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 3] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.686224934 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 1] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686262246 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 2] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank5]:[E710 18:00:32.686365442 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 5] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686417085 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 6] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank7]:[E710 18:00:32.686433436 ProcessGroupNCCL.cpp:1922] [PG ID 0 PG GUID 0(default_pg) Rank 7] Observed flight recorder dump signal from another rank via TCPStore.
[rank4]:[E710 18:00:32.686477409 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 4] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank2]:[E710 18:00:32.686652949 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 2] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.686716232 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 7] Received a dump signal due to a collective timeout from  rank 3 and we will try our best to dump the debug info. Last enqueued NCCL work: 59957, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank6]:[E710 18:00:32.686736403 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 6] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank5]:[E710 18:00:32.686795127 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 5] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank4]:[E710 18:00:32.686820118 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 4] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank7]:[E710 18:00:32.687058842 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 7] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank1]:[E710 18:00:32.690089115 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank0]:[E710 18:00:32.089607983 ProcessGroupNCCL.cpp:1987] [PG ID 0 PG GUID 0(default_pg) Rank 0] Received a dump signal due to a collective timeout from this local rank and we will try our best to dump the debug info. Last enqueued NCCL work: 59998, last completed NCCL work: 59957.This is most likely caused by incorrect usages of collectives, e.g., wrong sizes used across ranks, the order of collectives is not same for all ranks or the scheduled collective, for some reason, didn't run. Additionally, this can be caused by GIL deadlock or other reasons such as network errors or bugs in the communications library (e.g. NCCL), etc. 
[rank0]:[E710 18:00:32.090056919 ProcessGroupNCCL.cpp:1700] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL preparing to dump debug info. Include stack trace: 1, only active collectives: 0
[rank3]:[F710 18:08:32.707469047 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 3] [PG ID 0 PG GUID 0(default_pg) Rank 3] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank4]:[F710 18:08:32.775586860 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 4] [PG ID 0 PG GUID 0(default_pg) Rank 4] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank5]:[F710 18:08:32.782402239 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 5] [PG ID 0 PG GUID 0(default_pg) Rank 5] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank7]:[F710 18:08:32.789963540 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 7] [PG ID 0 PG GUID 0(default_pg) Rank 7] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank6]:[F710 18:08:32.790053185 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 6] [PG ID 0 PG GUID 0(default_pg) Rank 6] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank2]:[F710 18:08:32.800745985 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 2] [PG ID 0 PG GUID 0(default_pg) Rank 2] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank1]:[F710 18:08:32.804707381 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 1] [PG ID 0 PG GUID 0(default_pg) Rank 1] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
[rank0]:[F710 18:08:33.186771213 ProcessGroupNCCL.cpp:1725] [PG ID 0 PG GUID 0(default_pg) Rank 0] [PG ID 0 PG GUID 0(default_pg) Rank 0] Terminating the process after attempting to dump debug info, due to collective timeout or exception.
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **62.3** |   73.2 |
| TPOT median (ms)          |            - |  **22.8** |   60.7 |
| E2E median (ms)           |            - | **185.9** |  303.6 |
| Throughput median (tok/s) |            - |  **24.6** |   15.0 |
| Correctness               |            - |       99% |    99% |
