# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:16 AM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **57.1s (1.0m)** | `390fed4` |
| vllm         |    490.1s (8.2m) | `6eac8e0` |
| sglang       |    338.0s (5.6m) | `6dd0cef` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        196.5 | **130.0** |  143.5 |
| TPOT median (ms)          |         48.6 |  **42.7** |   75.8 |
| E2E median (ms)           |        242.7 | **163.6** |  221.0 |
| Throughput median (tok/s) |          5.5 |   **7.9** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        315.0 | **185.2** |  225.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        332.8 | **208.4** |  378.9 |
| Throughput median (tok/s) |          3.0 |   **4.8** |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        359.8 | **143.6** |  166.0 |
| TPOT median (ms)          |     **60.4** |      61.5 |  109.3 |
| E2E median (ms)           |        417.9 | **203.1** |  277.2 |
| Throughput median (tok/s) |          3.4 |   **6.5** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        128.5 | **63.6** |   77.0 |
| TPOT median (ms)          |         37.2 | **31.3** |   61.8 |
| E2E median (ms)           |        153.3 | **87.7** |  148.4 |
| Throughput median (tok/s) |          8.3 | **13.8** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        273.5 |      83.1 | **72.5** |
| TPOT median (ms)          |         20.8 |  **15.0** |     22.7 |
| E2E median (ms)           |       1075.9 | **662.4** |    847.8 |
| Throughput median (tok/s) |         35.6 |  **57.3** |     41.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        254.7 | **121.1** |  136.9 |
| TPOT median (ms)          |         33.4 |  **30.1** |   53.9 |
| E2E median (ms)           |        444.5 | **265.0** |  374.7 |
| Throughput median (tok/s) |         11.2 |  **18.1** |   12.7 |
| Correctness               |          99% |       99% |    99% |
