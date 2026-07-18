# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jul 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **14/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.6s (0.7m)** | `96adc9d` |
| vllm         |    325.8s (5.4m) | `7c2acd3` |
| sglang       |    174.6s (2.9m) | `10908a6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.3 | **68.8** |   93.6 |
| TPOT median (ms)          |     **31.6** |     37.9 |   75.2 |
| E2E median (ms)           |        165.9 | **96.6** |  155.2 |
| Throughput median (tok/s) |          7.0 | **13.8** |    8.6 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.0** | 72.5 |  172.2 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **75.9** | 89.3 |  233.3 |
| Throughput median (tok/s) |     **13.2** | 11.2 |    4.3 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        192.6 |  **86.7** |   97.5 |
| TPOT median (ms)          |     **35.0** |      36.4 |   85.1 |
| E2E median (ms)           |        221.5 | **116.0** |  171.4 |
| Throughput median (tok/s) |          5.1 |  **10.8** |    7.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         51.4 | **37.0** |   68.6 |
| TPOT median (ms)          |         34.6 | **27.1** |  445.0 |
| E2E median (ms)           |         72.2 | **55.1** |  514.5 |
| Throughput median (tok/s) |         20.0 | **22.8** |    2.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        186.6 |  **47.2** |   60.7 |
| TPOT median (ms)          |         19.3 |  **15.6** |   28.8 |
| E2E median (ms)           |        868.6 | **577.7** | 1096.3 |
| Throughput median (tok/s) |         41.1 |  **60.2** |   33.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.8 |  **62.4** |   98.5 |
| TPOT median (ms)          |         24.1 |  **23.4** |  126.8 |
| E2E median (ms)           |        280.8 | **186.9** |  434.1 |
| Throughput median (tok/s) |         17.3 |  **23.8** |   11.4 |
| Correctness               |          99% |       99% |    99% |
