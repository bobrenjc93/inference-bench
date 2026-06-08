# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 8 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     419.0s (7.0m) | `446ca63` |
| vllm         |   1361.6s (22.7m) | `fa662b1` |
| sglang       | **222.8s (3.7m)** | `a26587d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        288.9 |     160.5 | **153.3** |
| TPOT median (ms)          |         98.8 |  **59.8** |      70.6 |
| E2E median (ms)           |        384.1 | **211.6** |     219.9 |
| Throughput median (tok/s) |          3.0 |   **6.9** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        418.1 |     210.2 | **201.8** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        558.7 | **234.3** |     334.4 |
| Throughput median (tok/s) |          1.8 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        704.7 |     178.9 | **164.5** |
| TPOT median (ms)          |         71.1 |  **69.8** |      94.2 |
| E2E median (ms)           |        776.5 | **240.4** |     257.5 |
| Throughput median (tok/s) |          1.6 |   **5.9** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        381.5 | **61.7** |   84.0 |
| TPOT median (ms)          |         65.1 | **27.7** |   56.6 |
| E2E median (ms)           |        427.9 | **84.1** |  144.5 |
| Throughput median (tok/s) |          3.0 | **14.3** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        535.2 |  **72.4** |   82.4 |
| TPOT median (ms)          |         21.3 |  **14.7** |   23.7 |
| E2E median (ms)           |       1232.4 | **603.9** |  897.1 |
| Throughput median (tok/s) |         27.2 |  **59.1** |   39.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        465.7 | **136.7** |  137.2 |
| TPOT median (ms)          |         51.3 |  **34.4** |   49.0 |
| E2E median (ms)           |        675.9 | **274.9** |  370.7 |
| Throughput median (tok/s) |          7.3 |  **18.1** |   12.5 |
| Correctness               |          98% |       98% |    99% |
