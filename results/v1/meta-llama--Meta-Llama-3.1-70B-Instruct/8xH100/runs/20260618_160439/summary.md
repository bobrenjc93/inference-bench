# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, Jun 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **19/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     381.8s (6.4m) | `ccca738` |
| vllm         |     511.1s (8.5m) | `bf2a393` |
| sglang       | **290.9s (4.8m)** | `0eded9e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **135.8** |  144.2 |
| TPOT median (ms)          |            - |  **47.3** |   72.4 |
| E2E median (ms)           |            - | **174.3** |  210.7 |
| Throughput median (tok/s) |            - |   **8.1** |    5.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 15/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 16/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1119:1119 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1121:1121 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1118:1118 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **191.1** |  219.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **212.4** |  361.3 |
| Throughput median (tok/s) |            - |   **4.7** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 15/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 16/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1119:1119 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1121:1121 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1118:1118 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **154.7** |  159.8 |
| TPOT median (ms)          |            - |  **53.3** |  100.9 |
| E2E median (ms)           |            - | **196.1** |  256.0 |
| Throughput median (tok/s) |            - |   **6.8** |    5.4 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 15/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 16/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1119:1119 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1121:1121 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1118:1118 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.5** |   83.9 |
| TPOT median (ms)          |            - | **30.3** |   39.6 |
| E2E median (ms)           |            - | **81.6** |  134.1 |
| Throughput median (tok/s) |            - | **15.2** |   10.4 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 15/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 16/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1119:1119 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1121:1121 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1118:1118 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **66.2** |   66.7 |
| TPOT median (ms)          |            - |  **15.2** |   22.5 |
| E2E median (ms)           |            - | **604.4** |  836.4 |
| Throughput median (tok/s) |            - |  **58.7** |   42.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 15/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 16/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 17/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-984732c0:1122:1122 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1120:1120 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1123:1123 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1119:1119 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1121:1121 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1118:1118 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1124:1124 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-984732c0:1117:1117 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **121.3** |  134.7 |
| TPOT median (ms)          |            - |  **29.2** |   47.1 |
| E2E median (ms)           |            - | **253.8** |  359.7 |
| Throughput median (tok/s) |            - |  **18.7** |   13.3 |
| Correctness               |            - |       99% |    99% |
