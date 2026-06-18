# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 18 2026

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
| torchinferno |     483.9s (8.1m) | `ccca738` |
| vllm         |     515.2s (8.6m) | `7022141` |
| sglang       | **280.9s (4.7m)** | `5900126` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **137.3** |  141.1 |
| TPOT median (ms)          |            - |  **45.3** |   72.8 |
| E2E median (ms)           |            - | **171.7** |  208.3 |
| Throughput median (tok/s) |            - |   **8.2** |    5.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 17/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1120:1120 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1121:1121 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1117:1117 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **191.9** |  218.2 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **245.8** |  361.2 |
| Throughput median (tok/s) |            - |   **4.1** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 17/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1120:1120 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1121:1121 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1117:1117 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **161.9** |  163.0 |
| TPOT median (ms)          |            - |  **52.0** |   96.6 |
| E2E median (ms)           |            - | **209.3** |  258.6 |
| Throughput median (tok/s) |            - |   **6.6** |    5.4 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 17/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1120:1120 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1121:1121 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1117:1117 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **57.5** |   81.4 |
| TPOT median (ms)          |            - | **29.8** |   43.9 |
| E2E median (ms)           |            - | **78.8** |  137.0 |
| Throughput median (tok/s) |            - | **15.3** |   10.1 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 17/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1120:1120 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1121:1121 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1117:1117 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **71.8** |   73.8 |
| TPOT median (ms)          |            - |  **15.1** |   22.4 |
| E2E median (ms)           |            - | **614.8** |  851.3 |
| Throughput median (tok/s) |            - |  **58.8** |   41.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 17/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-6b384697:1115:1115 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1114:1114 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1120:1120 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1116:1116 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1121:1121 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1119:1119 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1118:1118 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-6b384697:1117:1117 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.1** |  135.5 |
| TPOT median (ms)          |            - |  **28.5** |   47.1 |
| E2E median (ms)           |            - | **264.1** |  363.3 |
| Throughput median (tok/s) |            - |  **18.6** |   13.1 |
| Correctness               |            - |       98% |    98% |
