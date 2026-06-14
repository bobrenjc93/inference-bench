# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     339.6s (5.7m) | `a102128` |
| vllm         |   1285.7s (21.4m) | `c621af1` |
| sglang       | **209.4s (3.5m)** | `d723148` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        282.6 |    171.1 | **142.6** |
| TPOT median (ms)          |         80.9 | **61.6** |      71.9 |
| E2E median (ms)           |        355.5 |    227.0 | **213.5** |
| Throughput median (tok/s) |          3.5 |  **6.4** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        325.5 |     210.9 | **207.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        444.0 | **236.8** |     335.0 |
| Throughput median (tok/s) |          2.3 |   **4.2** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        717.0 |     175.6 | **171.9** |
| TPOT median (ms)          |         68.1 |  **59.9** |     105.7 |
| E2E median (ms)           |        807.3 | **229.3** |     268.8 |
| Throughput median (tok/s) |          1.6 |   **6.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        269.2 | **62.2** |   79.8 |
| TPOT median (ms)          |         49.6 | **28.8** |   44.2 |
| E2E median (ms)           |        313.2 | **83.4** |  138.2 |
| Throughput median (tok/s) |          4.5 | **14.4** |   10.0 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        341.0 |      79.3 | **68.3** |
| TPOT median (ms)          |         21.4 |  **15.0** |     22.2 |
| E2E median (ms)           |       1113.5 | **635.2** |    854.6 |
| Throughput median (tok/s) |         32.7 |  **57.3** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        387.1 |     139.8 | **134.0** |
| TPOT median (ms)          |         44.0 |  **33.0** |      48.8 |
| E2E median (ms)           |        606.7 | **282.3** |     362.0 |
| Throughput median (tok/s) |          8.9 |  **17.7** |      13.1 |
| Correctness               |          99% |       98% |       99% |
