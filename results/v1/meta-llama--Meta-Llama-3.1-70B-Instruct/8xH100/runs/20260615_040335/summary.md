# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jun 14 2026

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
| torchinferno |     355.8s (5.9m) | `377bf47` |
| vllm         |     477.8s (8.0m) | `e3e3cd5` |
| sglang       | **255.4s (4.3m)** | `bf38a0b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        453.2 |     165.6 | **148.1** |
| TPOT median (ms)          |         52.2 |  **51.3** |      72.6 |
| E2E median (ms)           |        512.1 | **218.7** |     220.5 |
| Throughput median (tok/s) |          3.0 |   **7.0** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        272.4 | **183.0** |  202.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        384.7 | **240.8** |  341.0 |
| Throughput median (tok/s) |          2.6 |   **4.2** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        680.8 |     168.9 | **162.9** |
| TPOT median (ms)          |         61.7 |  **55.3** |     100.8 |
| E2E median (ms)           |        757.4 | **216.4** |     253.1 |
| Throughput median (tok/s) |          1.8 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        192.4 | **63.1** |   81.8 |
| TPOT median (ms)          |         33.4 | **28.4** |   58.2 |
| E2E median (ms)           |        224.0 | **85.8** |  152.3 |
| Throughput median (tok/s) |          5.7 | **14.3** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        352.4 |      74.7 | **68.0** |
| TPOT median (ms)          |         22.2 |  **14.8** |     21.6 |
| E2E median (ms)           |       1132.3 | **614.5** |    813.5 |
| Throughput median (tok/s) |         30.1 |  **59.5** |     43.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        390.3 | **131.1** |  132.6 |
| TPOT median (ms)          |         33.9 |  **29.9** |   50.7 |
| E2E median (ms)           |        602.1 | **275.2** |  356.0 |
| Throughput median (tok/s) |          8.6 |  **18.3** |   13.2 |
| Correctness               |          98% |       98% |    99% |
