# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 13 2026

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

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     465.9s (7.8m) | `1d4b263` |
| vllm         |   1387.9s (23.1m) | `0d29612` |
| sglang       | **211.1s (3.5m)** | `806365e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     165.6 | **152.5** |
| TPOT median (ms)          |            - |  **61.9** |      73.7 |
| E2E median (ms)           |            - | **220.9** |     223.1 |
| Throughput median (tok/s) |            - |   **6.9** |       5.2 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
a P2P/CUMEM
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **189.4** |  221.3 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **213.2** |  362.0 |
| Throughput median (tok/s) |            - |   **4.7** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
a P2P/CUMEM
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     178.1 | **160.2** |
| TPOT median (ms)          |            - |  **65.4** |     105.1 |
| E2E median (ms)           |            - | **233.8** |     258.8 |
| Throughput median (tok/s) |            - |   **6.0** |       5.2 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
a P2P/CUMEM
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **61.4** |   78.8 |
| TPOT median (ms)          |            - | **29.3** |   48.1 |
| E2E median (ms)           |            - | **83.7** |  142.2 |
| Throughput median (tok/s) |            - | **14.5** |    9.9 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
a P2P/CUMEM
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      68.9 | **68.5** |
| TPOT median (ms)          |            - |  **15.1** |     21.9 |
| E2E median (ms)           |            - | **620.5** |    829.1 |
| Throughput median (tok/s) |            - |  **58.3** |     42.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
a P2P/CUMEM
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 18/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-524f9954:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-524f9954:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **132.7** |  136.3 |
| TPOT median (ms)          |            - |  **34.3** |   49.7 |
| E2E median (ms)           |            - | **274.4** |  363.1 |
| Throughput median (tok/s) |            - |  **18.1** |   13.1 |
| Correctness               |            - |       98% |    99% |
