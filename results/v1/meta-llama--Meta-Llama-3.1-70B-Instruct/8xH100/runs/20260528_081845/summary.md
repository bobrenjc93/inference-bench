# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:01 AM PT, May 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     356.2s (5.9m) | `f4c65f7` |
| vllm         |   1416.7s (23.6m) | `6cc8577` |
| sglang       | **242.0s (4.0m)** | `00cd6fb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        268.1 |     161.4 | **152.4** |
| TPOT median (ms)          |         62.3 |  **58.6** |      71.8 |
| E2E median (ms)           |        335.2 | **220.7** |     221.5 |
| Throughput median (tok/s) |          4.3 |   **6.8** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        290.8 |     206.5 | **200.8** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        328.8 | **227.1** |     333.0 |
| Throughput median (tok/s) |          3.0 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        744.3 |     177.8 | **169.8** |
| TPOT median (ms)          |     **55.4** |      61.8 |     103.4 |
| E2E median (ms)           |        798.6 | **234.5** |     273.0 |
| Throughput median (tok/s) |          1.6 |   **6.0** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        197.7 | **58.5** |   82.7 |
| TPOT median (ms)          |         27.3 | **27.0** |   40.5 |
| E2E median (ms)           |        227.7 | **79.2** |  134.1 |
| Throughput median (tok/s) |          6.4 | **15.6** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        586.6 |  **71.0** |   77.8 |
| TPOT median (ms)          |     **14.4** |      15.0 |   23.6 |
| E2E median (ms)           |       1182.0 | **624.2** |  862.2 |
| Throughput median (tok/s) |         28.1 |  **58.8** |   39.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        417.5 | **135.1** |  136.7 |
| TPOT median (ms)          |     **31.9** |      32.5 |   47.8 |
| E2E median (ms)           |        574.5 | **277.1** |  364.8 |
| Throughput median (tok/s) |          8.7 |  **18.3** |   12.5 |
| Correctness               |          98% |       99% |    99% |
