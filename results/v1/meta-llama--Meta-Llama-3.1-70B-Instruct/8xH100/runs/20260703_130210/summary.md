# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         6/20 | **10/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **40.1s (0.7m)** | `4be1a2f` |
| vllm         |    230.2s (3.8m) | `978de83` |
| sglang       |    160.1s (2.7m) | `1058d00` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        148.8 |   144.7 | **141.1** |
| TPOT median (ms)          |     **46.8** |    51.4 |      77.2 |
| E2E median (ms)           |    **189.1** |   191.7 |     217.4 |
| Throughput median (tok/s) |          6.5 | **7.6** |       5.5 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **154.5** | 204.4 |  215.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **162.3** | 229.7 |  367.5 |
| Throughput median (tok/s) |      **6.2** |   4.4 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        312.1 |     177.5 | **163.0** |
| TPOT median (ms)          |         60.7 |  **55.1** |     103.5 |
| E2E median (ms)           |        365.5 | **226.9** |     270.0 |
| Throughput median (tok/s) |          4.0 |   **6.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        127.9 | **62.1** |   73.3 |
| TPOT median (ms)          |     **27.0** |     29.9 |   57.2 |
| E2E median (ms)           |        148.4 | **84.1** |  138.7 |
| Throughput median (tok/s) |          9.0 | **14.1** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        265.6 |      81.5 | **71.0** |
| TPOT median (ms)          |         20.7 |  **15.1** |     22.3 |
| E2E median (ms)           |        953.3 | **612.8** |    856.8 |
| Throughput median (tok/s) |         36.5 |  **57.1** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        201.8 |     134.0 | **132.7** |
| TPOT median (ms)          |         31.1 |  **30.3** |      52.0 |
| E2E median (ms)           |        363.7 | **269.0** |     370.1 |
| Throughput median (tok/s) |         12.4 |  **17.8** |      13.1 |
| Correctness               |          99% |       99% |       99% |
