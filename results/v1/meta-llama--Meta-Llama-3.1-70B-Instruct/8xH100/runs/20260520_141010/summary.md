# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:08 AM PT, May 20 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     275.9s (4.6m) | `9f91b40` |
| vllm         |   1154.1s (19.2m) | `0a50874` |
| sglang       | **205.8s (3.4m)** | `55ba03d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        286.4 |    167.5 | **135.1** |
| TPOT median (ms)          |        148.5 | **55.3** |      76.5 |
| E2E median (ms)           |        384.8 |    223.3 | **206.8** |
| Throughput median (tok/s) |          4.1 |  **6.6** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        285.2 |     212.0 | **186.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        307.5 | **292.8** |     323.6 |
| Throughput median (tok/s) |          3.3 |   **3.4** |       3.1 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        541.6 |     173.8 | **158.2** |
| TPOT median (ms)          |        128.2 |  **60.5** |      91.9 |
| E2E median (ms)           |        635.2 | **227.0** |     256.7 |
| Throughput median (tok/s) |          2.1 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        313.7 | **58.0** |   75.3 |
| TPOT median (ms)          |        127.9 | **26.7** |   57.5 |
| E2E median (ms)           |        409.7 | **78.0** |  150.7 |
| Throughput median (tok/s) |          3.4 | **15.7** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        739.3 |      77.8 | **65.8** |
| TPOT median (ms)          |         16.0 |  **14.9** |     22.2 |
| E2E median (ms)           |       1494.8 | **637.2** |    829.8 |
| Throughput median (tok/s) |         22.7 |  **57.2** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        433.2 |     137.8 | **124.3** |
| TPOT median (ms)          |         84.1 |  **31.5** |      49.6 |
| E2E median (ms)           |        646.4 | **291.7** |     353.5 |
| Throughput median (tok/s) |          7.1 |  **17.8** |      13.2 |
| Correctness               |          99% |       98% |       99% |
