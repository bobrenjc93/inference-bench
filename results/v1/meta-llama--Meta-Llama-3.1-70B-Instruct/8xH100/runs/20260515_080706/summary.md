# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 AM PT, May 15 2026

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
| torchinferno |     294.8s (4.9m) | `d648af4` |
| vllm         |   1118.6s (18.6m) | `31fa757` |
| sglang       | **163.8s (2.7m)** | `66ef97c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        314.7 |    165.0 | **142.1** |
| TPOT median (ms)          |        159.3 | **58.6** |      77.1 |
| E2E median (ms)           |        405.8 |    215.5 | **212.1** |
| Throughput median (tok/s) |          3.5 |  **6.8** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        299.7 |     208.1 | **207.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        378.0 | **228.5** |     351.9 |
| Throughput median (tok/s) |          2.6 |   **4.4** |       2.8 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        563.0 |     172.2 | **164.2** |
| TPOT median (ms)          |        131.8 |  **64.0** |      98.1 |
| E2E median (ms)           |        685.6 | **230.4** |     262.4 |
| Throughput median (tok/s) |          2.1 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        338.2 | **58.1** |   78.0 |
| TPOT median (ms)          |        135.4 | **26.8** |   54.0 |
| E2E median (ms)           |        436.2 | **78.3** |  143.5 |
| Throughput median (tok/s) |          3.3 | **15.7** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        536.2 |      75.3 | **68.6** |
| TPOT median (ms)          |         15.5 |  **14.9** |     22.3 |
| E2E median (ms)           |       1226.3 | **632.0** |    815.8 |
| Throughput median (tok/s) |         27.0 |  **58.7** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        410.4 |     135.7 | **132.1** |
| TPOT median (ms)          |         88.4 |  **32.9** |      50.3 |
| E2E median (ms)           |        626.4 | **276.9** |     357.1 |
| Throughput median (tok/s) |          7.7 |  **18.3** |      13.2 |
| Correctness               |          98% |       99% |       98% |
