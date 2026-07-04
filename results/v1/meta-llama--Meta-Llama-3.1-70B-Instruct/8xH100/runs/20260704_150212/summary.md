# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |      **2/4** |       1/4 |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **3/4** |     1/4 |
| **Total**        |         3/20 | **12/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **45.9s (0.8m)** | `390fed4` |
| vllm         |    261.4s (4.4m) | `0cd6f76` |
| sglang       |    148.8s (2.5m) | `6dd0cef` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        170.2 |   169.4 | **146.4** |
| TPOT median (ms)          |     **49.1** |    59.8 |      77.7 |
| E2E median (ms)           |        225.4 |   222.2 | **219.8** |
| Throughput median (tok/s) |          5.6 | **6.4** |       5.3 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        170.4 | **157.3** |  221.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |    **179.3** |     274.0 |  374.5 |
| Throughput median (tok/s) |      **5.6** |       3.6 |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        346.0 |     176.7 | **160.5** |
| TPOT median (ms)          |         61.3 |  **51.2** |     101.1 |
| E2E median (ms)           |        402.4 | **223.7** |     266.3 |
| Throughput median (tok/s) |          3.6 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        130.6 | **66.1** |   73.9 |
| TPOT median (ms)          |         33.0 | **30.6** |   82.2 |
| E2E median (ms)           |        156.0 | **89.2** |  154.8 |
| Throughput median (tok/s) |          8.4 | **13.3** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        268.2 |      84.6 | **72.3** |
| TPOT median (ms)          |         20.2 |  **14.9** |     22.4 |
| E2E median (ms)           |        968.3 | **636.6** |    827.1 |
| Throughput median (tok/s) |         37.2 |  **57.8** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        217.1 | **130.8** |  135.0 |
| TPOT median (ms)          |         32.7 |  **31.3** |   56.7 |
| E2E median (ms)           |        386.3 | **289.1** |  368.5 |
| Throughput median (tok/s) |         12.1 |  **17.4** |   12.8 |
| Correctness               |          99% |       98% |    99% |
