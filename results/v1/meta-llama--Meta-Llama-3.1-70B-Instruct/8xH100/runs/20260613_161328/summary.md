# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jun 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     361.8s (6.0m) | `b648e00` |
| vllm         |   1372.2s (22.9m) | `470229c` |
| sglang       | **217.0s (3.6m)** | `29128f3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        308.4 |    161.5 | **141.5** |
| TPOT median (ms)          |        100.6 | **63.4** |      75.6 |
| E2E median (ms)           |        392.1 |    212.0 | **210.0** |
| Throughput median (tok/s) |          3.2 |  **7.0** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        322.4 | **204.3** |  215.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        446.2 | **229.1** |  355.5 |
| Throughput median (tok/s) |          2.2 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        743.6 | **161.4** |  165.9 |
| TPOT median (ms)          |         65.6 |  **51.0** |  101.4 |
| E2E median (ms)           |        855.2 | **206.6** |  262.7 |
| Throughput median (tok/s) |          1.6 |   **6.4** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        329.2 | **58.7** |   85.3 |
| TPOT median (ms)          |         65.7 | **28.2** |   43.7 |
| E2E median (ms)           |        385.6 | **80.3** |  143.4 |
| Throughput median (tok/s) |          3.6 | **15.3** |    9.5 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        296.2 |      74.9 | **70.1** |
| TPOT median (ms)          |         22.4 |  **14.9** |     22.2 |
| E2E median (ms)           |       1124.0 | **611.1** |    825.0 |
| Throughput median (tok/s) |         32.3 |  **59.0** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        399.9 | **132.2** |  135.7 |
| TPOT median (ms)          |         50.9 |  **31.5** |   48.6 |
| E2E median (ms)           |        640.6 | **267.8** |  359.3 |
| Throughput median (tok/s) |          8.6 |  **18.4** |   13.1 |
| Correctness               |          98% |       99% |    98% |
