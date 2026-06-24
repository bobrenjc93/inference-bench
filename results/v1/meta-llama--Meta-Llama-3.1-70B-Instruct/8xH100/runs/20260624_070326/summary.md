# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:44 PM PT, Jun 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **3.9s (0.1m)** | `6e2cc27` |
| vllm         |    86.0s (1.4m) | `0bc479e` |
| sglang       |     8.9s (0.1m) | `09b808a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        166.6 |   166.4 | **146.8** |
| TPOT median (ms)          |     **51.9** |    57.1 |      76.6 |
| E2E median (ms)           |    **212.6** |   219.4 |     223.3 |
| Throughput median (tok/s) |          5.6 | **6.3** |       5.5 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        358.0 | **182.9** |  242.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        391.1 | **308.5** |  412.3 |
| Throughput median (tok/s) |          2.6 |   **3.2** |    2.4 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        429.1 | **180.2** |  188.8 |
| TPOT median (ms)          |     **64.9** |      65.7 |  116.1 |
| E2E median (ms)           |        496.1 | **242.1** |  313.6 |
| Throughput median (tok/s) |          2.4 |   **5.6** |    4.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        319.6 |  **74.1** |   77.5 |
| TPOT median (ms)          |         51.2 |  **35.5** |   72.6 |
| E2E median (ms)           |        377.1 | **102.4** |  159.7 |
| Throughput median (tok/s) |          4.0 |  **11.7** |    8.9 |
| Correctness               |          97% |       97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        345.6 |  **73.1** |   80.6 |
| TPOT median (ms)          |         27.1 |  **18.9** |   27.3 |
| E2E median (ms)           |       1453.9 | **761.2** | 1008.3 |
| Throughput median (tok/s) |         27.8 |  **48.2** |   34.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        323.8 | **135.3** |  147.3 |
| TPOT median (ms)          |         39.0 |  **35.4** |   58.5 |
| E2E median (ms)           |        586.2 | **326.7** |  423.4 |
| Throughput median (tok/s) |          8.5 |  **15.0** |   11.1 |
| Correctness               |          98% |       98% |    99% |
