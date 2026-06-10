# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:09 PM PT, Jun 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     381.9s (6.4m) | `c208ddb` |
| vllm         |   1363.0s (22.7m) | `16282a9` |
| sglang       | **221.6s (3.7m)** | `0da18f8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        248.9 |     159.8 | **150.7** |
| TPOT median (ms)          |         99.2 |  **58.1** |      73.0 |
| E2E median (ms)           |        352.7 | **211.0** |     218.7 |
| Throughput median (tok/s) |          3.6 |   **7.0** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        353.6 | **189.5** |  213.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        492.0 | **224.4** |  354.0 |
| Throughput median (tok/s) |          2.0 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        662.8 |     186.3 | **163.2** |
| TPOT median (ms)          |         66.7 |  **52.3** |     107.9 |
| E2E median (ms)           |        741.2 | **231.0** |     259.6 |
| Throughput median (tok/s) |          1.7 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        398.9 | **61.1** |   81.5 |
| TPOT median (ms)          |         63.6 | **27.6** |   50.0 |
| E2E median (ms)           |        449.6 | **83.4** |  146.6 |
| Throughput median (tok/s) |          2.8 | **14.6** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.0 |  **71.1** |   88.1 |
| TPOT median (ms)          |         26.7 |  **14.9** |   23.4 |
| E2E median (ms)           |       1222.2 | **608.1** |  887.2 |
| Throughput median (tok/s) |         29.9 |  **59.1** |   39.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        371.6 | **133.5** |  139.5 |
| TPOT median (ms)          |         51.2 |  **30.6** |   50.9 |
| E2E median (ms)           |        651.6 | **271.6** |  373.2 |
| Throughput median (tok/s) |          8.0 |  **18.3** |   12.5 |
| Correctness               |          99% |       99% |    99% |
