# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jun 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **19/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     392.0s (6.5m) | `31187b4` |
| vllm         |     477.4s (8.0m) | `0119213` |
| sglang       | **262.1s (4.4m)** | `ca88b7f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        335.5 | **132.8** |  150.1 |
| TPOT median (ms)          |         54.4 |  **45.1** |   78.1 |
| E2E median (ms)           |        386.7 | **168.9** |  222.6 |
| Throughput median (tok/s) |          3.1 |   **8.1** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        318.9 | **192.9** |  234.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        429.9 | **263.2** |  390.3 |
| Throughput median (tok/s) |          2.3 |   **3.8** |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       3400.3 | **157.0** |  167.3 |
| TPOT median (ms)          |         69.0 |  **47.2** |  112.1 |
| E2E median (ms)           |       3465.1 | **200.1** |  267.2 |
| Throughput median (tok/s) |          0.5 |   **6.7** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        204.6 | **58.2** |   81.5 |
| TPOT median (ms)          |         30.7 | **28.5** |   45.6 |
| E2E median (ms)           |        234.4 | **79.9** |  139.2 |
| Throughput median (tok/s) |          5.4 | **15.5** |    9.9 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        434.5 |  **65.7** |   67.8 |
| TPOT median (ms)          |         35.5 |  **15.2** |   22.5 |
| E2E median (ms)           |       1625.7 | **601.7** |  830.3 |
| Throughput median (tok/s) |         21.9 |  **58.8** |   41.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        938.7 | **121.3** |  140.3 |
| TPOT median (ms)          |         37.9 |  **27.2** |   51.7 |
| E2E median (ms)           |       1228.3 | **262.8** |  369.9 |
| Throughput median (tok/s) |          6.6 |  **18.6** |   12.9 |
| Correctness               |          99% |       98% |    99% |
