# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:28 AM PT, Jun 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         3/20 | **14/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **3.9s (0.1m)** | `a180fbb` |
| vllm         |    86.2s (1.4m) | `1cd3e0e` |
| sglang       |     9.0s (0.1m) | `4a4f063` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        165.3 |   160.1 | **143.0** |
| TPOT median (ms)          |     **52.3** |    61.5 |      81.4 |
| E2E median (ms)           |    **215.0** |   219.6 |     219.3 |
| Throughput median (tok/s) |          5.6 | **6.6** |       5.4 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        221.1 | **169.0** |  223.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        368.8 | **300.4** |  419.1 |
| Throughput median (tok/s) |          2.7 |   **3.3** |    2.4 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        427.6 |     182.6 | **180.4** |
| TPOT median (ms)          |     **68.6** |      70.7 |     110.9 |
| E2E median (ms)           |        502.4 | **242.5** |     299.4 |
| Throughput median (tok/s) |          2.3 |   **5.7** |       4.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        288.7 |  **72.7** |   76.7 |
| TPOT median (ms)          |         51.4 |  **35.6** |   62.3 |
| E2E median (ms)           |        323.5 | **100.4** |  149.6 |
| Throughput median (tok/s) |          4.3 |  **12.0** |    8.9 |
| Correctness               |          97% |       97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        405.0 |  **88.1** |   89.6 |
| TPOT median (ms)          |         24.8 |  **18.9** |   26.2 |
| E2E median (ms)           |       1440.7 | **772.6** | 1025.6 |
| Throughput median (tok/s) |         25.8 |  **47.1** |   34.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        301.5 | **134.5** |  142.5 |
| TPOT median (ms)          |         39.4 |  **37.3** |   56.2 |
| E2E median (ms)           |        570.1 | **327.1** |  422.6 |
| Throughput median (tok/s) |          8.2 |  **14.9** |   11.1 |
| Correctness               |          98% |       99% |    99% |
