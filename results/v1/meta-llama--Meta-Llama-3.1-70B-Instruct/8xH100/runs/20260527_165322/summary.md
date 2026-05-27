# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:35 AM PT, May 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     442.4s (7.4m) | `21e9c2a` |
| vllm         |   1394.0s (23.2m) | `49a3510` |
| sglang       | **260.0s (4.3m)** | `a95b4e2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |    167.0 | **143.2** |
| TPOT median (ms)          |            - | **59.3** |      73.2 |
| E2E median (ms)           |            - |    224.1 | **211.1** |
| Throughput median (tok/s) |            - |  **6.6** |       5.8 |
| Correctness               |            - |      98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **182.8** |  202.0 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **204.8** |  328.6 |
| Throughput median (tok/s) |            - |   **4.9** |    3.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     171.4 | **160.2** |
| TPOT median (ms)          |            - |  **64.4** |     101.0 |
| E2E median (ms)           |            - | **228.1** |     261.7 |
| Throughput median (tok/s) |            - |   **6.0** |       5.0 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.0** |   78.3 |
| TPOT median (ms)          |            - | **26.6** |   56.3 |
| E2E median (ms)           |            - | **79.1** |  151.8 |
| Throughput median (tok/s) |            - | **15.7** |    9.2 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      79.5 | **77.4** |
| TPOT median (ms)          |            - |  **14.9** |     23.1 |
| E2E median (ms)           |            - | **621.2** |    868.2 |
| Throughput median (tok/s) |            - |  **57.9** |     40.6 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **131.9** |  132.2 |
| TPOT median (ms)          |            - |  **33.0** |   50.7 |
| E2E median (ms)           |            - | **271.5** |  364.3 |
| Throughput median (tok/s) |            - |  **18.2** |   12.7 |
| Correctness               |            - |       98% |    99% |
