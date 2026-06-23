# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, Jun 22 2026

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
| torchinferno |     520.8s (8.7m) | `721a3c0` |
| vllm         |    623.5s (10.4m) | `430a95a` |
| sglang       | **307.4s (5.1m)** | `b42c79c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **140.6** |  141.1 |
| TPOT median (ms)          |            - |  **49.4** |   77.7 |
| E2E median (ms)           |            - | **181.5** |  215.1 |
| Throughput median (tok/s) |            - |   **7.8** |    5.5 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **179.0** |  208.5 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **203.7** |  343.9 |
| Throughput median (tok/s) |            - |   **4.9** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **162.9** |  166.1 |
| TPOT median (ms)          |            - |  **48.7** |   92.1 |
| E2E median (ms)           |            - | **208.1** |  265.7 |
| Throughput median (tok/s) |            - |   **6.6** |    5.1 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **60.8** |   83.9 |
| TPOT median (ms)          |            - | **28.9** |   46.1 |
| E2E median (ms)           |            - | **82.4** |  144.3 |
| Throughput median (tok/s) |            - | **14.5** |    9.8 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      71.1 | **69.3** |
| TPOT median (ms)          |            - |  **15.1** |     22.6 |
| E2E median (ms)           |            - | **620.4** |    850.6 |
| Throughput median (tok/s) |            - |  **58.8** |     41.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 20/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-f8f4794f:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-f8f4794f:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **122.9** |  133.8 |
| TPOT median (ms)          |            - |  **28.4** |   47.7 |
| E2E median (ms)           |            - | **259.2** |  363.9 |
| Throughput median (tok/s) |            - |  **18.5** |   13.0 |
| Correctness               |            - |       99% |    99% |
