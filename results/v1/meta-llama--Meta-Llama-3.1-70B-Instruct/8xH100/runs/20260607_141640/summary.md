# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jun 7 2026

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
| torchinferno |     385.5s (6.4m) | `73aa664` |
| vllm         |   1334.3s (22.2m) | `228bcc4` |
| sglang       | **221.0s (3.7m)** | `a07d813` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        306.5 |     159.4 | **156.5** |
| TPOT median (ms)          |     **51.3** |      59.1 |      76.4 |
| E2E median (ms)           |        356.0 | **212.6** |     229.1 |
| Throughput median (tok/s) |          3.3 |   **6.9** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        248.5 | **204.5** |  210.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        346.0 | **230.5** |  345.8 |
| Throughput median (tok/s) |          2.9 |   **4.3** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        709.1 |     177.3 | **164.6** |
| TPOT median (ms)          |         62.9 |  **56.5** |      96.6 |
| E2E median (ms)           |        773.8 | **222.7** |     263.3 |
| Throughput median (tok/s) |          1.7 |   **6.3** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        362.1 | **60.5** |   82.9 |
| TPOT median (ms)          |         31.7 | **27.9** |   47.5 |
| E2E median (ms)           |        389.9 | **82.2** |  142.6 |
| Throughput median (tok/s) |          3.3 | **14.9** |    9.6 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        590.8 |  **70.5** |   78.9 |
| TPOT median (ms)          |         33.4 |  **15.1** |   23.2 |
| E2E median (ms)           |       1775.5 | **615.7** |  899.3 |
| Throughput median (tok/s) |         19.8 |  **58.8** |   40.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        443.4 | **134.5** |  138.7 |
| TPOT median (ms)          |         35.9 |  **31.7** |   48.7 |
| E2E median (ms)           |        728.2 | **272.7** |  376.0 |
| Throughput median (tok/s) |          6.2 |  **18.2** |   12.5 |
| Correctness               |          98% |       99% |    98% |
