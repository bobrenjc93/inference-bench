# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 AM PT, Jun 30 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **18/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    858.6s (14.3m) | `7cbb5fe` |
| vllm         |    603.1s (10.1m) | `ea9ddf5` |
| sglang       | **383.5s (6.4m)** | `c6a7c98` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        171.3 | **138.7** |  142.1 |
| TPOT median (ms)          |     **49.7** |      52.2 |   74.3 |
| E2E median (ms)           |        212.1 | **181.1** |  213.0 |
| Throughput median (tok/s) |          5.4 |   **7.9** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        235.3 | **191.9** |  214.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        275.8 | **218.1** |  351.8 |
| Throughput median (tok/s) |          3.6 |   **4.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        299.8 | **155.9** |  163.4 |
| TPOT median (ms)          |         56.8 |  **49.6** |  101.4 |
| E2E median (ms)           |        351.3 | **200.9** |  264.5 |
| Throughput median (tok/s) |          4.2 |   **6.7** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        201.3 | **59.3** |   84.9 |
| TPOT median (ms)          |         58.6 | **31.2** |   48.5 |
| E2E median (ms)           |        241.0 | **83.3** |  145.6 |
| Throughput median (tok/s) |          5.6 | **14.9** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        322.1 |  **74.5** |   75.8 |
| TPOT median (ms)          |         23.0 |  **14.9** |   22.5 |
| E2E median (ms)           |       1157.6 | **606.3** |  842.1 |
| Throughput median (tok/s) |         32.0 |  **59.1** |   41.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        246.0 | **124.1** |  136.0 |
| TPOT median (ms)          |         37.6 |  **29.6** |   49.3 |
| E2E median (ms)           |        447.6 | **257.9** |  363.4 |
| Throughput median (tok/s) |         10.2 |  **18.6** |   12.9 |
| Correctness               |          98% |       99% |    98% |
