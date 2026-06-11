# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:04 AM PT, Jun 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     435.7s (7.3m) | `065275c` |
| vllm         |   1345.0s (22.4m) | `6e64c1b` |
| sglang       | **198.9s (3.3m)** | `b8376ae` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        302.4 |     162.3 | **154.3** |
| TPOT median (ms)          |         92.7 |  **61.1** |      71.7 |
| E2E median (ms)           |        394.2 | **215.0** |     225.6 |
| Throughput median (tok/s) |          3.3 |   **7.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        303.9 | **204.6** |  212.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        419.2 | **224.7** |  347.8 |
| Throughput median (tok/s) |          2.4 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        721.5 | **177.2** |  180.9 |
| TPOT median (ms)          |         66.7 |  **60.3** |   97.1 |
| E2E median (ms)           |        782.6 | **231.7** |  284.6 |
| Throughput median (tok/s) |          1.6 |   **6.1** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        402.0 | **60.8** |   83.3 |
| TPOT median (ms)          |         66.4 | **28.9** |   62.4 |
| E2E median (ms)           |        455.8 | **81.9** |  158.8 |
| Throughput median (tok/s) |          3.1 | **14.5** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.5 |  **72.7** |   78.8 |
| TPOT median (ms)          |         26.4 |  **15.1** |   24.7 |
| E2E median (ms)           |       1229.8 | **621.0** |  890.4 |
| Throughput median (tok/s) |         30.5 |  **57.7** |   38.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        383.7 | **135.5** |  141.9 |
| TPOT median (ms)          |         50.4 |  **33.1** |   51.2 |
| E2E median (ms)           |        656.3 | **274.9** |  381.4 |
| Throughput median (tok/s) |          8.2 |  **18.0** |   12.0 |
| Correctness               |          99% |       99% |    99% |
