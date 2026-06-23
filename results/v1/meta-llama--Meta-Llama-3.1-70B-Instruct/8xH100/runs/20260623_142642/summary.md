# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jun 23 2026

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
| torchinferno |     453.3s (7.6m) | `68cbf28` |
| vllm         |   1448.0s (24.1m) | `f59db63` |
| sglang       | **287.8s (4.8m)** | `c67d338` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **132.6** |  152.0 |
| TPOT median (ms)          |            - |  **47.0** |   72.1 |
| E2E median (ms)           |            - | **175.4** |  219.5 |
| Throughput median (tok/s) |            - |   **7.9** |    5.6 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 12/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 14/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 13/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 15/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 16/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 17/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1793:1793 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1791:1791 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1789:1789 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **190.4** |  203.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **212.0** |  345.1 |
| Throughput median (tok/s) |            - |   **4.7** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 12/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 14/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 13/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 15/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 16/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 17/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1793:1793 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1791:1791 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1789:1789 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **163.6** |  167.4 |
| TPOT median (ms)          |            - |  **56.5** |  101.0 |
| E2E median (ms)           |            - | **210.7** |  270.9 |
| Throughput median (tok/s) |            - |   **6.4** |    5.0 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 12/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 14/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 13/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 15/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 16/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 17/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1793:1793 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1791:1791 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1789:1789 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **57.7** |   82.7 |
| TPOT median (ms)          |            - | **28.6** |   46.7 |
| E2E median (ms)           |            - | **80.4** |  140.9 |
| Throughput median (tok/s) |            - | **15.3** |   10.1 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 12/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 14/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 13/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 15/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 16/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 17/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1793:1793 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1791:1791 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1789:1789 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      75.9 | **69.1** |
| TPOT median (ms)          |            - |  **14.8** |     21.9 |
| E2E median (ms)           |            - | **620.6** |    810.1 |
| Throughput median (tok/s) |            - |  **58.6** |     42.9 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 12/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 14/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 21/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 22/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 13/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 15/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Channel 23/0 : 7[7] -> 0[0] via P2P/CUMEM
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Channel 23/0 : 5[5] -> 6[6] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 14/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 16/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 15/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 17/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 16/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 18/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 17/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 19/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 18/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 20/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 19/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 21/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 20/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 22/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 21/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 22/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Channel 23/0 : 3[3] -> 4[4] via P2P/CUMEM
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Channel 23/0 : 1[1] -> 2[2] via P2P/CUMEM
gpu-dev-c6a15b5d:1793:1793 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1794:1794 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1792:1792 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1787:1787 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1791:1791 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1790:1790 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1788:1788 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
gpu-dev-c6a15b5d:1789:1789 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.0** |  134.9 |
| TPOT median (ms)          |            - |  **29.4** |   48.3 |
| E2E median (ms)           |            - | **259.8** |  357.3 |
| Throughput median (tok/s) |            - |  **18.6** |   13.3 |
| Correctness               |            - |       98% |    99% |
