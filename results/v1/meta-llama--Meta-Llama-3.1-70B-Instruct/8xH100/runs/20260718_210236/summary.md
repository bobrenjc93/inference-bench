# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jul 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **44.2s (0.7m)** | `96adc9d` |
| vllm         |    430.0s (7.2m) | `df362b2` |
| sglang       |    186.5s (3.1m) | `99f5a6f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        142.2 |  **86.1** |  102.8 |
| TPOT median (ms)          |     **32.9** |      40.5 |   65.8 |
| E2E median (ms)           |        167.5 | **118.3** |  158.9 |
| Throughput median (tok/s) |          6.9 |  **11.9** |    8.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **56.0** | 76.1 |  158.8 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **72.7** | 94.9 |  240.5 |
| Throughput median (tok/s) |     **13.8** | 10.5 |    4.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.5 |  **79.4** |   97.7 |
| TPOT median (ms)          |         35.9 |  **34.8** |   75.1 |
| E2E median (ms)           |        219.5 | **107.0** |  161.2 |
| Throughput median (tok/s) |          5.1 |  **12.5** |    8.4 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.0 | **37.6** |   62.9 |
| TPOT median (ms)          |         34.7 | **28.2** |  394.3 |
| E2E median (ms)           |         74.8 | **55.8** |  453.5 |
| Throughput median (tok/s) |         19.7 | **22.4** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        192.2 |  **47.4** |   54.5 |
| TPOT median (ms)          |         19.2 |  **15.6** |   27.7 |
| E2E median (ms)           |        851.1 | **582.3** | 1082.9 |
| Throughput median (tok/s) |         41.1 |  **60.3** |   34.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.8 |  **65.3** |   95.3 |
| TPOT median (ms)          |         24.5 |  **23.8** |  112.6 |
| E2E median (ms)           |        277.1 | **191.6** |  419.4 |
| Throughput median (tok/s) |         17.3 |  **23.5** |   11.7 |
| Correctness               |          99% |       99% |    99% |
