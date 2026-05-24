# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 PM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     332.5s (5.5m) | `9f91b40` |
| vllm         |   1299.4s (21.7m) | `33d7cbe` |
| sglang       | **209.4s (3.5m)** | `d6d9f12` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        300.8 |     152.8 | **141.2** |
| TPOT median (ms)          |        157.1 |  **58.1** |      78.6 |
| E2E median (ms)           |        410.6 | **205.0** |     214.4 |
| Throughput median (tok/s) |          3.7 |   **7.3** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        236.7 | **179.3** |  205.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        329.4 | **201.5** |  342.9 |
| Throughput median (tok/s) |          3.0 |   **5.0** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        805.1 |     173.4 | **162.1** |
| TPOT median (ms)          |        114.8 |  **57.1** |     103.5 |
| E2E median (ms)           |        914.5 | **223.2** |     266.5 |
| Throughput median (tok/s) |          1.4 |   **6.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        435.3 | **56.6** |   78.8 |
| TPOT median (ms)          |        133.9 | **27.0** |   62.4 |
| E2E median (ms)           |        548.2 | **76.6** |  148.0 |
| Throughput median (tok/s) |          2.7 | **16.0** |    9.2 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        811.0 |      73.2 | **66.9** |
| TPOT median (ms)          |         15.9 |  **15.1** |     22.4 |
| E2E median (ms)           |       1551.4 | **611.5** |    821.6 |
| Throughput median (tok/s) |         21.5 |  **58.3** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        517.8 | **127.1** |  130.9 |
| TPOT median (ms)          |         84.3 |  **31.5** |   53.4 |
| E2E median (ms)           |        750.8 | **263.5** |  358.7 |
| Throughput median (tok/s) |          6.5 |  **18.5** |   12.9 |
| Correctness               |          98% |       98% |    99% |
