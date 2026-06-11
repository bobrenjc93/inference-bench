# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:04 AM PT, Jun 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     438.0s (7.3m) | `065275c` |
| vllm         |   1426.2s (23.8m) | `f81daf8` |
| sglang       | **196.2s (3.3m)** | `7f57b34` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        310.2 |     160.6 | **147.3** |
| TPOT median (ms)          |         95.3 |  **56.0** |      83.3 |
| E2E median (ms)           |        402.0 | **215.4** |     225.1 |
| Throughput median (tok/s) |          3.2 |   **6.9** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        396.8 | **213.8** |  216.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        543.6 | **236.6** |  349.9 |
| Throughput median (tok/s) |          1.8 |   **4.2** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        731.8 | **165.5** |  168.3 |
| TPOT median (ms)          |         60.2 |  **58.8** |  100.2 |
| E2E median (ms)           |        790.2 | **213.7** |  271.4 |
| Throughput median (tok/s) |          1.7 |   **6.2** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        442.1 | **62.9** |   82.3 |
| TPOT median (ms)          |         62.8 | **28.8** |   46.2 |
| E2E median (ms)           |        477.4 | **85.2** |  139.6 |
| Throughput median (tok/s) |          3.2 | **14.2** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        195.1 |  **74.1** |   77.8 |
| TPOT median (ms)          |         26.3 |  **15.1** |   23.9 |
| E2E median (ms)           |       1181.1 | **626.4** |  911.8 |
| Throughput median (tok/s) |         31.1 |  **57.8** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        415.2 | **135.4** |  138.4 |
| TPOT median (ms)          |         48.9 |  **31.7** |   50.7 |
| E2E median (ms)           |        678.9 | **275.5** |  379.6 |
| Throughput median (tok/s) |          8.2 |  **17.9** |   12.5 |
| Correctness               |          98% |       98% |    98% |
