# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 20 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     400.7s (6.7m) | `15af2ce` |
| vllm         |     515.6s (8.6m) | `dced290` |
| sglang       | **254.2s (4.2m)** | `1109acc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        176.2 | **136.8** |  142.8 |
| TPOT median (ms)          |     **37.4** |      45.7 |   77.1 |
| E2E median (ms)           |        208.9 | **173.9** |  213.4 |
| Throughput median (tok/s) |          5.5 |   **7.9** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        294.2 | **207.0** |  222.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        407.5 | **230.9** |  369.1 |
| Throughput median (tok/s) |          2.5 |   **4.3** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        550.5 | **157.3** |  165.8 |
| TPOT median (ms)          |         46.8 |  **45.0** |   99.0 |
| E2E median (ms)           |        586.3 | **191.1** |  258.6 |
| Throughput median (tok/s) |          2.1 |   **6.8** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        193.3 | **59.2** |   86.1 |
| TPOT median (ms)          |         32.5 | **29.1** |   39.7 |
| E2E median (ms)           |        227.4 | **81.8** |  143.6 |
| Throughput median (tok/s) |          5.8 | **14.9** |    9.5 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        362.6 |      74.6 | **67.8** |
| TPOT median (ms)          |         21.6 |  **14.8** |     22.5 |
| E2E median (ms)           |       1137.1 | **616.0** |    833.1 |
| Throughput median (tok/s) |         31.4 |  **58.9** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        315.4 | **127.0** |  137.0 |
| TPOT median (ms)          |         27.7 |  **26.9** |   47.7 |
| E2E median (ms)           |        513.4 | **258.7** |  363.5 |
| Throughput median (tok/s) |          9.4 |  **18.6** |   13.0 |
| Correctness               |          98% |       98% |    99% |
