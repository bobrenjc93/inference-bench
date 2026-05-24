# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:05 AM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     281.8s (4.7m) | `9f91b40` |
| vllm         |   1290.2s (21.5m) | `1806d1a` |
| sglang       | **201.9s (3.4m)** | `9d50cd9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        292.1 |     152.8 | **143.4** |
| TPOT median (ms)          |        153.3 |  **55.8** |      75.7 |
| E2E median (ms)           |        387.4 | **203.2** |     212.8 |
| Throughput median (tok/s) |          4.0 |   **7.3** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        271.1 |     208.7 | **199.3** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        312.9 | **280.7** |     332.6 |
| Throughput median (tok/s) |          3.2 |   **3.6** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        713.1 |     170.7 | **160.2** |
| TPOT median (ms)          |        131.6 |  **53.9** |      98.4 |
| E2E median (ms)           |        820.9 | **220.1** |     258.5 |
| Throughput median (tok/s) |          1.6 |   **6.4** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        423.2 | **57.9** |   77.3 |
| TPOT median (ms)          |        132.4 | **26.5** |   56.1 |
| E2E median (ms)           |        523.7 | **78.1** |  144.0 |
| Throughput median (tok/s) |          2.7 | **15.6** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        703.4 |      72.2 | **67.2** |
| TPOT median (ms)          |         15.0 |  **14.8** |     22.1 |
| E2E median (ms)           |       1484.5 | **614.1** |    818.7 |
| Throughput median (tok/s) |         26.1 |  **59.1** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        480.6 |     132.4 | **129.5** |
| TPOT median (ms)          |         86.5 |  **30.2** |      50.4 |
| E2E median (ms)           |        705.8 | **279.2** |     353.3 |
| Throughput median (tok/s) |          7.5 |  **18.4** |      13.2 |
| Correctness               |          99% |       99% |       99% |
