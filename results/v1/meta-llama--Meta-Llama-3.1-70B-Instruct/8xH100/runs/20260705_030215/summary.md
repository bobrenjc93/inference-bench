# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **2/4** |       1/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **40.5s (0.7m)** | `390fed4` |
| vllm         |    313.0s (5.2m) | `34b560b` |
| sglang       |    246.4s (4.1m) | `5e6f49c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        161.7 |     149.2 | **142.3** |
| TPOT median (ms)          |     **49.3** |      50.6 |      72.9 |
| E2E median (ms)           |        213.8 | **187.9** |     216.9 |
| Throughput median (tok/s) |          5.7 |   **7.2** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        179.1 | **164.0** |  238.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |    **191.7** |     289.0 |  396.5 |
| Throughput median (tok/s) |      **5.2** |       3.5 |    2.5 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        340.0 | **147.7** |  166.9 |
| TPOT median (ms)          |     **62.9** |      66.8 |   99.5 |
| E2E median (ms)           |        398.6 | **208.4** |  268.0 |
| Throughput median (tok/s) |          3.6 |   **6.3** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        119.9 | **65.6** |   74.2 |
| TPOT median (ms)          |         44.6 | **29.6** |   57.2 |
| E2E median (ms)           |        148.5 | **90.4** |  139.9 |
| Throughput median (tok/s) |          9.0 | **13.6** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        250.4 |      76.6 | **74.4** |
| TPOT median (ms)          |         20.9 |  **14.9** |     22.3 |
| E2E median (ms)           |        982.9 | **617.6** |    838.1 |
| Throughput median (tok/s) |         36.1 |  **59.1** |     40.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        210.2 | **120.6** |  139.2 |
| TPOT median (ms)          |         35.5 |  **32.4** |   50.4 |
| E2E median (ms)           |        387.1 | **278.7** |  371.9 |
| Throughput median (tok/s) |         11.9 |  **17.9** |   12.7 |
| Correctness               |          98% |       98% |    98% |
