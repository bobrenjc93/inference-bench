# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:29 PM PT, Jul 1 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |       1/4 | **2/4** |          1/4 |
| self_consistency |       1/4 |     0/4 |      **2/4** |
| multi_turn       |   **3/4** |     1/4 |          0/4 |
| tree_of_thought  |   **3/4** |     1/4 |          0/4 |
| long_output      |   **3/4** |     1/4 |          0/4 |
| **Total**        | **11/20** |    5/20 |         3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** | `c621af1` |
| sglang       |     0.0s (0.0m) | `99b8f36` |
| torchinferno |     0.0s (0.0m) | `840f859` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |    vllm |    sglang | torchinferno |
| :------------------------ | ------: | --------: | -----------: |
| TTFT median (ms)          |   156.1 | **120.0** |        172.0 |
| TPOT median (ms)          |    53.8 |      72.6 |     **48.6** |
| E2E median (ms)           |   206.7 | **195.3** |        213.3 |
| Throughput median (tok/s) | **7.5** |       6.4 |          5.5 |
| Correctness               |     98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **168.9** |  205.3 |        211.2 |
| TPOT median (ms)          |       0.0 |    0.0 |          0.0 |
| E2E median (ms)           |     263.5 |  370.5 |    **229.0** |
| Throughput median (tok/s) |       3.8 |    2.7 |      **4.4** |
| Correctness               |      100% |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     183.9 | **152.1** |        326.6 |
| TPOT median (ms)          |  **59.9** |     114.1 |         61.3 |
| E2E median (ms)           | **236.4** |     271.1 |        381.2 |
| Throughput median (tok/s) |   **5.9** |       4.8 |          3.4 |
| Correctness               |       98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     66.5 | **60.9** |        161.4 |
| TPOT median (ms)          | **31.4** |     71.9 |         46.7 |
| E2E median (ms)           | **89.6** |    143.4 |        190.7 |
| Throughput median (tok/s) | **13.5** |      9.9 |          6.6 |
| Correctness               |      96% |      97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      64.4 | **62.5** |        257.2 |
| TPOT median (ms)          |  **16.9** |     24.2 |         24.5 |
| E2E median (ms)           | **674.0** |    914.3 |       1254.0 |
| Throughput median (tok/s) |  **54.0** |     38.4 |         31.7 |
| Correctness               |      100% |     100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     127.9 | **120.2** |        225.7 |
| TPOT median (ms)          |  **32.4** |      56.6 |         36.2 |
| E2E median (ms)           | **294.1** |     378.9 |        453.6 |
| Throughput median (tok/s) |  **16.9** |      12.4 |         10.3 |
| Correctness               |       98% |       98% |          99% |
