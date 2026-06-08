# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jun 7 2026

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
| torchinferno |     315.9s (5.3m) | `ef87e07` |
| vllm         |   1309.1s (21.8m) | `5633405` |
| sglang       | **209.8s (3.5m)** | `bf7fb6b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        298.8 |    168.5 | **146.8** |
| TPOT median (ms)          |         97.9 | **63.0** |      71.9 |
| E2E median (ms)           |        384.5 |    223.2 | **213.5** |
| Throughput median (tok/s) |          3.2 |  **6.5** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        381.5 | **199.9** |  206.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        512.6 | **222.8** |  336.6 |
| Throughput median (tok/s) |          2.0 |   **4.5** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        738.7 |     174.3 | **164.7** |
| TPOT median (ms)          |         64.4 |  **63.6** |     103.1 |
| E2E median (ms)           |        795.9 | **227.5** |     258.7 |
| Throughput median (tok/s) |          1.5 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        396.9 | **60.9** |   82.2 |
| TPOT median (ms)          |         63.4 | **29.9** |   49.3 |
| E2E median (ms)           |        454.0 | **83.1** |  150.6 |
| Throughput median (tok/s) |          2.8 | **14.6** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        465.8 |  **70.3** |   81.3 |
| TPOT median (ms)          |         22.1 |  **15.0** |   23.8 |
| E2E median (ms)           |       1281.4 | **614.3** |  887.0 |
| Throughput median (tok/s) |         28.2 |  **59.7** |   39.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        456.3 | **134.8** |  136.3 |
| TPOT median (ms)          |         49.6 |  **34.3** |   49.6 |
| E2E median (ms)           |        685.7 | **274.2** |  369.3 |
| Throughput median (tok/s) |          7.5 |  **18.3** |   12.4 |
| Correctness               |          99% |       99% |    98% |
