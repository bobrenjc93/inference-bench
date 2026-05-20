# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 PM PT, May 20 2026

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
| torchinferno |     268.4s (4.5m) | `9f91b40` |
| vllm         |   1136.2s (18.9m) | `2a43b40` |
| sglang       | **199.8s (3.3m)** | `dac7876` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        286.8 |    170.8 | **137.7** |
| TPOT median (ms)          |        152.5 | **54.0** |      73.7 |
| E2E median (ms)           |        383.4 |    223.2 | **203.1** |
| Throughput median (tok/s) |          4.0 |  **6.7** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        297.8 | **202.7** |  217.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        337.4 | **223.5** |  348.5 |
| Throughput median (tok/s) |          3.0 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        552.0 |     185.0 | **157.5** |
| TPOT median (ms)          |        136.1 |  **48.4** |     103.9 |
| E2E median (ms)           |        644.0 | **226.3** |     255.5 |
| Throughput median (tok/s) |          2.0 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        344.5 | **58.0** |   80.6 |
| TPOT median (ms)          |        131.7 | **26.9** |   52.7 |
| E2E median (ms)           |        454.6 | **78.4** |  150.8 |
| Throughput median (tok/s) |          2.8 | **15.4** |    9.6 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        757.2 |      73.9 | **65.8** |
| TPOT median (ms)          |         17.0 |  **14.9** |     27.2 |
| E2E median (ms)           |       1420.1 | **621.8** |    951.7 |
| Throughput median (tok/s) |         22.2 |  **58.6** |     35.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        447.7 |     138.1 | **131.8** |
| TPOT median (ms)          |         87.5 |  **28.8** |      51.5 |
| E2E median (ms)           |        647.9 | **274.7** |     381.9 |
| Throughput median (tok/s) |          6.8 |  **18.2** |      11.7 |
| Correctness               |          98% |       99% |       99% |
