# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:51 PM PT, Jun 26 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |       1/4 |    1/4 |      **2/4** |
| self_consistency |   **3/4** |    0/4 |          0/4 |
| multi_turn       |   **3/4** |    0/4 |          1/4 |
| tree_of_thought  |   **4/4** |    0/4 |          0/4 |
| long_output      |   **3/4** |    1/4 |          0/4 |
| **Total**        | **14/20** |   2/20 |         3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** | `9222148` |
| sglang       |     0.0s (0.0m) | `bc15017` |
| torchinferno |     0.0s (0.0m) | `6a62c0c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |    vllm |    sglang | torchinferno |
| :------------------------ | ------: | --------: | -----------: |
| TTFT median (ms)          |   154.9 | **142.6** |        157.1 |
| TPOT median (ms)          |    58.8 |      81.7 |     **51.4** |
| E2E median (ms)           |   208.8 |     219.9 |    **198.9** |
| Throughput median (tok/s) | **6.9** |       5.3 |          5.7 |
| Correctness               |     98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **176.4** |  214.3 |        272.2 |
| TPOT median (ms)          |       0.0 |    0.0 |          0.0 |
| E2E median (ms)           | **309.6** |  400.8 |        309.8 |
| Throughput median (tok/s) |   **3.2** |    2.5 |          3.2 |
| Correctness               |      100% |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **132.8** |  173.1 |        430.8 |
| TPOT median (ms)          |      81.5 |  121.4 |     **65.6** |
| E2E median (ms)           | **217.2** |  290.7 |        500.5 |
| Throughput median (tok/s) |   **6.0** |    4.4 |          2.3 |
| Correctness               |       98% |    98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **72.0** |   78.8 |        342.5 |
| TPOT median (ms)          | **35.6** |   65.5 |         55.7 |
| E2E median (ms)           | **99.9** |  156.1 |        371.6 |
| Throughput median (tok/s) | **12.3** |    8.7 |          4.0 |
| Correctness               |      97% |    97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      84.3 | **82.5** |        337.7 |
| TPOT median (ms)          |  **18.8** |     26.8 |         28.2 |
| E2E median (ms)           | **786.5** |    984.4 |       1457.3 |
| Throughput median (tok/s) |  **47.2** |     34.6 |         25.9 |
| Correctness               |      100% |     100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **124.1** |  138.2 |        308.1 |
| TPOT median (ms)          |  **39.0** |   59.1 |         40.2 |
| E2E median (ms)           | **324.4** |  410.4 |        567.6 |
| Throughput median (tok/s) |  **15.1** |   11.1 |          8.2 |
| Correctness               |       98% |    98% |          99% |
