# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **14/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     331.8s (5.5m) | `a102128` |
| vllm         |   1271.0s (21.2m) | `c621af1` |
| sglang       | **195.6s (3.3m)** | `d723148` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        322.4 |    165.9 | **144.9** |
| TPOT median (ms)          |         98.3 | **60.6** |      73.8 |
| E2E median (ms)           |        415.8 |    221.7 | **214.6** |
| Throughput median (tok/s) |          3.0 |  **6.6** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        302.5 | **189.9** |  227.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        417.6 | **212.3** |  372.9 |
| Throughput median (tok/s) |          2.4 |   **4.7** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        673.7 |     173.4 | **157.6** |
| TPOT median (ms)          |     **63.3** |      65.7 |     100.0 |
| E2E median (ms)           |        745.5 | **228.9** |     254.5 |
| Throughput median (tok/s) |          1.9 |   **6.0** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        243.0 | **62.0** |   77.8 |
| TPOT median (ms)          |         58.0 | **28.6** |   47.3 |
| E2E median (ms)           |        309.0 | **83.9** |  142.2 |
| Throughput median (tok/s) |          4.2 | **14.5** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        354.8 |      72.5 | **69.9** |
| TPOT median (ms)          |         21.4 |  **15.1** |     22.6 |
| E2E median (ms)           |       1108.0 | **622.9** |    854.4 |
| Throughput median (tok/s) |         31.0 |  **59.1** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        379.3 | **132.7** |  135.6 |
| TPOT median (ms)          |         48.2 |  **34.0** |   48.7 |
| E2E median (ms)           |        599.2 | **273.9** |  367.7 |
| Throughput median (tok/s) |          8.5 |  **18.2** |   13.0 |
| Correctness               |          99% |       99% |    99% |
