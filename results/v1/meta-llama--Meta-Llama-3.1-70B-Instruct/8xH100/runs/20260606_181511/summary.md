# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jun 6 2026

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
| torchinferno |     459.2s (7.7m) | `25260c0` |
| vllm         |   1362.9s (22.7m) | `fa27d4e` |
| sglang       | **219.7s (3.7m)** | `88a7b0f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        275.3 |     161.8 | **145.4** |
| TPOT median (ms)          |     **48.2** |      59.0 |      75.8 |
| E2E median (ms)           |        319.8 | **210.7** |     215.8 |
| Throughput median (tok/s) |          4.2 |   **6.8** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        247.3 | **181.6** |  220.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        346.2 | **205.0** |  364.8 |
| Throughput median (tok/s) |          2.9 |   **4.9** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        648.6 |     169.6 | **164.4** |
| TPOT median (ms)          |         58.8 |  **54.3** |     108.6 |
| E2E median (ms)           |        714.0 | **219.2** |     272.9 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        431.7 | **59.3** |   77.2 |
| TPOT median (ms)          |         31.7 | **29.1** |   55.4 |
| E2E median (ms)           |        461.5 | **80.4** |  144.3 |
| Throughput median (tok/s) |          3.1 | **15.2** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        532.7 |  **67.7** |   82.6 |
| TPOT median (ms)          |         31.1 |  **15.1** |   23.7 |
| E2E median (ms)           |       1609.9 | **616.5** |  897.9 |
| Throughput median (tok/s) |         22.5 |  **58.9** |   39.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        427.1 | **128.0** |  138.0 |
| TPOT median (ms)          |         34.0 |  **31.5** |   52.7 |
| E2E median (ms)           |        690.3 | **266.4** |  379.1 |
| Throughput median (tok/s) |          6.9 |  **18.4** |   12.4 |
| Correctness               |          98% |       99% |    99% |
