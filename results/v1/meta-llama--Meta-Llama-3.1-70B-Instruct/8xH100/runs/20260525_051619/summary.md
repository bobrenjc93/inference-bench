# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:04 PM PT, May 24 2026

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
| torchinferno |     425.6s (7.1m) | `9f91b40` |
| vllm         |   1278.6s (21.3m) | `6cbe448` |
| sglang       | **215.1s (3.6m)** | `ec6fcb9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        284.5 |    159.1 | **138.3** |
| TPOT median (ms)          |        152.5 | **58.0** |      77.0 |
| E2E median (ms)           |        377.4 |    217.0 | **210.2** |
| Throughput median (tok/s) |          4.0 |  **6.5** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        248.3 |     210.2 | **202.3** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        301.0 | **234.8** |     333.8 |
| Throughput median (tok/s) |          3.3 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        726.8 |     179.8 | **163.2** |
| TPOT median (ms)          |        101.9 |  **51.5** |     102.3 |
| E2E median (ms)           |        826.9 | **231.6** |     260.2 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        350.5 | **58.1** |   76.7 |
| TPOT median (ms)          |        131.1 | **26.7** |   55.3 |
| E2E median (ms)           |        438.1 | **78.5** |  153.7 |
| Throughput median (tok/s) |          3.2 | **15.7** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        799.9 |      67.3 | **65.6** |
| TPOT median (ms)          |         15.3 |  **15.0** |     22.2 |
| E2E median (ms)           |       1466.3 | **606.4** |    841.6 |
| Throughput median (tok/s) |         24.4 |  **59.3** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        482.0 |     134.9 | **129.2** |
| TPOT median (ms)          |         80.2 |  **30.3** |      51.4 |
| E2E median (ms)           |        681.9 | **273.6** |     359.9 |
| Throughput median (tok/s) |          7.3 |  **18.4** |      13.1 |
| Correctness               |          99% |       99% |       99% |
