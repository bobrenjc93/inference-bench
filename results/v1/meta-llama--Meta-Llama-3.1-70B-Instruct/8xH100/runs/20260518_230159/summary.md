# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:02 PM PT, May 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     272.4s (4.5m) | `c837893` |
| vllm         |   1109.2s (18.5m) | `57fef4e` |
| sglang       | **179.6s (3.0m)** | `6f89204` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        284.0 |     161.1 | **143.4** |
| TPOT median (ms)          |        152.6 |  **54.8** |      75.8 |
| E2E median (ms)           |        371.1 | **211.0** |     214.2 |
| Throughput median (tok/s) |          4.0 |   **6.9** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        272.2 |     208.0 | **202.4** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        300.2 | **234.8** |     338.5 |
| Throughput median (tok/s) |          3.3 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        533.4 |     170.5 | **157.6** |
| TPOT median (ms)          |        104.2 |  **55.8** |     106.3 |
| E2E median (ms)           |        641.5 | **226.8** |     255.3 |
| Throughput median (tok/s) |          2.0 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        348.5 | **57.7** |   74.6 |
| TPOT median (ms)          |        130.3 | **26.8** |   62.4 |
| E2E median (ms)           |        446.8 | **78.0** |  147.2 |
| Throughput median (tok/s) |          2.9 | **15.7** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        741.4 |      69.7 | **66.5** |
| TPOT median (ms)          |         16.2 |  **15.0** |     22.1 |
| E2E median (ms)           |       1381.1 | **614.7** |    835.8 |
| Throughput median (tok/s) |         23.9 |  **59.3** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        435.9 |     133.4 | **128.9** |
| TPOT median (ms)          |         80.7 |  **30.5** |      53.3 |
| E2E median (ms)           |        628.2 | **273.1** |     358.2 |
| Throughput median (tok/s) |          7.2 |  **18.4** |      13.2 |
| Correctness               |          99% |       99% |       99% |
