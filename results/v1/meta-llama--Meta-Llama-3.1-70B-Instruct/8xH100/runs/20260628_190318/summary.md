# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 PM PT, Jun 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     359.4s (6.0m) | `4000a03` |
| vllm         |     529.0s (8.8m) | `c2127a2` |
| sglang       | **258.5s (4.3m)** | `ad30a99` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        208.1 |     143.8 | **143.4** |
| TPOT median (ms)          |     **46.8** |      47.4 |      74.8 |
| E2E median (ms)           |        251.8 | **185.5** |     214.6 |
| Throughput median (tok/s) |          5.2 |   **7.6** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        280.7 | **186.9** |  213.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        300.7 | **211.4** |  350.3 |
| Throughput median (tok/s) |          3.3 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        414.2 | **163.3** |  165.9 |
| TPOT median (ms)          |         58.5 |  **51.0** |  104.5 |
| E2E median (ms)           |        470.7 | **206.4** |  268.2 |
| Throughput median (tok/s) |          2.9 |   **6.4** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        264.2 | **64.5** |   80.4 |
| TPOT median (ms)          |         42.6 | **32.7** |   44.8 |
| E2E median (ms)           |        310.0 | **89.2** |  133.4 |
| Throughput median (tok/s) |          4.3 | **13.4** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        288.3 |      79.1 | **69.9** |
| TPOT median (ms)          |         21.5 |  **14.8** |     22.2 |
| E2E median (ms)           |       1060.7 | **638.6** |    839.3 |
| Throughput median (tok/s) |         34.9 |  **57.9** |     41.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        291.1 | **127.5** |  134.6 |
| TPOT median (ms)          |         33.9 |  **29.2** |   49.2 |
| E2E median (ms)           |        478.8 | **266.2** |  361.2 |
| Throughput median (tok/s) |         10.1 |  **18.0** |   13.1 |
| Correctness               |          98% |       98% |    99% |
