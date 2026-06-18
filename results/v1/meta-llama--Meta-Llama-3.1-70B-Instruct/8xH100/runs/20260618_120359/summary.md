# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 AM PT, Jun 18 2026

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
| torchinferno |     435.8s (7.3m) | `ccca738` |
| vllm         |     528.7s (8.8m) | `351c72d` |
| sglang       | **262.3s (4.4m)** | `bb9d31f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        431.4 |     147.1 | **144.2** |
| TPOT median (ms)          |         62.7 |  **53.5** |      70.1 |
| E2E median (ms)           |        487.7 | **194.1** |     213.6 |
| Throughput median (tok/s) |          2.9 |   **7.3** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        297.8 | **182.5** |  229.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        414.9 | **204.1** |  363.7 |
| Throughput median (tok/s) |          2.4 |   **4.9** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        633.8 | **161.6** |  163.6 |
| TPOT median (ms)          |         60.7 |  **55.5** |  105.8 |
| E2E median (ms)           |        716.4 | **209.5** |  262.2 |
| Throughput median (tok/s) |          1.8 |   **6.8** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        226.5 | **56.7** |   87.3 |
| TPOT median (ms)          |         35.4 | **29.5** |   43.5 |
| E2E median (ms)           |        262.7 | **79.2** |  147.5 |
| Throughput median (tok/s) |          5.2 | **15.1** |    9.4 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        362.2 |  **64.8** |   69.4 |
| TPOT median (ms)          |         21.9 |  **15.0** |   22.2 |
| E2E median (ms)           |       1172.2 | **610.0** |  821.5 |
| Throughput median (tok/s) |         30.9 |  **59.3** |   42.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        390.3 | **122.5** |  138.8 |
| TPOT median (ms)          |         36.1 |  **30.7** |   48.3 |
| E2E median (ms)           |        610.8 | **259.4** |  361.7 |
| Throughput median (tok/s) |          8.6 |  **18.7** |   13.0 |
| Correctness               |          98% |       99% |    99% |
