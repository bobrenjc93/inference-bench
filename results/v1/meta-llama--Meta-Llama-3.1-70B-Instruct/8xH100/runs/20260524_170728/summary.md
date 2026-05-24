# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:03 AM PT, May 24 2026

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
| torchinferno |     266.4s (4.4m) | `9f91b40` |
| vllm         |   1259.3s (21.0m) | `1806d1a` |
| sglang       | **193.3s (3.2m)** | `5c37758` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        300.4 |     155.1 | **140.1** |
| TPOT median (ms)          |        154.6 |  **55.2** |      79.3 |
| E2E median (ms)           |        410.0 | **206.9** |     213.1 |
| Throughput median (tok/s) |          3.7 |   **7.3** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        296.6 | **192.4** |  200.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        320.3 | **214.2** |  332.9 |
| Throughput median (tok/s) |          3.1 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        699.4 |     173.5 | **156.9** |
| TPOT median (ms)          |        121.9 |  **58.1** |      99.7 |
| E2E median (ms)           |        792.9 | **227.4** |     261.6 |
| Throughput median (tok/s) |          1.7 |   **6.3** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        369.0 | **58.7** |   79.5 |
| TPOT median (ms)          |        132.8 | **27.1** |   63.8 |
| E2E median (ms)           |        477.6 | **78.6** |  157.4 |
| Throughput median (tok/s) |          2.8 | **15.6** |    9.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        984.6 |      73.1 | **64.2** |
| TPOT median (ms)          |         16.4 |  **14.9** |     22.3 |
| E2E median (ms)           |       1587.7 | **628.7** |    826.0 |
| Throughput median (tok/s) |         20.7 |  **58.4** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        530.0 |     130.6 | **128.2** |
| TPOT median (ms)          |         85.1 |  **31.1** |      53.0 |
| E2E median (ms)           |        717.7 | **271.2** |     358.2 |
| Throughput median (tok/s) |          6.4 |  **18.4** |      12.9 |
| Correctness               |          98% |       99% |       99% |
