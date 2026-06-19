# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:09 AM PT, Jun 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     408.2s (6.8m) | `31187b4` |
| vllm         |     481.9s (8.0m) | `b9a7cd4` |
| sglang       | **258.3s (4.3m)** | `cab6285` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **130.6** |  146.5 |
| TPOT median (ms)          |            - |  **45.4** |   70.3 |
| E2E median (ms)           |            - | **169.5** |  215.3 |
| Throughput median (tok/s) |            - |   **8.0** |    5.5 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 14/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 15/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **173.5** |  218.3 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **203.6** |  359.2 |
| Throughput median (tok/s) |            - |   **4.9** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 14/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 15/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **155.4** |  158.0 |
| TPOT median (ms)          |            - |  **53.3** |  100.4 |
| E2E median (ms)           |            - | **197.2** |  254.9 |
| Throughput median (tok/s) |            - |   **6.8** |    5.3 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 14/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 15/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **57.9** |   78.2 |
| TPOT median (ms)          |            - | **29.5** |   54.2 |
| E2E median (ms)           |            - | **80.6** |  137.2 |
| Throughput median (tok/s) |            - | **15.1** |   10.1 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 14/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 15/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      67.9 | **67.8** |
| TPOT median (ms)          |            - |  **15.1** |     22.4 |
| E2E median (ms)           |            - | **627.3** |    826.3 |
| Throughput median (tok/s) |            - |  **58.6** |     42.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 15/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 14/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 15/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 16/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 17/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 18/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 19/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-34d01721:1748:1748 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1746:1746 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1749:1749 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1747:1747 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1742:1742 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1745:1745 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1743:1743 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-34d01721:1744:1744 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **117.0** |  133.8 |
| TPOT median (ms)          |            - |  **28.7** |   49.4 |
| E2E median (ms)           |            - | **255.6** |  358.6 |
| Throughput median (tok/s) |            - |  **18.7** |   13.2 |
| Correctness               |            - |       99% |    99% |
