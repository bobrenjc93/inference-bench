# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **14/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     445.4s (7.4m) | `a9e2f5a` |
| vllm         |   1322.0s (22.0m) | `22c2e87` |
| sglang       | **206.0s (3.4m)** | `7aee2ff` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        293.7 |     158.1 | **146.8** |
| TPOT median (ms)          |     **53.0** |      59.5 |      79.2 |
| E2E median (ms)           |        344.7 | **213.4** |     221.5 |
| Throughput median (tok/s) |          3.6 |   **7.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        258.3 |     214.0 | **204.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        364.4 | **286.4** |     341.1 |
| Throughput median (tok/s) |          2.7 |   **3.5** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        752.1 |     179.5 | **164.7** |
| TPOT median (ms)          |        111.3 |  **58.8** |     106.5 |
| E2E median (ms)           |        830.8 | **237.6** |     276.7 |
| Throughput median (tok/s) |          1.5 |   **6.0** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        417.5 | **62.4** |   84.4 |
| TPOT median (ms)          |         32.3 | **28.3** |   57.9 |
| E2E median (ms)           |        461.6 | **84.3** |  148.2 |
| Throughput median (tok/s) |          3.3 | **14.3** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        473.2 |      77.5 | **76.7** |
| TPOT median (ms)          |         28.5 |  **14.8** |     23.4 |
| E2E median (ms)           |       1462.0 | **616.3** |    891.7 |
| Throughput median (tok/s) |         24.6 |  **58.7** |     39.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        439.0 |     138.3 | **135.5** |
| TPOT median (ms)          |         45.0 |  **32.3** |      53.4 |
| E2E median (ms)           |        692.7 | **287.6** |     375.8 |
| Throughput median (tok/s) |          7.1 |  **17.9** |      12.4 |
| Correctness               |          98% |       99% |       99% |
