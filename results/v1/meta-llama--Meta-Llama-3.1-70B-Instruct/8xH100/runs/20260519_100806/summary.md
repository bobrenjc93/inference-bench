# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, May 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     305.8s (5.1m) | `9f91b40` |
| vllm         |   1259.1s (21.0m) | `ef54a4d` |
| sglang       | **186.3s (3.1m)** | `45a85ef` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        279.6 |    160.2 | **138.2** |
| TPOT median (ms)          |        154.3 | **59.6** |      77.3 |
| E2E median (ms)           |        376.6 |    220.7 | **207.5** |
| Throughput median (tok/s) |          4.1 |  **6.5** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        274.2 | **178.3** |  203.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        303.3 | **203.3** |  342.3 |
| Throughput median (tok/s) |          3.3 |   **4.9** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        533.3 |     177.4 | **152.2** |
| TPOT median (ms)          |        131.3 |  **44.8** |     103.5 |
| E2E median (ms)           |        632.3 | **217.0** |     252.8 |
| Throughput median (tok/s) |          2.1 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        337.0 | **58.0** |   75.9 |
| TPOT median (ms)          |        129.2 | **27.8** |   56.9 |
| E2E median (ms)           |        439.4 | **77.8** |  147.6 |
| Throughput median (tok/s) |          3.1 | **15.5** |    9.7 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        671.5 |      66.0 | **64.5** |
| TPOT median (ms)          |         15.5 |  **15.0** |     22.5 |
| E2E median (ms)           |       1205.8 | **597.3** |    829.7 |
| Throughput median (tok/s) |         25.8 |  **59.9** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        419.1 |     128.0 | **126.8** |
| TPOT median (ms)          |         86.1 |  **29.5** |      52.0 |
| E2E median (ms)           |        591.5 | **263.2** |     356.0 |
| Throughput median (tok/s) |          7.7 |  **18.6** |      13.1 |
| Correctness               |          98% |       99% |       98% |
