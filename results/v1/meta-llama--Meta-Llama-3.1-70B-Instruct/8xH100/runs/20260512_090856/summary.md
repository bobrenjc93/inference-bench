# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:06 AM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     357.8s (6.0m) | `b468ebb` |
| vllm         |   1014.9s (16.9m) | `ef34592` |
| sglang       | **183.4s (3.1m)** | `1efe9e2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        430.0 |    164.5 | **136.8** |
| TPOT median (ms)          |        472.2 | **56.1** |      73.9 |
| E2E median (ms)           |        827.4 |    220.5 | **204.2** |
| Throughput median (tok/s) |          1.6 |  **6.5** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        409.3 |     208.8 | **208.2** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        499.5 | **276.5** |     348.6 |
| Throughput median (tok/s) |          2.0 |   **3.6** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        709.6 |     163.2 | **162.7** |
| TPOT median (ms)          |        567.9 |  **51.8** |      98.6 |
| E2E median (ms)           |       1346.5 | **209.4** |     260.7 |
| Throughput median (tok/s) |          1.1 |   **6.4** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        409.8 | **59.1** |   77.6 |
| TPOT median (ms)          |        426.1 | **28.0** |   50.6 |
| E2E median (ms)           |        750.8 | **79.4** |  133.5 |
| Throughput median (tok/s) |          1.9 | **15.5** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        806.3 |      80.6 | **65.3** |
| TPOT median (ms)          |         29.0 |  **15.0** |     22.4 |
| E2E median (ms)           |       2061.6 | **633.6** |    835.9 |
| Throughput median (tok/s) |         16.5 |  **57.5** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        553.0 |     135.2 | **130.1** |
| TPOT median (ms)          |        299.1 |  **30.2** |      49.1 |
| E2E median (ms)           |       1097.1 | **283.9** |     356.6 |
| Throughput median (tok/s) |          4.6 |  **17.9** |      13.2 |
| Correctness               |          99% |       98% |       99% |
