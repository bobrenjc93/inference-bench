# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:07 AM PT, Jul 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **38.3s (0.6m)** | `0ba2517` |
| vllm         |    276.8s (4.6m) | `54503ec` |
| sglang       |    201.9s (3.4m) | `32cb89d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        140.7 | **69.3** |   78.1 |
| TPOT median (ms)          |     **32.0** |     36.7 |   64.3 |
| E2E median (ms)           |        166.5 | **96.4** |  130.7 |
| Throughput median (tok/s) |          6.9 | **13.6** |   10.2 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **70.4** | 77.2 |  123.0 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **89.1** | 93.5 |  207.0 |
| Throughput median (tok/s) |     **11.2** | 10.7 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.4 |  **81.0** |   82.5 |
| TPOT median (ms)          |         35.5 |  **35.2** |   73.4 |
| E2E median (ms)           |        218.5 | **108.2** |  140.8 |
| Throughput median (tok/s) |          5.2 |  **12.0** |    9.4 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.2 | **36.1** |   52.3 |
| TPOT median (ms)          |         34.5 | **24.3** |  389.9 |
| E2E median (ms)           |         72.8 | **53.6** |  455.9 |
| Throughput median (tok/s) |         20.1 | **23.8** |    3.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.7 |  **46.4** |   52.2 |
| TPOT median (ms)          |         19.0 |  **15.2** |   24.0 |
| E2E median (ms)           |        845.2 | **569.7** |  918.1 |
| Throughput median (tok/s) |         40.7 |  **61.7** |   40.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        129.5 |  **62.0** |   77.6 |
| TPOT median (ms)          |         24.2 |  **22.3** |  110.3 |
| E2E median (ms)           |        278.4 | **184.3** |  370.5 |
| Throughput median (tok/s) |         16.8 |  **24.4** |   13.6 |
| Correctness               |          99% |       99% |    99% |
