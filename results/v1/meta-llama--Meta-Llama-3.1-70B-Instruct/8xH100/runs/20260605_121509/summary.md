# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 AM PT, Jun 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     406.2s (6.8m) | `89edcfc` |
| vllm         |   1383.5s (23.1m) | `7fe7800` |
| sglang       | **198.9s (3.3m)** | `e1955bf` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        346.8 |     162.2 | **145.3** |
| TPOT median (ms)          |     **54.0** |      55.5 |      74.4 |
| E2E median (ms)           |        406.1 | **217.6** |     219.7 |
| Throughput median (tok/s) |          3.1 |   **7.1** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        228.6 | **197.8** |  201.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        353.9 | **231.6** |  349.2 |
| Throughput median (tok/s) |          2.8 |   **4.3** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        720.9 |     168.1 | **163.2** |
| TPOT median (ms)          |         68.2 |  **65.6** |      99.6 |
| E2E median (ms)           |        784.7 | **220.5** |     262.8 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        389.1 | **61.9** |   80.7 |
| TPOT median (ms)          |         32.0 | **28.6** |   55.1 |
| E2E median (ms)           |        419.9 | **83.7** |  145.2 |
| Throughput median (tok/s) |          3.4 | **14.5** |    9.6 |
| Correctness               |          96% |      96% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        541.0 |  **77.2** |   81.3 |
| TPOT median (ms)          |         31.6 |  **15.0** |   23.2 |
| E2E median (ms)           |       1598.6 | **628.6** |  873.2 |
| Throughput median (tok/s) |         20.8 |  **58.6** |   40.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        445.3 | **133.5** |  134.4 |
| TPOT median (ms)          |         37.1 |  **32.9** |   50.4 |
| E2E median (ms)           |        712.6 | **276.4** |  370.0 |
| Throughput median (tok/s) |          6.4 |  **18.2** |   12.6 |
| Correctness               |          98% |       98% |    98% |
