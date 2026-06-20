# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jun 20 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     325.3s (5.4m) | `3550159` |
| vllm         |     496.7s (8.3m) | `6e91996` |
| sglang       | **259.1s (4.3m)** | `f42ec35` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        166.3 | **132.5** |  148.0 |
| TPOT median (ms)          |     **43.7** |      45.7 |   77.5 |
| E2E median (ms)           |        201.6 | **173.9** |  214.4 |
| Throughput median (tok/s) |          6.1 |   **8.1** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        319.0 |     229.3 | **216.2** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        437.8 | **257.4** |     366.4 |
| Throughput median (tok/s) |          2.3 |   **3.9** |       2.7 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        552.7 | **158.5** |  159.5 |
| TPOT median (ms)          |     **36.0** |      49.3 |   94.8 |
| E2E median (ms)           |        581.2 | **199.9** |  257.8 |
| Throughput median (tok/s) |          2.2 |   **6.9** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        201.7 | **59.2** |   82.9 |
| TPOT median (ms)          |         31.6 | **29.1** |   50.2 |
| E2E median (ms)           |        230.6 | **81.3** |  143.8 |
| Throughput median (tok/s) |          5.6 | **14.9** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        350.1 |      73.9 | **71.5** |
| TPOT median (ms)          |         21.1 |  **15.0** |     22.1 |
| E2E median (ms)           |       1189.9 | **619.6** |    832.0 |
| Throughput median (tok/s) |         31.4 |  **58.7** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        318.0 | **130.7** |  135.6 |
| TPOT median (ms)          |     **26.5** |      27.8 |   48.9 |
| E2E median (ms)           |        528.2 | **266.4** |  362.9 |
| Throughput median (tok/s) |          9.5 |  **18.5** |   13.1 |
| Correctness               |          99% |       99% |    99% |
