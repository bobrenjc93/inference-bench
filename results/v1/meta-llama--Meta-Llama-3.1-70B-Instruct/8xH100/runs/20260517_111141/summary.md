# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:09 AM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     308.5s (5.1m) | `1cdab3f` |
| vllm         |   1057.6s (17.6m) | `0fa8884` |
| sglang       | **167.7s (2.8m)** | `be3c425` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        279.2 |    162.0 | **136.9** |
| TPOT median (ms)          |        148.4 | **58.1** |      79.7 |
| E2E median (ms)           |        363.8 |    218.4 | **212.2** |
| Throughput median (tok/s) |          4.0 |  **6.7** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        253.0 | **191.1** |  209.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        301.0 | **214.5** |  348.4 |
| Throughput median (tok/s) |          3.3 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        525.1 |     169.4 | **159.5** |
| TPOT median (ms)          |        183.2 |  **61.5** |     105.9 |
| E2E median (ms)           |        639.9 | **224.1** |     262.2 |
| Throughput median (tok/s) |          2.1 |   **6.3** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        350.0 | **58.0** |   76.9 |
| TPOT median (ms)          |        127.5 | **26.5** |   64.3 |
| E2E median (ms)           |        440.4 | **78.1** |  154.7 |
| Throughput median (tok/s) |          3.2 | **15.9** |    9.5 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        632.8 |  **67.6** |   68.0 |
| TPOT median (ms)          |         15.9 |  **15.1** |   22.4 |
| E2E median (ms)           |       1248.2 | **614.0** |  821.3 |
| Throughput median (tok/s) |         27.6 |  **59.0** |   42.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        408.0 | **129.6** |  130.1 |
| TPOT median (ms)          |         95.0 |  **32.3** |   54.5 |
| E2E median (ms)           |        598.7 | **269.8** |  359.7 |
| Throughput median (tok/s) |          8.0 |  **18.5** |   13.1 |
| Correctness               |          99% |       99% |    98% |
