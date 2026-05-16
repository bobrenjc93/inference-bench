# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:07 PM PT, May 15 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **2/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     296.2s (4.9m) | `cbfd345` |
| vllm         |   1089.9s (18.2m) | `32b7177` |
| sglang       | **167.0s (2.8m)** | `416fdbb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        283.4 |     157.1 | **141.9** |
| TPOT median (ms)          |        148.3 |  **58.9** |      76.1 |
| E2E median (ms)           |        367.3 | **206.4** |     214.3 |
| Throughput median (tok/s) |          3.9 |   **7.3** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        242.1 | **192.8** |  201.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        312.3 | **216.6** |  338.2 |
| Throughput median (tok/s) |          3.2 |   **4.6** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        492.2 |     173.4 | **149.8** |
| TPOT median (ms)          |         98.6 |  **57.2** |     109.1 |
| E2E median (ms)           |        603.4 | **228.5** |     251.7 |
| Throughput median (tok/s) |          2.2 |   **6.3** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        306.3 | **57.6** |   75.4 |
| TPOT median (ms)          |        129.0 | **27.1** |   60.1 |
| E2E median (ms)           |        409.6 | **78.1** |  147.5 |
| Throughput median (tok/s) |          3.7 | **15.6** |    9.8 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        517.9 |      67.0 | **65.7** |
| TPOT median (ms)          |     **15.0** |      15.0 |     21.6 |
| E2E median (ms)           |       1218.9 | **616.4** |    807.7 |
| Throughput median (tok/s) |         28.1 |  **59.3** |     43.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        368.4 |     129.6 | **126.9** |
| TPOT median (ms)          |         78.2 |  **31.6** |      53.4 |
| E2E median (ms)           |        582.3 | **269.2** |     351.9 |
| Throughput median (tok/s) |          8.2 |  **18.6** |      13.4 |
| Correctness               |          99% |       98% |       99% |
