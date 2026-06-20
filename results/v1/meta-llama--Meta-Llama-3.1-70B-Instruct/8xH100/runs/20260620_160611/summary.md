# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, Jun 20 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **17/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     400.6s (6.7m) | `c7b73ec` |
| vllm         |     561.7s (9.4m) | `d272418` |
| sglang       | **267.1s (4.5m)** | `ff1fc1f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        221.9 | **138.4** |  146.3 |
| TPOT median (ms)          |     **34.4** |      48.5 |   76.9 |
| E2E median (ms)           |        250.8 | **185.3** |  215.7 |
| Throughput median (tok/s) |          5.3 |   **7.6** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        296.0 | **179.1** |  222.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        410.9 | **202.8** |  365.9 |
| Throughput median (tok/s) |          2.4 |   **4.9** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        503.5 | **154.6** |  164.5 |
| TPOT median (ms)          |     **36.8** |      47.5 |  103.8 |
| E2E median (ms)           |        544.3 | **196.1** |  265.9 |
| Throughput median (tok/s) |          2.3 |   **6.8** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        240.9 | **57.3** |   82.5 |
| TPOT median (ms)          |         31.5 | **29.4** |   44.1 |
| E2E median (ms)           |        275.3 | **80.1** |  142.8 |
| Throughput median (tok/s) |          5.3 | **15.0** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        351.2 |  **67.0** |   70.0 |
| TPOT median (ms)          |         22.1 |  **15.1** |   22.5 |
| E2E median (ms)           |       1076.8 | **620.7** |  829.5 |
| Throughput median (tok/s) |         32.1 |  **58.9** |   41.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        322.7 | **119.3** |  137.2 |
| TPOT median (ms)          |     **25.0** |      28.1 |   49.5 |
| E2E median (ms)           |        511.6 | **257.0** |  364.0 |
| Throughput median (tok/s) |          9.5 |  **18.7** |   13.1 |
| Correctness               |          98% |       99% |    98% |
