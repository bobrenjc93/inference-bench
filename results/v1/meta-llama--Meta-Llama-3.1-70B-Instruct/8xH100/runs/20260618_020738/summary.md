# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, Jun 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     423.9s (7.1m) | `ccca738` |
| vllm         |     551.4s (9.2m) | `b409217` |
| sglang       | **296.8s (4.9m)** | `9888b7b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **133.4** |  137.6 |
| TPOT median (ms)          |            - |  **46.1** |   72.8 |
| E2E median (ms)           |            - | **174.6** |  205.0 |
| Throughput median (tok/s) |            - |   **8.0** |    5.9 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 13/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **191.8** |  221.8 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **213.8** |  365.3 |
| Throughput median (tok/s) |            - |   **4.7** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 13/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     159.2 | **158.9** |
| TPOT median (ms)          |            - |  **53.8** |      97.2 |
| E2E median (ms)           |            - | **202.7** |     256.4 |
| Throughput median (tok/s) |            - |   **6.8** |       5.3 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 13/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **57.8** |   80.4 |
| TPOT median (ms)          |            - | **28.6** |   46.1 |
| E2E median (ms)           |            - | **79.4** |  135.2 |
| Throughput median (tok/s) |            - | **15.1** |   10.0 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 13/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **64.8** |   67.9 |
| TPOT median (ms)          |            - |  **15.2** |   22.6 |
| E2E median (ms)           |            - | **618.5** |  850.1 |
| Throughput median (tok/s) |            - |  **58.7** |   42.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 13/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-62a01c4c:1118:1118 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1119:1119 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1115:1115 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1117:1117 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1116:1116 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1120:1120 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1114:1114 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-62a01c4c:1113:1113 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **121.4** |  133.3 |
| TPOT median (ms)          |            - |  **28.7** |   47.7 |
| E2E median (ms)           |            - | **257.8** |  362.4 |
| Throughput median (tok/s) |            - |  **18.7** |   13.2 |
| Correctness               |            - |       98% |    99% |
