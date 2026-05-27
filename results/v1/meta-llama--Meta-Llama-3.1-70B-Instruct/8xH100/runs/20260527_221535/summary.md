# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 PM PT, May 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     426.6s (7.1m) | `1159634` |
| vllm         |   1356.8s (22.6m) | `2c2c966` |
| sglang       | **206.3s (3.4m)** | `e06058e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        287.5 |    155.9 | **146.3** |
| TPOT median (ms)          |         72.0 | **58.3** |      75.9 |
| E2E median (ms)           |        352.7 |    216.2 | **215.6** |
| Throughput median (tok/s) |          3.4 |  **7.0** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.2 | **187.6** |  200.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        333.8 | **206.5** |  335.4 |
| Throughput median (tok/s) |          3.0 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        774.6 |     180.0 | **165.4** |
| TPOT median (ms)          |     **59.0** |      66.1 |     104.2 |
| E2E median (ms)           |        835.6 | **242.5** |     266.1 |
| Throughput median (tok/s) |          1.5 |   **6.0** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        195.5 | **60.2** |   75.9 |
| TPOT median (ms)          |         28.7 | **28.7** |   47.0 |
| E2E median (ms)           |        227.2 | **82.1** |  137.8 |
| Throughput median (tok/s) |          6.1 | **15.0** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        700.1 |  **69.1** |   77.8 |
| TPOT median (ms)          |     **15.1** |      15.1 |   23.0 |
| E2E median (ms)           |       1391.3 | **610.5** |  869.1 |
| Throughput median (tok/s) |         24.6 |  **58.6** |   40.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        449.6 | **130.6** |  133.3 |
| TPOT median (ms)          |         35.0 |  **33.6** |   50.0 |
| E2E median (ms)           |        628.1 | **271.5** |  364.8 |
| Throughput median (tok/s) |          7.7 |  **18.3** |   12.8 |
| Correctness               |          99% |       98% |    99% |
