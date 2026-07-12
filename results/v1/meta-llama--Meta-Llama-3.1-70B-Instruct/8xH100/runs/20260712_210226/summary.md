# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jul 12 2026

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
| torchinferno | **37.3s (0.6m)** | `96adc9d` |
| vllm         |    336.6s (5.6m) | `4c81772` |
| sglang       |    149.2s (2.5m) | `24d59d8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        140.3 |      80.3 | **79.5** |
| TPOT median (ms)          |     **32.4** |      41.5 |     63.2 |
| E2E median (ms)           |        165.8 | **114.6** |    133.4 |
| Throughput median (tok/s) |          7.0 |  **11.7** |     10.1 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.1** | 68.1 |  120.3 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **74.6** | 87.0 |  199.2 |
| Throughput median (tok/s) |     **13.4** | 11.5 |    5.0 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        188.1 | **73.1** |   81.7 |
| TPOT median (ms)          |     **35.7** |     36.1 |   75.4 |
| E2E median (ms)           |        218.3 | **98.0** |  141.4 |
| Throughput median (tok/s) |          5.1 | **13.2** |    9.5 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.1 | **37.0** |   52.2 |
| TPOT median (ms)          |         34.6 | **27.0** |  392.9 |
| E2E median (ms)           |         72.2 | **56.2** |  468.3 |
| Throughput median (tok/s) |         19.7 | **23.5** |    3.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        183.7 |  **46.1** |   51.6 |
| TPOT median (ms)          |         19.3 |  **15.4** |   24.1 |
| E2E median (ms)           |        869.3 | **575.5** |  930.9 |
| Throughput median (tok/s) |         40.9 |  **60.4** |   40.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.3 |  **60.9** |   77.1 |
| TPOT median (ms)          |         24.4 |  **24.0** |  111.1 |
| E2E median (ms)           |        280.0 | **186.3** |  374.6 |
| Throughput median (tok/s) |         17.2 |  **24.1** |   13.6 |
| Correctness               |          99% |       99% |    99% |
