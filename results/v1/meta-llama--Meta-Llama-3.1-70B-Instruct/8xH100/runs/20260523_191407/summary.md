# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:03 AM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     331.2s (5.5m) | `9f91b40` |
| vllm         |   1289.8s (21.5m) | `4438b6e` |
| sglang       | **202.3s (3.4m)** | `2de7403` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        291.0 |    174.0 | **141.8** |
| TPOT median (ms)          |        156.3 | **65.9** |      77.0 |
| E2E median (ms)           |        391.8 |    228.4 | **214.1** |
| Throughput median (tok/s) |          3.8 |  **6.3** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.4 | **184.2** |  196.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        319.5 | **204.3** |  328.7 |
| Throughput median (tok/s) |          3.1 |   **4.9** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        785.3 |     173.8 | **156.8** |
| TPOT median (ms)          |        153.4 |  **47.1** |     102.6 |
| E2E median (ms)           |        903.7 | **219.8** |     259.3 |
| Throughput median (tok/s) |          1.4 |   **6.4** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        311.0 | **59.3** |   76.3 |
| TPOT median (ms)          |        132.9 | **27.2** |   49.5 |
| E2E median (ms)           |        408.8 | **79.8** |  136.4 |
| Throughput median (tok/s) |          3.6 | **15.4** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        888.1 |      67.9 | **66.4** |
| TPOT median (ms)          |         16.6 |  **15.1** |     22.6 |
| E2E median (ms)           |       1607.4 | **613.4** |    829.9 |
| Throughput median (tok/s) |         20.9 |  **59.0** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        513.2 |     131.8 | **127.6** |
| TPOT median (ms)          |         91.8 |  **31.1** |      50.4 |
| E2E median (ms)           |        726.2 | **269.1** |     353.7 |
| Throughput median (tok/s) |          6.6 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       98% |
