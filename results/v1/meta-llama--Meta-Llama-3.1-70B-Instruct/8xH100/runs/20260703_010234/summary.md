# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         5/20 | **11/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **38.6s (0.6m)** | `5e433fe` |
| vllm         |    312.4s (5.2m) | `4c3c64f` |
| sglang       |    166.5s (2.8m) | `05bc3f2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        156.0 |   155.2 | **142.7** |
| TPOT median (ms)          |     **47.4** |    56.3 |      76.4 |
| E2E median (ms)           |    **200.0** |   205.8 |     220.6 |
| Throughput median (tok/s) |          6.3 | **6.9** |       5.5 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **154.3** | 210.2 |  233.4 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **166.0** | 233.5 |  384.4 |
| Throughput median (tok/s) |      **6.0** |   4.3 |    2.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        303.7 |     174.9 | **161.4** |
| TPOT median (ms)          |         60.2 |  **54.0** |     112.2 |
| E2E median (ms)           |        358.6 | **225.6** |     270.8 |
| Throughput median (tok/s) |          3.9 |   **6.0** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        136.6 | **63.4** |   71.4 |
| TPOT median (ms)          |         39.8 | **30.6** |   75.8 |
| E2E median (ms)           |        162.6 | **86.5** |  151.7 |
| Throughput median (tok/s) |          8.0 | **14.1** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        252.5 |      78.4 | **72.5** |
| TPOT median (ms)          |         21.2 |  **15.1** |     21.6 |
| E2E median (ms)           |        966.4 | **621.6** |    805.8 |
| Throughput median (tok/s) |         36.5 |  **57.1** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        200.6 |     136.4 | **136.3** |
| TPOT median (ms)          |         33.7 |  **31.2** |      57.2 |
| E2E median (ms)           |        370.7 | **274.6** |     366.7 |
| Throughput median (tok/s) |         12.1 |  **17.7** |      13.0 |
| Correctness               |          98% |       99% |       99% |
