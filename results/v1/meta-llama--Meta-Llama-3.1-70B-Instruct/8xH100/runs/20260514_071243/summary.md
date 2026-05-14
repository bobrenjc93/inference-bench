# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:16 PM PT, May 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     381.3s (6.4m) | `1824bbb` |
| vllm         |   1019.1s (17.0m) | `fd7d858` |
| sglang       | **162.0s (2.7m)** | `7b128e1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        258.8 |    153.9 | **134.3** |
| TPOT median (ms)          |        168.9 | **53.6** |      75.6 |
| E2E median (ms)           |        397.4 |    205.3 | **204.5** |
| Throughput median (tok/s) |          3.7 |  **7.3** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        267.4 | **188.7** |  199.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        363.9 | **208.5** |  332.3 |
| Throughput median (tok/s) |          2.7 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        700.2 |     168.6 | **157.6** |
| TPOT median (ms)          |        180.6 |  **59.3** |     103.4 |
| E2E median (ms)           |        862.8 | **212.9** |     256.7 |
| Throughput median (tok/s) |          1.6 |   **6.5** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        359.0 | **57.5** |   76.2 |
| TPOT median (ms)          |        255.0 | **27.4** |   63.5 |
| E2E median (ms)           |        576.6 | **78.2** |  150.4 |
| Throughput median (tok/s) |          2.3 | **15.6** |    9.3 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        711.9 |  **65.2** |   65.3 |
| TPOT median (ms)          |         23.8 |  **14.9** |   22.0 |
| E2E median (ms)           |       1746.1 | **600.0** |  808.5 |
| Throughput median (tok/s) |         18.5 |  **59.8** |   43.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        459.4 |     126.8 | **126.4** |
| TPOT median (ms)          |        125.6 |  **31.0** |      52.9 |
| E2E median (ms)           |        789.4 | **261.0** |     350.5 |
| Throughput median (tok/s) |          5.8 |  **18.8** |      13.3 |
| Correctness               |          98% |       98% |       99% |
