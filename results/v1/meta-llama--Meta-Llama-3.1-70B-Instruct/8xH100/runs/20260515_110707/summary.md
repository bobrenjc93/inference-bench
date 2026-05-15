# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:07 AM PT, May 15 2026

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
| torchinferno |     343.5s (5.7m) | `d648af4` |
| vllm         |   1110.5s (18.5m) | `1dc3fe0` |
| sglang       | **160.9s (2.7m)** | `3117415` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        301.2 |    163.7 | **137.9** |
| TPOT median (ms)          |        158.8 | **57.4** |      77.5 |
| E2E median (ms)           |        393.1 |    213.8 | **208.6** |
| Throughput median (tok/s) |          3.6 |  **6.8** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        297.6 |     208.1 | **200.3** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        326.4 | **237.8** |     346.4 |
| Throughput median (tok/s) |          3.1 |   **4.2** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        564.0 |     165.3 | **156.3** |
| TPOT median (ms)          |        118.7 |  **57.7** |     102.0 |
| E2E median (ms)           |        650.4 | **215.5** |     254.3 |
| Throughput median (tok/s) |          2.2 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        344.5 | **58.8** |   72.1 |
| TPOT median (ms)          |        138.4 | **26.6** |   63.2 |
| E2E median (ms)           |        440.8 | **79.5** |  155.1 |
| Throughput median (tok/s) |          3.4 | **15.6** |    9.6 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        523.3 |      68.5 | **66.1** |
| TPOT median (ms)          |         15.4 |  **15.1** |     22.0 |
| E2E median (ms)           |       1191.5 | **614.9** |    827.5 |
| Throughput median (tok/s) |         27.4 |  **59.1** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        406.1 |     132.9 | **126.6** |
| TPOT median (ms)          |         86.3 |  **31.3** |      52.9 |
| E2E median (ms)           |        600.4 | **272.3** |     358.4 |
| Throughput median (tok/s) |          7.9 |  **18.4** |      13.2 |
| Correctness               |          99% |       98% |       99% |
