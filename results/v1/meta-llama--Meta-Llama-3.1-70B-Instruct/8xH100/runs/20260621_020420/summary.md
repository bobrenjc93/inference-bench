# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jun 20 2026

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
| torchinferno |     421.7s (7.0m) | `1348cf0` |
| vllm         |     469.6s (7.8m) | `8dd1b70` |
| sglang       | **280.0s (4.7m)** | `c65f4ea` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **141.4** |  143.4 |
| TPOT median (ms)          |            - |  **50.6** |   80.2 |
| E2E median (ms)           |            - | **183.8** |  218.6 |
| Throughput median (tok/s) |            - |   **7.7** |    5.5 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **203.1** |  206.5 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **242.3** |  358.0 |
| Throughput median (tok/s) |            - |   **4.1** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     166.5 | **160.7** |
| TPOT median (ms)          |            - |  **48.5** |     105.4 |
| E2E median (ms)           |            - | **210.3** |     261.0 |
| Throughput median (tok/s) |            - |   **6.6** |       5.1 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.8** |   80.4 |
| TPOT median (ms)          |            - | **29.0** |   62.8 |
| E2E median (ms)           |            - | **81.7** |  158.5 |
| Throughput median (tok/s) |            - | **14.9** |    8.8 |
| Correctness               |            - |      97% |    96% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      71.0 | **69.9** |
| TPOT median (ms)          |            - |  **14.9** |     22.3 |
| E2E median (ms)           |            - | **609.4** |    823.9 |
| Throughput median (tok/s) |            - |  **59.3** |     42.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-dc7d4136:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-dc7d4136:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **128.4** |  132.2 |
| TPOT median (ms)          |            - |  **28.6** |   54.1 |
| E2E median (ms)           |            - | **265.5** |  364.0 |
| Throughput median (tok/s) |            - |  **18.5** |   12.9 |
| Correctness               |            - |       98% |    98% |
