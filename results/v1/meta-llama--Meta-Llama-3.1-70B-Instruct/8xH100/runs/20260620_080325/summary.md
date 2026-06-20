# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 20 2026

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
| torchinferno |     388.7s (6.5m) | `cfe98ee` |
| vllm         |     522.0s (8.7m) | `dced290` |
| sglang       | **271.8s (4.5m)** | `c1416bb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        148.7 | **120.6** |  150.2 |
| TPOT median (ms)          |         45.6 |  **39.4** |   81.9 |
| E2E median (ms)           |        194.7 | **152.3** |  225.8 |
| Throughput median (tok/s) |          6.1 |   **8.6** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        316.0 | **178.4** |  223.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        427.0 | **201.6** |  375.3 |
| Throughput median (tok/s) |          2.3 |   **5.0** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        453.1 | **159.4** |  173.8 |
| TPOT median (ms)          |         56.6 |  **48.2** |  106.0 |
| E2E median (ms)           |        507.9 | **204.4** |  275.6 |
| Throughput median (tok/s) |          2.4 |   **6.8** |    4.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        279.5 | **58.0** |   84.2 |
| TPOT median (ms)          |         31.5 | **29.3** |   42.7 |
| E2E median (ms)           |        311.8 | **80.0** |  141.9 |
| Throughput median (tok/s) |          4.7 | **14.9** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        345.3 |  **67.1** |   82.3 |
| TPOT median (ms)          |         21.9 |  **14.9** |   23.2 |
| E2E median (ms)           |       1192.9 | **600.3** |  881.3 |
| Throughput median (tok/s) |         31.5 |  **59.8** |   39.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        308.5 | **116.7** |  142.7 |
| TPOT median (ms)          |         31.1 |  **26.4** |   50.7 |
| E2E median (ms)           |        526.9 | **247.7** |  380.0 |
| Throughput median (tok/s) |          9.4 |  **19.0** |   12.5 |
| Correctness               |          99% |       98% |    99% |
