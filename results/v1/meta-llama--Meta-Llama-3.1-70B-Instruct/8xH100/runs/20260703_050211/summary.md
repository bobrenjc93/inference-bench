# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.9s (0.7m)** | `1aecb5d` |
| vllm         |    265.9s (4.4m) | `2dfaae7` |
| sglang       |    152.5s (2.5m) | `e878c6e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        151.7 | **135.6** |  144.1 |
| TPOT median (ms)          |         46.0 |  **42.8** |   76.9 |
| E2E median (ms)           |        194.1 | **169.1** |  221.9 |
| Throughput median (tok/s) |          6.4 |   **8.2** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **148.7** | 223.1 |  221.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **157.9** | 246.2 |  373.6 |
| Throughput median (tok/s) |      **6.3** |   4.1 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        309.7 |     174.1 | **162.6** |
| TPOT median (ms)          |         61.0 |  **45.5** |     113.4 |
| E2E median (ms)           |        363.6 | **220.7** |     271.1 |
| Throughput median (tok/s) |          4.0 |   **6.2** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        132.1 | **63.9** |   71.2 |
| TPOT median (ms)          |     **28.3** |     30.5 |   61.3 |
| E2E median (ms)           |        154.0 | **87.0** |  138.6 |
| Throughput median (tok/s) |          8.5 | **13.7** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        270.8 |      84.1 | **73.1** |
| TPOT median (ms)          |         21.2 |  **15.1** |     21.8 |
| E2E median (ms)           |        964.3 | **681.8** |    855.9 |
| Throughput median (tok/s) |         36.2 |  **56.8** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        202.6 |     136.2 | **134.6** |
| TPOT median (ms)          |         31.3 |  **26.8** |      54.7 |
| E2E median (ms)           |        366.8 | **281.0** |     372.2 |
| Throughput median (tok/s) |         12.3 |  **17.8** |      13.1 |
| Correctness               |          99% |       99% |       99% |
