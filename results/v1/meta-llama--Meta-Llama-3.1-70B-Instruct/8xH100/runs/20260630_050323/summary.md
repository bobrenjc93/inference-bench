# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 PM PT, Jun 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    697.6s (11.6m) | `7cbb5fe` |
| vllm         |    627.8s (10.5m) | `e45c8a9` |
| sglang       | **355.5s (5.9m)** | `dad0120` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        163.4 | **141.4** |  149.3 |
| TPOT median (ms)          |     **45.5** |      47.2 |   71.4 |
| E2E median (ms)           |        202.8 | **179.5** |  221.0 |
| Throughput median (tok/s) |          5.8 |   **7.9** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        231.1 | **192.6** |  214.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        247.6 | **216.2** |  347.5 |
| Throughput median (tok/s) |          4.0 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        307.6 | **163.8** |  173.1 |
| TPOT median (ms)          |         61.1 |  **55.3** |  108.0 |
| E2E median (ms)           |        370.9 | **207.7** |  275.8 |
| Throughput median (tok/s) |          3.5 |   **6.6** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        214.0 | **65.1** |   82.1 |
| TPOT median (ms)          |         57.0 | **32.8** |   60.1 |
| E2E median (ms)           |        259.2 | **90.8** |  154.6 |
| Throughput median (tok/s) |          5.6 | **13.5** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        284.0 |      70.3 | **69.3** |
| TPOT median (ms)          |         22.9 |  **14.8** |     22.7 |
| E2E median (ms)           |       1082.8 | **612.9** |    865.4 |
| Throughput median (tok/s) |         33.4 |  **59.8** |     40.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        240.0 | **126.6** |  137.6 |
| TPOT median (ms)          |         37.3 |  **30.0** |   52.4 |
| E2E median (ms)           |        432.7 | **261.4** |  372.8 |
| Throughput median (tok/s) |         10.4 |  **18.5** |   12.7 |
| Correctness               |          99% |       98% |    98% |
