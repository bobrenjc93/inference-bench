# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jun 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **3/4** |     1/4 |
| **Total**        |         1/20 | **14/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     358.9s (6.0m) | `377bf47` |
| vllm         |     458.1s (7.6m) | `c621af1` |
| sglang       | **196.1s (3.3m)** | `f18d38d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        371.8 |   161.9 | **145.1** |
| TPOT median (ms)          |     **51.2** |    61.2 |      81.3 |
| E2E median (ms)           |        422.6 |   220.4 | **218.6** |
| Throughput median (tok/s) |          3.3 | **6.9** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        276.9 | **179.7** |  209.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        391.2 | **227.3** |  347.1 |
| Throughput median (tok/s) |          2.6 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        712.0 |     170.5 | **160.2** |
| TPOT median (ms)          |         63.5 |  **56.4** |     105.7 |
| E2E median (ms)           |        769.5 | **215.0** |     266.1 |
| Throughput median (tok/s) |          1.8 |   **6.5** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        196.9 | **59.6** |   84.2 |
| TPOT median (ms)          |         30.0 | **28.0** |   56.9 |
| E2E median (ms)           |        226.5 | **81.5** |  147.8 |
| Throughput median (tok/s) |          5.6 | **14.7** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        355.2 |      68.2 | **67.0** |
| TPOT median (ms)          |         20.2 |  **14.9** |     22.2 |
| E2E median (ms)           |       1171.3 | **608.2** |    815.3 |
| Throughput median (tok/s) |         32.9 |  **59.7** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        382.6 | **128.0** |  133.2 |
| TPOT median (ms)          |         33.0 |  **32.1** |   53.2 |
| E2E median (ms)           |        596.2 | **270.5** |  359.0 |
| Throughput median (tok/s) |          9.3 |  **18.4** |   13.1 |
| Correctness               |          99% |       99% |    99% |
