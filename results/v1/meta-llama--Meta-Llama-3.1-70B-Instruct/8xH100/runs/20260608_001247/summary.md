# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 PM PT, Jun 7 2026

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
| torchinferno |     354.2s (5.9m) | `d21d686` |
| vllm         |   1314.0s (21.9m) | `4dcd10e` |
| sglang       | **188.8s (3.1m)** | `f68c796` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        372.2 |     156.2 | **150.2** |
| TPOT median (ms)          |         94.2 |  **55.1** |      70.6 |
| E2E median (ms)           |        444.5 | **210.0** |     216.7 |
| Throughput median (tok/s) |          3.1 |   **7.2** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        391.7 | **194.0** |  207.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        550.2 | **214.5** |  340.3 |
| Throughput median (tok/s) |          1.8 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        674.6 |     170.0 | **164.1** |
| TPOT median (ms)          |         64.6 |  **52.8** |     101.1 |
| E2E median (ms)           |        739.6 | **223.0** |     258.6 |
| Throughput median (tok/s) |          1.7 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        507.1 | **60.7** |   82.0 |
| TPOT median (ms)          |         61.4 | **28.4** |   48.3 |
| E2E median (ms)           |        561.0 | **82.7** |  146.4 |
| Throughput median (tok/s) |          2.4 | **14.8** |    9.7 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        493.8 |  **68.7** |   80.0 |
| TPOT median (ms)          |         21.8 |  **14.8** |   23.2 |
| E2E median (ms)           |       1316.9 | **600.4** |  879.9 |
| Throughput median (tok/s) |         28.0 |  **59.4** |   40.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        487.9 | **129.9** |  136.8 |
| TPOT median (ms)          |         48.4 |  **30.2** |   48.7 |
| E2E median (ms)           |        722.4 | **266.1** |  368.4 |
| Throughput median (tok/s) |          7.4 |  **18.5** |   12.7 |
| Correctness               |          99% |       98% |    99% |
