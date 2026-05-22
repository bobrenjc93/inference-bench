# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:03 PM PT, May 21 2026

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
| torchinferno |     320.5s (5.3m) | `9f91b40` |
| vllm         |   1271.1s (21.2m) | `1fe3303` |
| sglang       | **187.4s (3.1m)** | `acb8310` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        294.3 |    160.3 | **136.7** |
| TPOT median (ms)          |        150.1 | **58.7** |      73.1 |
| E2E median (ms)           |        400.8 |    210.9 | **204.1** |
| Throughput median (tok/s) |          3.7 |  **7.0** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        273.7 |     204.4 | **199.1** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        322.4 | **226.2** |     335.7 |
| Throughput median (tok/s) |          3.1 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        680.5 |     158.9 | **152.8** |
| TPOT median (ms)          |        108.8 |  **52.3** |     104.7 |
| E2E median (ms)           |        761.7 | **201.0** |     249.5 |
| Throughput median (tok/s) |          1.7 |   **6.5** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        383.0 | **58.6** |   76.6 |
| TPOT median (ms)          |        129.1 | **27.2** |   67.1 |
| E2E median (ms)           |        490.7 | **79.6** |  156.1 |
| Throughput median (tok/s) |          2.8 | **15.4** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        824.1 |      67.2 | **64.6** |
| TPOT median (ms)          |         16.1 |  **15.1** |     22.3 |
| E2E median (ms)           |       1616.0 | **605.1** |    831.3 |
| Throughput median (tok/s) |         21.3 |  **59.1** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        491.1 |     129.9 | **126.0** |
| TPOT median (ms)          |         80.8 |  **30.7** |      53.4 |
| E2E median (ms)           |        718.3 | **264.5** |     355.3 |
| Throughput median (tok/s) |          6.5 |  **18.5** |      13.2 |
| Correctness               |          98% |       98% |       99% |
