# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:03 AM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     364.4s (6.1m) | `9f91b40` |
| vllm         |   1317.5s (22.0m) | `357fddf` |
| sglang       | **188.9s (3.1m)** | `0b65588` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        284.2 |    166.7 | **134.4** |
| TPOT median (ms)          |        152.9 | **60.1** |      75.1 |
| E2E median (ms)           |        378.7 |    226.0 | **203.1** |
| Throughput median (tok/s) |          3.9 |  **6.6** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        289.2 | **191.5** |  201.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        321.7 | **212.4** |  338.5 |
| Throughput median (tok/s) |          3.1 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        817.6 |     168.6 | **158.4** |
| TPOT median (ms)          |        136.6 |  **56.4** |     104.7 |
| E2E median (ms)           |        904.5 | **218.3** |     261.9 |
| Throughput median (tok/s) |          1.5 |   **6.5** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        361.9 | **58.6** |   77.8 |
| TPOT median (ms)          |        130.3 | **26.3** |   65.2 |
| E2E median (ms)           |        460.2 | **79.2** |  152.3 |
| Throughput median (tok/s) |          2.9 | **15.6** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        706.1 |  **68.5** |   68.9 |
| TPOT median (ms)          |         15.2 |  **15.0** |   22.1 |
| E2E median (ms)           |       1370.6 | **609.6** |  841.9 |
| Throughput median (tok/s) |         27.0 |  **59.0** |   42.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        491.8 |     130.8 | **128.2** |
| TPOT median (ms)          |         87.0 |  **31.6** |      53.4 |
| E2E median (ms)           |        687.1 | **269.1** |     359.5 |
| Throughput median (tok/s) |          7.7 |  **18.5** |      13.2 |
| Correctness               |          99% |       98% |       98% |
