# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jun 28 2026

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
| torchinferno | **123.5s (2.1m)** | `1702ba1` |
| vllm         |     543.7s (9.1m) | `4dfbf15` |
| sglang       |     265.7s (4.4m) | `b9b8606` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        163.4 | **134.1** |  148.2 |
| TPOT median (ms)          |         50.3 |  **43.2** |   82.3 |
| E2E median (ms)           |        203.7 | **166.9** |  226.5 |
| Throughput median (tok/s) |          5.8 |   **7.9** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        252.2 | **195.6** |  222.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        268.9 | **218.0** |  368.7 |
| Throughput median (tok/s) |          3.7 |   **4.6** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        319.3 | **163.7** |  180.9 |
| TPOT median (ms)          |         58.2 |  **54.4** |  105.2 |
| E2E median (ms)           |        376.3 | **208.6** |  281.5 |
| Throughput median (tok/s) |          3.4 |   **6.6** |    4.6 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        196.2 | **60.7** |   89.0 |
| TPOT median (ms)          |         57.9 | **30.8** |   46.1 |
| E2E median (ms)           |        241.2 | **84.6** |  149.4 |
| Throughput median (tok/s) |          5.8 | **14.4** |    9.1 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        338.4 |      77.7 | **74.1** |
| TPOT median (ms)          |         22.8 |  **15.0** |     22.7 |
| E2E median (ms)           |       1164.9 | **621.8** |    863.0 |
| Throughput median (tok/s) |         31.9 |  **57.9** |     40.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        253.9 | **126.4** |  142.9 |
| TPOT median (ms)          |         37.8 |  **28.7** |   51.3 |
| E2E median (ms)           |        451.0 | **260.0** |  377.8 |
| Throughput median (tok/s) |         10.1 |  **18.3** |   12.5 |
| Correctness               |          98% |       98% |    98% |
