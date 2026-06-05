# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:01 AM PT, Jun 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     387.4s (6.5m) | `89edcfc` |
| vllm         |   1316.2s (21.9m) | `6542d48` |
| sglang       | **200.3s (3.3m)** | `4ef081b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        306.1 |     165.4 | **161.7** |
| TPOT median (ms)          |     **50.0** |      61.3 |      69.6 |
| E2E median (ms)           |        357.6 | **220.0** |     226.2 |
| Throughput median (tok/s) |          3.4 |   **7.0** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        265.8 | **197.3** |  211.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        395.0 | **218.6** |  340.7 |
| Throughput median (tok/s) |          2.5 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        764.7 |     184.1 | **167.5** |
| TPOT median (ms)          |     **61.9** |      66.4 |      97.1 |
| E2E median (ms)           |        829.8 | **245.9** |     270.4 |
| Throughput median (tok/s) |          1.5 |   **5.8** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        419.3 | **60.6** |   82.8 |
| TPOT median (ms)          |         32.7 | **27.6** |   51.7 |
| E2E median (ms)           |        455.1 | **82.0** |  148.5 |
| Throughput median (tok/s) |          3.2 | **15.0** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        553.1 |      80.1 | **80.0** |
| TPOT median (ms)          |         32.0 |  **14.7** |     23.5 |
| E2E median (ms)           |       1597.3 | **624.3** |    884.6 |
| Throughput median (tok/s) |         21.6 |  **58.0** |     39.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        461.8 | **137.5** |  140.8 |
| TPOT median (ms)          |         35.3 |  **34.0** |   48.4 |
| E2E median (ms)           |        726.9 | **278.2** |  374.1 |
| Throughput median (tok/s) |          6.4 |  **18.1** |   12.5 |
| Correctness               |          99% |       98% |    98% |
