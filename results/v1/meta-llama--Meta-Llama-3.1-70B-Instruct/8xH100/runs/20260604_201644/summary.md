# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:01 PM PT, Jun 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **2/4** |     1/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         1/20 | **14/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     418.5s (7.0m) | `0f61f09` |
| vllm         |   1315.1s (21.9m) | `a55fccf` |
| sglang       | **195.6s (3.3m)** | `69623f4` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        265.3 |   169.1 | **146.2** |
| TPOT median (ms)          |     **48.3** |    60.0 |      72.8 |
| E2E median (ms)           |        313.6 |   222.2 | **217.6** |
| Throughput median (tok/s) |          4.3 | **6.7** |       5.5 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        252.2 |     219.3 | **218.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        352.7 | **246.1** |     362.1 |
| Throughput median (tok/s) |          2.8 |   **4.1** |       2.8 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        861.5 |     169.2 | **164.6** |
| TPOT median (ms)          |        111.2 |  **59.2** |     107.2 |
| E2E median (ms)           |        981.5 | **222.7** |     266.4 |
| Throughput median (tok/s) |          1.3 |   **6.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        334.3 | **61.6** |   79.1 |
| TPOT median (ms)          |         32.6 | **28.5** |   58.0 |
| E2E median (ms)           |        363.6 | **83.6** |  150.4 |
| Throughput median (tok/s) |          3.4 | **14.7** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        469.2 |  **73.9** |   81.5 |
| TPOT median (ms)          |         28.5 |  **14.7** |   23.1 |
| E2E median (ms)           |       1500.9 | **608.1** |  887.3 |
| Throughput median (tok/s) |         24.2 |  **59.5** |   40.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        436.5 |     138.6 | **138.0** |
| TPOT median (ms)          |         44.1 |  **32.5** |      52.2 |
| E2E median (ms)           |        702.5 | **276.5** |     376.8 |
| Throughput median (tok/s) |          7.2 |  **18.2** |      12.6 |
| Correctness               |          99% |       99% |       99% |
