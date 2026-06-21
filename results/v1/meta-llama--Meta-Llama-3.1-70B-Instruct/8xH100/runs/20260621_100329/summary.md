# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 21 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          2/4 |       2/4 |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     354.1s (5.9m) | `a7e5516` |
| vllm         |     502.2s (8.4m) | `b80ce9d` |
| sglang       | **247.0s (4.1m)** | `9691a29` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        139.1 | **137.4** |  155.6 |
| TPOT median (ms)          |     **45.7** |      51.3 |   72.5 |
| E2E median (ms)           |    **183.3** |     183.9 |  224.0 |
| Throughput median (tok/s) |          6.6 |   **7.8** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        296.4 | **172.2** |  215.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        410.7 | **194.6** |  354.7 |
| Throughput median (tok/s) |          2.4 |   **5.1** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        585.4 | **160.4** |  163.7 |
| TPOT median (ms)          |     **36.7** |      56.6 |  102.2 |
| E2E median (ms)           |        616.1 | **205.2** |  263.7 |
| Throughput median (tok/s) |          2.3 |   **6.6** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        195.5 | **57.1** |   82.5 |
| TPOT median (ms)          |         28.8 | **28.8** |   43.3 |
| E2E median (ms)           |        226.2 | **78.7** |  140.9 |
| Throughput median (tok/s) |          6.0 | **15.6** |    9.5 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        367.8 |      71.4 | **68.6** |
| TPOT median (ms)          |         21.1 |  **15.2** |     22.5 |
| E2E median (ms)           |       1212.4 | **622.7** |    822.4 |
| Throughput median (tok/s) |         30.7 |  **57.9** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        316.9 | **119.7** |  137.1 |
| TPOT median (ms)          |     **26.5** |      30.4 |   48.1 |
| E2E median (ms)           |        529.8 | **257.0** |  361.1 |
| Throughput median (tok/s) |          9.6 |  **18.6** |   13.0 |
| Correctness               |          98% |       98% |    98% |
