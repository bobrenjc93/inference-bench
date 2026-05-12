# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:07 AM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     418.8s (7.0m) | `49a8f38` |
| vllm         |    993.9s (16.6m) | `07a40ed` |
| sglang       | **176.7s (2.9m)** | `693f497` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        448.9 |    160.4 | **137.6** |
| TPOT median (ms)          |        365.9 | **60.7** |      75.8 |
| E2E median (ms)           |        780.6 |    220.8 | **208.0** |
| Throughput median (tok/s) |          1.7 |  **6.8** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        385.5 | **195.6** |  209.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        438.6 | **217.2** |  358.9 |
| Throughput median (tok/s) |          2.3 |   **4.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        643.1 |     180.3 | **158.5** |
| TPOT median (ms)          |        532.5 |  **62.4** |     107.4 |
| E2E median (ms)           |       1187.3 | **230.3** |     259.7 |
| Throughput median (tok/s) |          1.1 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        449.6 | **57.9** |   76.9 |
| TPOT median (ms)          |        479.1 | **26.6** |   63.2 |
| E2E median (ms)           |        878.3 | **78.7** |  156.7 |
| Throughput median (tok/s) |          1.7 | **15.6** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        718.7 |      70.7 | **68.5** |
| TPOT median (ms)          |         26.6 |  **14.9** |     22.3 |
| E2E median (ms)           |       1913.8 | **607.1** |    835.5 |
| Throughput median (tok/s) |         17.9 |  **59.0** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        529.2 |     133.0 | **130.1** |
| TPOT median (ms)          |        280.8 |  **32.9** |      53.7 |
| E2E median (ms)           |       1039.7 | **270.8** |     363.8 |
| Throughput median (tok/s) |          4.9 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       99% |
