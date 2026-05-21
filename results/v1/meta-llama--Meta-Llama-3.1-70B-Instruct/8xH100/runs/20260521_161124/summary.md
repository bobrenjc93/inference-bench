# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, May 21 2026

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
| torchinferno |     355.3s (5.9m) | `9f91b40` |
| vllm         |   1200.9s (20.0m) | `1c78f76` |
| sglang       | **202.1s (3.4m)** | `a24c374` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        285.5 |    161.8 | **139.8** |
| TPOT median (ms)          |        150.8 | **61.9** |      70.7 |
| E2E median (ms)           |        377.4 |    220.4 | **208.1** |
| Throughput median (tok/s) |          3.9 |  **6.6** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        268.8 |     208.6 | **200.1** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        298.9 | **231.0** |     334.3 |
| Throughput median (tok/s) |          3.3 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        741.6 |     171.3 | **161.0** |
| TPOT median (ms)          |        118.4 |  **70.1** |     105.0 |
| E2E median (ms)           |        880.3 | **232.2** |     261.7 |
| Throughput median (tok/s) |          1.4 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        372.5 | **58.4** |   72.4 |
| TPOT median (ms)          |        128.4 | **26.6** |   63.7 |
| E2E median (ms)           |        466.8 | **78.8** |  143.6 |
| Throughput median (tok/s) |          3.0 | **15.5** |    9.4 |
| Correctness               |          98% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        832.5 |      66.2 | **65.1** |
| TPOT median (ms)          |         16.9 |  **15.0** |     22.0 |
| E2E median (ms)           |       1583.9 | **606.8** |    812.2 |
| Throughput median (tok/s) |         22.9 |  **59.1** |     42.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        500.2 |     133.3 | **127.7** |
| TPOT median (ms)          |         82.9 |  **34.7** |      52.3 |
| E2E median (ms)           |        721.5 | **273.8** |     352.0 |
| Throughput median (tok/s) |          6.9 |  **18.3** |      13.2 |
| Correctness               |          99% |       98% |       99% |
