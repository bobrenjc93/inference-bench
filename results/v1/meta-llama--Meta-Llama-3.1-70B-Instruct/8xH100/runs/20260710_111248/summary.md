# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:12 AM PT, Jul 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **14/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **38.1s (0.6m)** | `a4d92f0` |
| vllm         |    283.0s (4.7m) | `68ea76e` |
| sglang       |    215.4s (3.6m) | `7045e0f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        152.1 |      77.0 | **75.4** |
| TPOT median (ms)          |     **31.4** |      36.2 |     65.5 |
| E2E median (ms)           |        176.9 | **107.3** |    132.5 |
| Throughput median (tok/s) |          6.4 |  **12.6** |     10.6 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **53.7** | 80.0 |  118.2 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **54.1** | 97.1 |  195.1 |
| Throughput median (tok/s) |     **18.5** | 10.3 |    5.1 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        469.5 | **70.4** |   85.7 |
| TPOT median (ms)          |        124.5 | **35.9** |   74.9 |
| E2E median (ms)           |        569.0 | **96.8** |  153.8 |
| Throughput median (tok/s) |          2.1 | **13.8** |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        126.7 | **35.2** |   48.4 |
| TPOT median (ms)          |         84.4 | **22.9** |  400.7 |
| E2E median (ms)           |        166.2 | **53.3** |  441.0 |
| Throughput median (tok/s) |          8.4 | **24.7** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        587.9 |  **46.4** |   48.7 |
| TPOT median (ms)          |         65.3 |  **15.2** |   23.7 |
| E2E median (ms)           |       2915.1 | **581.0** |  898.0 |
| Throughput median (tok/s) |         12.4 |  **61.5** |   40.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        278.0 |  **61.8** |   75.3 |
| TPOT median (ms)          |         61.1 |  **22.0** |  113.0 |
| E2E median (ms)           |        776.3 | **187.1** |  364.1 |
| Throughput median (tok/s) |          9.6 |  **24.6** |   13.7 |
| Correctness               |          99% |       99% |    99% |
