# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jun 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     377.5s (6.3m) | `377bf47` |
| vllm         |     451.4s (7.5m) | `c621af1` |
| sglang       | **216.0s (3.6m)** | `3cb29f6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        305.7 |     159.3 | **144.2** |
| TPOT median (ms)          |     **50.1** |      58.0 |      81.4 |
| E2E median (ms)           |        355.6 | **211.9** |     222.0 |
| Throughput median (tok/s) |          3.7 |   **7.1** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        335.0 | **189.0** |  203.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        464.4 | **214.6** |  341.7 |
| Throughput median (tok/s) |          2.2 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        615.6 |     180.0 | **160.5** |
| TPOT median (ms)          |     **60.8** |      67.1 |     105.1 |
| E2E median (ms)           |        670.2 | **242.4** |     267.6 |
| Throughput median (tok/s) |          1.9 |   **5.9** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        206.0 | **61.2** |   81.1 |
| TPOT median (ms)          |         31.0 | **28.3** |   48.5 |
| E2E median (ms)           |        239.4 | **82.8** |  147.7 |
| Throughput median (tok/s) |          5.6 | **14.4** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        388.5 |  **69.1** |   70.5 |
| TPOT median (ms)          |         20.8 |  **14.9** |   22.6 |
| E2E median (ms)           |       1199.4 | **595.3** |  839.0 |
| Throughput median (tok/s) |         30.7 |  **59.7** |   41.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        370.2 | **131.7** |  132.0 |
| TPOT median (ms)          |     **32.5** |      33.6 |   51.5 |
| E2E median (ms)           |        585.8 | **269.4** |  363.6 |
| Throughput median (tok/s) |          8.8 |  **18.4** |   12.9 |
| Correctness               |          99% |       99% |    98% |
