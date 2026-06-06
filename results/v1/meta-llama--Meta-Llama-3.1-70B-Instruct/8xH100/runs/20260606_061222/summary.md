# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 PM PT, Jun 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     342.6s (5.7m) | `75bbe35` |
| vllm         |   1297.6s (21.6m) | `ec0a31d` |
| sglang       | **200.2s (3.3m)** | `9da88e3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        299.7 |     154.7 | **148.3** |
| TPOT median (ms)          |     **52.2** |      54.9 |      76.2 |
| E2E median (ms)           |        343.7 | **204.6** |     215.4 |
| Throughput median (tok/s) |          4.0 |   **7.1** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        254.6 | **189.0** |  202.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        357.0 | **215.4** |  348.9 |
| Throughput median (tok/s) |          2.8 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        680.9 |     174.6 | **172.6** |
| TPOT median (ms)          |     **63.6** |      65.5 |      95.9 |
| E2E median (ms)           |        756.7 | **225.5** |     270.2 |
| Throughput median (tok/s) |          1.7 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        377.5 | **58.4** |   77.8 |
| TPOT median (ms)          |         30.7 | **27.5** |   54.9 |
| E2E median (ms)           |        407.4 | **79.3** |  142.8 |
| Throughput median (tok/s) |          3.4 | **15.1** |    9.8 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        543.5 |  **68.0** |   76.7 |
| TPOT median (ms)          |         32.3 |  **15.1** |   23.5 |
| E2E median (ms)           |       1573.1 | **620.3** |  887.7 |
| Throughput median (tok/s) |         21.1 |  **58.5** |   39.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        431.2 | **128.9** |  135.5 |
| TPOT median (ms)          |         35.8 |  **32.6** |   50.1 |
| E2E median (ms)           |        687.6 | **269.0** |  373.0 |
| Throughput median (tok/s) |          6.6 |  **18.3** |   12.6 |
| Correctness               |          98% |       98% |    99% |
