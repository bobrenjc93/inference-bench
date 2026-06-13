# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     332.2s (5.5m) | `065275c` |
| vllm         |   1368.0s (22.8m) | `1033ffa` |
| sglang       | **214.8s (3.6m)** | `cb4933b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        287.0 |     158.6 | **142.3** |
| TPOT median (ms)          |         81.5 |  **51.5** |      76.5 |
| E2E median (ms)           |        362.8 | **202.4** |     213.5 |
| Throughput median (tok/s) |          3.8 |   **7.2** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        402.9 | **186.4** |  227.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        571.7 | **242.9** |  381.2 |
| Throughput median (tok/s) |          1.7 |   **4.1** |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        720.1 |     175.9 | **168.0** |
| TPOT median (ms)          |     **60.9** |      61.4 |     104.8 |
| E2E median (ms)           |        777.5 | **236.9** |     268.0 |
| Throughput median (tok/s) |          1.8 |   **6.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        442.8 | **60.7** |   78.9 |
| TPOT median (ms)          |         65.5 | **28.1** |   58.2 |
| E2E median (ms)           |        524.7 | **82.9** |  154.4 |
| Throughput median (tok/s) |          2.9 | **14.5** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.5 |  **65.1** |   72.8 |
| TPOT median (ms)          |         25.8 |  **15.2** |   22.6 |
| E2E median (ms)           |       1226.5 | **608.9** |  842.9 |
| Throughput median (tok/s) |         31.1 |  **58.8** |   41.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        408.7 | **129.3** |  137.8 |
| TPOT median (ms)          |         46.7 |  **31.2** |   52.4 |
| E2E median (ms)           |        692.6 | **274.8** |  372.0 |
| Throughput median (tok/s) |          8.3 |  **18.2** |   12.8 |
| Correctness               |          98% |       99% |    99% |
