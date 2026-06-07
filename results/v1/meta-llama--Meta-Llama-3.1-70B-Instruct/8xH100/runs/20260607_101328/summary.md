# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 AM PT, Jun 7 2026

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
| torchinferno |     369.5s (6.2m) | `73aa664` |
| vllm         |   1303.4s (21.7m) | `3d3ba46` |
| sglang       | **199.9s (3.3m)** | `a07d813` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        333.1 |     157.6 | **144.3** |
| TPOT median (ms)          |     **52.9** |      53.6 |      72.3 |
| E2E median (ms)           |        391.3 | **212.5** |     214.4 |
| Throughput median (tok/s) |          3.3 |   **7.1** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        250.3 | **200.3** |  213.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        350.1 | **219.3** |  365.6 |
| Throughput median (tok/s) |          2.9 |   **4.6** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        767.9 |     170.0 | **160.2** |
| TPOT median (ms)          |         63.8 |  **43.5** |     104.0 |
| E2E median (ms)           |        809.9 | **211.8** |     264.6 |
| Throughput median (tok/s) |          1.7 |   **6.5** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        474.0 | **59.0** |   76.2 |
| TPOT median (ms)          |         31.3 | **28.6** |   54.7 |
| E2E median (ms)           |        505.2 | **80.4** |  138.0 |
| Throughput median (tok/s) |          2.9 | **15.1** |   10.2 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        560.6 |  **75.0** |   75.3 |
| TPOT median (ms)          |         32.3 |  **15.1** |   23.6 |
| E2E median (ms)           |       1699.7 | **616.8** |  886.1 |
| Throughput median (tok/s) |         20.5 |  **58.5** |   39.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        477.2 | **132.4** |  133.8 |
| TPOT median (ms)          |         36.1 |  **28.2** |   50.9 |
| E2E median (ms)           |        751.2 | **268.2** |  373.7 |
| Throughput median (tok/s) |          6.2 |  **18.3** |   12.7 |
| Correctness               |          98% |       98% |    99% |
