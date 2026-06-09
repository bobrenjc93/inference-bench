# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 AM PT, Jun 9 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     344.3s (5.7m) | `bb2b2bf` |
| vllm         |   1325.0s (22.1m) | `59401ac` |
| sglang       | **193.6s (3.2m)** | `fdcd28a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        311.9 |     157.7 | **156.2** |
| TPOT median (ms)          |         94.6 |  **57.3** |      71.8 |
| E2E median (ms)           |        392.0 | **212.0** |     224.1 |
| Throughput median (tok/s) |          3.0 |   **7.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        376.6 | **178.0** |  198.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        514.5 | **215.9** |  336.7 |
| Throughput median (tok/s) |          1.9 |   **4.6** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        666.6 |     172.3 | **168.5** |
| TPOT median (ms)          |         69.1 |  **54.6** |     110.2 |
| E2E median (ms)           |        736.2 | **220.0** |     272.0 |
| Throughput median (tok/s) |          1.7 |   **6.2** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        322.6 | **58.3** |   84.3 |
| TPOT median (ms)          |         63.0 | **28.4** |   43.0 |
| E2E median (ms)           |        381.8 | **79.7** |  140.2 |
| Throughput median (tok/s) |          3.6 | **15.1** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        497.1 |  **65.3** |   78.2 |
| TPOT median (ms)          |         21.5 |  **15.1** |   24.2 |
| E2E median (ms)           |       1120.8 | **603.8** |  894.2 |
| Throughput median (tok/s) |         28.9 |  **58.9** |   39.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        434.9 | **126.3** |  137.2 |
| TPOT median (ms)          |         49.6 |  **31.1** |   49.8 |
| E2E median (ms)           |        629.1 | **266.3** |  373.4 |
| Throughput median (tok/s) |          7.8 |  **18.4** |   12.4 |
| Correctness               |          99% |       99% |    99% |
