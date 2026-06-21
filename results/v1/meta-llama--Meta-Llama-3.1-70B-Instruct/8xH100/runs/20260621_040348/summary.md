# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, Jun 20 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **16/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     384.7s (6.4m) | `a7e5516` |
| vllm         |     492.3s (8.2m) | `7df3d7d` |
| sglang       | **266.5s (4.4m)** | `c65f4ea` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.9 | **140.4** |  150.2 |
| TPOT median (ms)          |     **45.1** |      47.3 |   76.7 |
| E2E median (ms)           |        231.9 | **183.8** |  220.9 |
| Throughput median (tok/s) |          5.5 |   **7.8** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        292.3 | **195.3** |  216.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        405.9 | **220.5** |  370.5 |
| Throughput median (tok/s) |          2.5 |   **4.5** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        513.4 |     165.8 | **163.3** |
| TPOT median (ms)          |     **37.9** |      56.2 |     101.2 |
| E2E median (ms)           |        563.9 | **217.6** |     263.4 |
| Throughput median (tok/s) |          2.2 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        202.8 | **58.1** |   88.4 |
| TPOT median (ms)          |         30.8 | **28.5** |   38.1 |
| E2E median (ms)           |        232.2 | **79.9** |  136.1 |
| Throughput median (tok/s) |          5.5 | **15.0** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        335.3 |  **65.7** |   67.7 |
| TPOT median (ms)          |         21.7 |  **14.9** |   22.6 |
| E2E median (ms)           |       1151.5 | **597.9** |  859.1 |
| Throughput median (tok/s) |         32.2 |  **59.6** |   41.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        306.9 | **125.0** |  137.2 |
| TPOT median (ms)          |     **27.1** |      29.4 |   47.7 |
| E2E median (ms)           |        517.1 | **259.9** |  370.0 |
| Throughput median (tok/s) |          9.6 |  **18.7** |   13.0 |
| Correctness               |          99% |       99% |    99% |
