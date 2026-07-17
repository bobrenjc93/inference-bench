# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 16 2026

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
| torchinferno | **43.9s (0.7m)** | `96adc9d` |
| vllm         |    307.9s (5.1m) | `3b6c96a` |
| sglang       |    170.0s (2.8m) | `444bbd8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        139.7 |  **79.3** |   79.9 |
| TPOT median (ms)          |     **32.3** |      40.9 |   68.6 |
| E2E median (ms)           |        165.0 | **111.0** |  135.6 |
| Throughput median (tok/s) |          7.1 |  **12.0** |    9.9 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **54.3** | 71.0 |  127.1 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **71.5** | 87.8 |  209.1 |
| Throughput median (tok/s) |     **14.0** | 11.4 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        191.6 |      86.1 | **83.0** |
| TPOT median (ms)          |     **35.1** |      47.7 |     77.9 |
| E2E median (ms)           |        219.9 | **118.6** |    143.2 |
| Throughput median (tok/s) |          5.1 |  **10.8** |      9.3 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.7 | **37.8** |   53.3 |
| TPOT median (ms)          |         34.9 | **27.3** |  340.8 |
| E2E median (ms)           |         73.5 | **56.2** |  429.9 |
| Throughput median (tok/s) |         19.4 | **22.4** |    3.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        183.3 |  **48.4** |   53.4 |
| TPOT median (ms)          |         19.1 |  **15.4** |   25.0 |
| E2E median (ms)           |        875.4 | **584.1** |  948.3 |
| Throughput median (tok/s) |         40.8 |  **60.3** |   38.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.3 |  **64.5** |   79.3 |
| TPOT median (ms)          |     **24.3** |      26.3 |  102.4 |
| E2E median (ms)           |        281.1 | **191.5** |  373.2 |
| Throughput median (tok/s) |         17.3 |  **23.4** |   13.2 |
| Correctness               |          99% |       99% |    98% |
