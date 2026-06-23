# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     481.4s (8.0m) | `5f97519` |
| vllm         |     593.7s (9.9m) | `901a3b0` |
| sglang       | **329.9s (5.5m)** | `0460f27` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **139.9** |  143.0 |
| TPOT median (ms)          |            - |  **46.5** |   75.4 |
| E2E median (ms)           |            - | **178.4** |  213.4 |
| Throughput median (tok/s) |            - |   **7.7** |    5.6 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1765:1765 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1763:1763 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **209.3** |  222.7 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **293.1** |  364.2 |
| Throughput median (tok/s) |            - |   **3.4** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1765:1765 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1763:1763 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     162.9 | **160.5** |
| TPOT median (ms)          |            - |  **51.2** |     108.4 |
| E2E median (ms)           |            - | **205.8** |     258.7 |
| Throughput median (tok/s) |            - |   **6.5** |       5.3 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1765:1765 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1763:1763 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **61.5** |   82.4 |
| TPOT median (ms)          |            - | **29.8** |   45.5 |
| E2E median (ms)           |            - | **83.7** |  144.5 |
| Throughput median (tok/s) |            - | **14.6** |   10.0 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1765:1765 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1763:1763 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      82.7 | **75.2** |
| TPOT median (ms)          |            - |  **14.8** |     22.1 |
| E2E median (ms)           |            - | **613.5** |    851.5 |
| Throughput median (tok/s) |            - |  **58.0** |     41.8 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 19/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-a1069b08:1768:1768 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1766:1766 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1769:1769 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1767:1767 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1765:1765 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1763:1763 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1764:1764 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-a1069b08:1762:1762 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **131.2** |  136.8 |
| TPOT median (ms)          |            - |  **28.5** |   50.3 |
| E2E median (ms)           |            - | **274.9** |  366.4 |
| Throughput median (tok/s) |            - |  **18.0** |   13.1 |
| Correctness               |            - |       98% |    99% |
