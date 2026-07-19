# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jul 19 2026

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
| torchinferno | **41.4s (0.7m)** | `96adc9d` |
| vllm         |    344.4s (5.7m) | `e6d1310` |
| sglang       |    182.0s (3.0m) | `d4801be` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        140.0 |  **73.6** |   99.0 |
| TPOT median (ms)          |     **32.7** |      38.0 |   73.6 |
| E2E median (ms)           |        165.5 | **103.7** |  164.2 |
| Throughput median (tok/s) |          7.1 |  **12.7** |    7.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **59.7** | 76.7 |  166.1 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **76.6** | 94.3 |  237.9 |
| Throughput median (tok/s) |     **13.0** | 10.6 |    4.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        190.2 |      98.1 | **91.9** |
| TPOT median (ms)          |     **35.9** |      37.6 |     78.4 |
| E2E median (ms)           |        219.7 | **127.1** |    154.4 |
| Throughput median (tok/s) |          5.2 |  **10.9** |      8.6 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.9 | **35.3** |   69.3 |
| TPOT median (ms)          |         34.7 | **22.9** |  455.7 |
| E2E median (ms)           |         74.7 | **53.6** |  526.1 |
| Throughput median (tok/s) |         19.3 | **24.6** |    2.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        195.6 |  **46.8** |   59.7 |
| TPOT median (ms)          |         19.6 |  **15.5** |   27.5 |
| E2E median (ms)           |        891.1 | **576.5** | 1045.5 |
| Throughput median (tok/s) |         40.4 |  **60.8** |   35.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.7 |  **66.1** |   97.2 |
| TPOT median (ms)          |         24.6 |  **22.8** |  127.0 |
| E2E median (ms)           |        285.5 | **191.0** |  425.6 |
| Throughput median (tok/s) |         17.0 |  **23.9** |   11.7 |
| Correctness               |          99% |       99% |    98% |
