# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, Jun 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    674.5s (11.2m) | `a349eba` |
| vllm         |     490.1s (8.2m) | `311ad68` |
| sglang       | **275.4s (4.6m)** | `06fd2ef` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        160.5 |     145.4 | **141.5** |
| TPOT median (ms)          |     **45.2** |      58.5 |      71.4 |
| E2E median (ms)           |        197.0 | **195.3** |     214.2 |
| Throughput median (tok/s) |          5.9 |   **7.5** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        246.2 | **174.3** |  225.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        264.8 | **197.9** |  376.5 |
| Throughput median (tok/s) |          3.8 |   **5.1** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        324.8 |     167.4 | **161.8** |
| TPOT median (ms)          |         57.7 |  **57.1** |     100.9 |
| E2E median (ms)           |        383.5 | **223.3** |     257.3 |
| Throughput median (tok/s) |          3.4 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        195.7 | **61.8** |   78.8 |
| TPOT median (ms)          |         56.6 | **32.1** |   45.6 |
| E2E median (ms)           |        241.0 | **86.9** |  135.3 |
| Throughput median (tok/s) |          5.8 | **14.3** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        277.2 |      73.0 | **68.6** |
| TPOT median (ms)          |         23.1 |  **14.8** |     22.0 |
| E2E median (ms)           |       1092.5 | **603.9** |    835.1 |
| Throughput median (tok/s) |         33.4 |  **59.4** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        240.9 | **124.4** |  135.3 |
| TPOT median (ms)          |         36.5 |  **32.5** |   48.0 |
| E2E median (ms)           |        435.8 | **261.5** |  363.7 |
| Throughput median (tok/s) |         10.5 |  **18.5** |   13.2 |
| Correctness               |          99% |       98% |    99% |
