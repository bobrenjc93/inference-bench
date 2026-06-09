# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 AM PT, Jun 9 2026

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
| torchinferno |     401.8s (6.7m) | `e211b4b` |
| vllm         |   1307.8s (21.8m) | `70db148` |
| sglang       | **230.1s (3.8m)** | `c6be251` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        266.8 |     152.3 | **151.3** |
| TPOT median (ms)          |         92.8 |  **51.9** |      72.8 |
| E2E median (ms)           |        354.6 | **198.9** |     221.0 |
| Throughput median (tok/s) |          3.4 |   **7.4** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        311.5 | **195.1** |  216.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        427.2 | **216.3** |  355.1 |
| Throughput median (tok/s) |          2.3 |   **4.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        723.2 |     171.5 | **157.7** |
| TPOT median (ms)          |         67.3 |  **64.8** |     103.9 |
| E2E median (ms)           |        778.6 | **230.7** |     253.4 |
| Throughput median (tok/s) |          1.8 |   **6.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        370.7 | **61.1** |   84.2 |
| TPOT median (ms)          |         59.2 | **27.9** |   44.3 |
| E2E median (ms)           |        426.8 | **82.0** |  141.1 |
| Throughput median (tok/s) |          3.3 | **14.5** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        514.3 |  **73.6** |   79.5 |
| TPOT median (ms)          |         21.3 |  **14.9** |   24.1 |
| E2E median (ms)           |       1342.2 | **607.2** |  882.5 |
| Throughput median (tok/s) |         27.7 |  **59.1** |   38.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        437.3 | **130.7** |  137.9 |
| TPOT median (ms)          |         48.1 |  **31.9** |   49.0 |
| E2E median (ms)           |        665.9 | **267.0** |  370.6 |
| Throughput median (tok/s) |          7.7 |  **18.4** |   12.4 |
| Correctness               |          99% |       99% |    99% |
