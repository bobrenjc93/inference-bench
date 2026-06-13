# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jun 13 2026

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
| torchinferno |     417.9s (7.0m) | `a102128` |
| vllm         |   1356.7s (22.6m) | `71b961d` |
| sglang       | **193.9s (3.2m)** | `27ba133` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        285.3 |     156.1 | **147.3** |
| TPOT median (ms)          |        100.7 |  **62.3** |      76.0 |
| E2E median (ms)           |        372.9 | **211.2** |     220.6 |
| Throughput median (tok/s) |          3.2 |   **7.2** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        316.2 | **194.1** |  197.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        438.6 | **246.0** |  338.3 |
| Throughput median (tok/s) |          2.3 |   **4.1** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        697.2 |     172.2 | **167.3** |
| TPOT median (ms)          |         69.8 |  **56.7** |      99.6 |
| E2E median (ms)           |        771.4 | **217.9** |     265.0 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        260.5 | **62.2** |   79.5 |
| TPOT median (ms)          |         53.7 | **27.5** |   47.0 |
| E2E median (ms)           |        319.0 | **83.9** |  136.5 |
| Throughput median (tok/s) |          4.4 | **14.6** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        349.8 |      69.2 | **68.4** |
| TPOT median (ms)          |         21.9 |  **14.7** |     22.4 |
| E2E median (ms)           |       1136.6 | **597.2** |    817.0 |
| Throughput median (tok/s) |         31.8 |  **60.1** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        381.8 | **130.7** |  131.9 |
| TPOT median (ms)          |         49.2 |  **32.3** |   49.0 |
| E2E median (ms)           |        607.7 | **271.2** |  355.5 |
| Throughput median (tok/s) |          8.7 |  **18.4** |   13.1 |
| Correctness               |          99% |       99% |    98% |
