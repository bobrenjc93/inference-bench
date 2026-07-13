# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **39.7s (0.7m)** | `96adc9d` |
| vllm         |    377.3s (6.3m) | `487dfb3` |
| sglang       |    173.1s (2.9m) | `874fc07` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        140.3 |      84.7 | **80.5** |
| TPOT median (ms)          |     **32.1** |      37.1 |     64.8 |
| E2E median (ms)           |        165.2 | **116.3** |    138.2 |
| Throughput median (tok/s) |          7.0 |  **11.9** |      9.8 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **53.5** | 70.6 |  122.0 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **71.6** | 87.6 |  195.4 |
| Throughput median (tok/s) |     **14.0** | 11.4 |    5.1 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        189.4 | **72.1** |   84.8 |
| TPOT median (ms)          |     **35.3** |     39.1 |   74.8 |
| E2E median (ms)           |        218.6 | **96.4** |  148.4 |
| Throughput median (tok/s) |          5.2 | **12.6** |    9.2 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.5 | **35.2** |   51.8 |
| TPOT median (ms)          |         34.5 | **23.3** |  363.1 |
| E2E median (ms)           |         73.0 | **53.4** |  428.1 |
| Throughput median (tok/s) |         20.0 | **24.5** |    3.4 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        186.6 |  **46.7** |   50.9 |
| TPOT median (ms)          |         19.6 |  **15.3** |   24.2 |
| E2E median (ms)           |        875.5 | **573.1** |  919.2 |
| Throughput median (tok/s) |         40.8 |  **60.9** |   40.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.4 |  **61.9** |   78.0 |
| TPOT median (ms)          |         24.3 |  **23.0** |  105.4 |
| E2E median (ms)           |        280.8 | **185.4** |  365.8 |
| Throughput median (tok/s) |         17.4 |  **24.3** |   13.5 |
| Correctness               |          98% |       99% |    98% |
