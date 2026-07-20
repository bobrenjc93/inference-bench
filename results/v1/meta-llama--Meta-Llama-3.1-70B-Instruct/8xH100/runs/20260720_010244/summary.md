# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **46.3s (0.8m)** | `96adc9d` |
| vllm         |    348.0s (5.8m) | `ace9fda` |
| sglang       |    177.4s (3.0m) | `bab1dd0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.1 | **71.7** |   82.0 |
| TPOT median (ms)          |     **31.5** |     37.1 |   67.7 |
| E2E median (ms)           |        165.6 | **96.9** |  138.9 |
| Throughput median (tok/s) |          7.0 | **13.4** |    9.7 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **54.3** | 72.8 |  164.1 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **71.7** | 89.5 |  251.5 |
| Throughput median (tok/s) |     **13.9** | 11.2 |    4.0 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        192.1 |      89.5 | **87.0** |
| TPOT median (ms)          |     **35.4** |      41.3 |     78.6 |
| E2E median (ms)           |        220.6 | **117.8** |    149.9 |
| Throughput median (tok/s) |          5.1 |  **11.0** |      8.9 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.9 | **36.5** |   60.5 |
| TPOT median (ms)          |         35.1 | **26.5** |  406.9 |
| E2E median (ms)           |         74.0 | **54.3** |  469.5 |
| Throughput median (tok/s) |         19.4 | **23.4** |    3.1 |
| Correctness               |          96% |      97% |    98% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.5 |  **46.1** |   53.8 |
| TPOT median (ms)          |         18.8 |  **15.4** |   27.5 |
| E2E median (ms)           |        857.9 | **578.6** | 1034.6 |
| Throughput median (tok/s) |         41.8 |  **60.9** |   35.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.6 |  **63.3** |   89.5 |
| TPOT median (ms)          |         24.2 |  **24.1** |  116.1 |
| E2E median (ms)           |        278.0 | **187.4** |  408.9 |
| Throughput median (tok/s) |         17.5 |  **24.0** |   12.2 |
| Correctness               |          98% |       98% |    99% |
