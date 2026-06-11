# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 PM PT, Jun 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     413.1s (6.9m) | `c208ddb` |
| vllm         |   1460.6s (24.3m) | `e2db022` |
| sglang       | **197.3s (3.3m)** | `125ef88` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        287.5 |     165.8 | **148.4** |
| TPOT median (ms)          |         93.1 |  **60.3** |      69.5 |
| E2E median (ms)           |        368.3 | **216.9** |     217.8 |
| Throughput median (tok/s) |          3.3 |   **6.9** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        375.5 | **204.1** |  211.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        528.6 | **228.1** |  357.2 |
| Throughput median (tok/s) |          1.9 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        636.6 |     181.0 | **174.7** |
| TPOT median (ms)          |     **63.3** |      65.3 |     101.9 |
| E2E median (ms)           |        698.2 | **239.4** |     273.4 |
| Throughput median (tok/s) |          1.8 |   **6.0** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        466.8 | **62.6** |   92.3 |
| TPOT median (ms)          |         55.0 | **26.9** |   42.2 |
| E2E median (ms)           |        505.5 | **84.0** |  152.5 |
| Throughput median (tok/s) |          3.4 | **14.3** |    9.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.2 |  **74.9** |   79.3 |
| TPOT median (ms)          |         27.3 |  **14.8** |   24.1 |
| E2E median (ms)           |       1275.7 | **616.0** |  895.3 |
| Throughput median (tok/s) |         30.6 |  **58.7** |   38.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        391.5 | **137.7** |  141.3 |
| TPOT median (ms)          |         47.7 |  **33.5** |   47.5 |
| E2E median (ms)           |        675.3 | **276.9** |  379.2 |
| Throughput median (tok/s) |          8.2 |  **18.1** |   12.2 |
| Correctness               |          99% |       98% |    99% |
