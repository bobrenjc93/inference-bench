# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 19 2026

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
| torchinferno |     394.0s (6.6m) | `31187b4` |
| vllm         |     463.6s (7.7m) | `ec67d7a` |
| sglang       | **293.2s (4.9m)** | `9bb9d17` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **141.0** |  143.8 |
| TPOT median (ms)          |            - |  **46.4** |   71.7 |
| E2E median (ms)           |            - | **179.5** |  210.3 |
| Throughput median (tok/s) |            - |   **7.9** |    5.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **172.3** |  215.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **193.3** |  355.9 |
| Throughput median (tok/s) |            - |   **5.2** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     164.5 | **163.9** |
| TPOT median (ms)          |            - |  **51.8** |     111.0 |
| E2E median (ms)           |            - | **213.2** |     268.0 |
| Throughput median (tok/s) |            - |   **6.4** |       5.0 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.2** |   82.6 |
| TPOT median (ms)          |            - | **28.5** |   55.5 |
| E2E median (ms)           |            - | **80.4** |  150.4 |
| Throughput median (tok/s) |            - | **15.1** |    9.2 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.7 | **70.6** |
| TPOT median (ms)          |            - |  **15.1** |     22.3 |
| E2E median (ms)           |            - | **618.2** |    849.5 |
| Throughput median (tok/s) |            - |  **57.8** |     41.8 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 20/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 21/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 22/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-d1d3b50c:1750:1750 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1748:1748 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1749:1749 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1751:1751 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1746:1746 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1744:1744 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1747:1747 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-d1d3b50c:1745:1745 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **121.4** |  135.2 |
| TPOT median (ms)          |            - |  **28.4** |   52.1 |
| E2E median (ms)           |            - | **256.9** |  366.8 |
| Throughput median (tok/s) |            - |  **18.5** |   12.9 |
| Correctness               |            - |       98% |    98% |
