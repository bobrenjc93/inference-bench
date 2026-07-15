# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 AM PT, Jul 15 2026

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
| torchinferno | **46.7s (0.8m)** | `96adc9d` |
| vllm         |    376.9s (6.3m) | `1b30ae4` |
| sglang       |    177.0s (3.0m) | `947a14d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        139.8 |  **73.8** |   81.2 |
| TPOT median (ms)          |     **32.5** |      38.2 |   66.5 |
| E2E median (ms)           |        164.5 | **104.5** |  137.6 |
| Throughput median (tok/s) |          7.1 |  **13.0** |    9.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **59.7** | 72.6 |  119.2 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **77.4** | 91.0 |  199.1 |
| Throughput median (tok/s) |     **12.9** | 11.0 |    5.0 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        190.1 | **68.6** |   83.2 |
| TPOT median (ms)          |         35.5 | **35.0** |   67.8 |
| E2E median (ms)           |        218.2 | **92.7** |  140.4 |
| Throughput median (tok/s) |          5.2 | **13.9** |    9.4 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.8 | **39.0** |   52.4 |
| TPOT median (ms)          |         34.8 | **29.4** |  423.6 |
| E2E median (ms)           |         74.2 | **59.9** |  427.1 |
| Throughput median (tok/s) |         19.6 | **22.1** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        182.6 |  **47.4** |   51.6 |
| TPOT median (ms)          |         19.0 |  **15.5** |   25.1 |
| E2E median (ms)           |        840.4 | **581.2** |  949.8 |
| Throughput median (tok/s) |         40.9 |  **59.6** |   38.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.0 |  **60.3** |   77.5 |
| TPOT median (ms)          |         24.4 |  **23.6** |  116.6 |
| E2E median (ms)           |        275.0 | **185.9** |  370.8 |
| Throughput median (tok/s) |         17.1 |  **23.9** |   13.1 |
| Correctness               |          99% |       99% |    99% |
