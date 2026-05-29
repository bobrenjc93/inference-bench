# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 AM PT, May 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     369.5s (6.2m) | `6ead340` |
| vllm         |   1279.0s (21.3m) | `0585b5b` |
| sglang       | **197.4s (3.3m)** | `ec075d8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        278.3 |    177.0 | **144.4** |
| TPOT median (ms)          |         70.2 | **63.1** |      78.7 |
| E2E median (ms)           |        345.2 |    239.2 | **217.5** |
| Throughput median (tok/s) |          3.5 |  **6.2** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.4 | **203.2** |  204.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        340.7 | **226.2** |  339.6 |
| Throughput median (tok/s) |          2.9 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        718.9 |     169.5 | **168.7** |
| TPOT median (ms)          |         57.6 |  **56.0** |     116.4 |
| E2E median (ms)           |        778.8 | **221.3** |     278.8 |
| Throughput median (tok/s) |          1.9 |   **6.4** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        178.4 | **60.1** |   81.4 |
| TPOT median (ms)          |         31.5 | **27.5** |   44.3 |
| E2E median (ms)           |        206.2 | **81.0** |  142.4 |
| Throughput median (tok/s) |          6.1 | **15.2** |    9.9 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        811.7 |  **68.7** |   80.6 |
| TPOT median (ms)          |     **14.6** |      15.1 |   24.1 |
| E2E median (ms)           |       1316.4 | **602.3** |  897.3 |
| Throughput median (tok/s) |         26.1 |  **58.9** |   38.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        455.5 | **135.7** |  136.0 |
| TPOT median (ms)          |         34.8 |  **32.3** |   52.7 |
| E2E median (ms)           |        597.5 | **274.0** |  375.1 |
| Throughput median (tok/s) |          8.1 |  **18.2** |   12.3 |
| Correctness               |          98% |       98% |    99% |
