# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     373.5s (6.2m) | `75bbe35` |
| vllm         |   1315.3s (21.9m) | `f87df1d` |
| sglang       | **196.0s (3.3m)** | `aa5213a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        431.8 |     149.3 | **142.2** |
| TPOT median (ms)          |     **55.3** |      56.7 |      73.7 |
| E2E median (ms)           |        481.9 | **194.5** |     212.9 |
| Throughput median (tok/s) |          3.3 |   **7.4** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        255.0 |     221.1 | **207.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        373.1 | **246.1** |     346.3 |
| Throughput median (tok/s) |          2.7 |   **4.1** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        721.2 |     174.5 | **156.7** |
| TPOT median (ms)          |         67.8 |  **63.3** |     108.7 |
| E2E median (ms)           |        791.2 | **230.6** |     263.3 |
| Throughput median (tok/s) |          1.5 |   **6.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        389.7 | **61.4** |   79.1 |
| TPOT median (ms)          |         32.5 | **29.1** |   46.4 |
| E2E median (ms)           |        422.5 | **82.8** |  137.6 |
| Throughput median (tok/s) |          3.1 | **14.5** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        546.5 |  **68.7** |   74.9 |
| TPOT median (ms)          |         31.1 |  **15.1** |   23.9 |
| E2E median (ms)           |       1717.6 | **612.0** |  905.7 |
| Throughput median (tok/s) |         22.5 |  **59.2** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        468.8 |     135.0 | **132.0** |
| TPOT median (ms)          |         37.3 |  **32.8** |      50.6 |
| E2E median (ms)           |        757.3 | **273.2** |     373.2 |
| Throughput median (tok/s) |          6.6 |  **18.2** |      12.6 |
| Correctness               |          98% |       98% |       99% |
