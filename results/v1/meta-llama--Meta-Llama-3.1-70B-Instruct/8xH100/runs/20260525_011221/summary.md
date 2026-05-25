# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:04 PM PT, May 24 2026

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
| torchinferno |     354.8s (5.9m) | `9f91b40` |
| vllm         |   1285.0s (21.4m) | `d0a100c` |
| sglang       | **199.7s (3.3m)** | `ed179bf` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        293.2 |     159.7 | **143.6** |
| TPOT median (ms)          |        153.3 |  **59.3** |      72.7 |
| E2E median (ms)           |        398.9 | **214.8** |     215.1 |
| Throughput median (tok/s) |          3.8 |   **7.1** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        300.0 | **194.3** |  206.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        328.7 | **217.7** |  349.8 |
| Throughput median (tok/s) |          3.0 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        742.2 |     181.3 | **158.6** |
| TPOT median (ms)          |        148.4 |  **62.8** |     104.5 |
| E2E median (ms)           |        868.8 | **226.9** |     257.8 |
| Throughput median (tok/s) |          1.5 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        358.4 | **58.3** |   76.4 |
| TPOT median (ms)          |        129.7 | **27.0** |   60.9 |
| E2E median (ms)           |        463.6 | **78.9** |  151.7 |
| Throughput median (tok/s) |          2.9 | **15.7** |    9.5 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        833.1 |      77.0 | **66.3** |
| TPOT median (ms)          |         16.0 |  **15.1** |     22.8 |
| E2E median (ms)           |       1633.2 | **625.7** |    875.9 |
| Throughput median (tok/s) |         19.6 |  **57.7** |     41.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        505.4 |     134.1 | **130.2** |
| TPOT median (ms)          |         89.5 |  **32.8** |      52.2 |
| E2E median (ms)           |        738.6 | **272.8** |     370.1 |
| Throughput median (tok/s) |          6.2 |  **18.2** |      12.9 |
| Correctness               |          98% |       99% |       98% |
