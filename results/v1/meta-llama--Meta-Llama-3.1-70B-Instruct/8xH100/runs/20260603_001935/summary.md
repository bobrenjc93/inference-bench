# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:08 PM PT, Jun 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     365.6s (6.1m) | `1cbe525` |
| vllm         |   1294.7s (21.6m) | `a4ac746` |
| sglang       | **207.0s (3.4m)** | `c55548b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        185.6 |     161.7 | **160.3** |
| TPOT median (ms)          |     **44.7** |      58.5 |      79.7 |
| E2E median (ms)           |        218.9 | **217.9** |     237.3 |
| Throughput median (tok/s) |          6.1 |   **7.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1061.4 |     236.7 | **206.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |       1160.8 | **272.4** |     339.8 |
| Throughput median (tok/s) |          0.9 |   **3.7** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       2506.7 |     184.6 | **168.1** |
| TPOT median (ms)          |        409.2 |  **67.3** |     105.9 |
| E2E median (ms)           |       2984.4 | **245.0** |     275.8 |
| Throughput median (tok/s) |          0.5 |   **5.8** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        754.4 | **61.4** |   86.5 |
| TPOT median (ms)          |     **27.7** |     28.4 |   60.3 |
| E2E median (ms)           |        776.4 | **83.1** |  164.1 |
| Throughput median (tok/s) |          1.6 | **14.8** |    8.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       2824.9 |  **76.5** |   78.3 |
| TPOT median (ms)          |         93.4 |  **14.8** |   23.6 |
| E2E median (ms)           |       5615.2 | **609.3** |  882.2 |
| Throughput median (tok/s) |          5.6 |  **59.3** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1466.6 |     144.2 | **139.9** |
| TPOT median (ms)          |        115.0 |  **33.8** |      53.9 |
| E2E median (ms)           |       2151.1 | **285.5** |     379.9 |
| Throughput median (tok/s) |          2.9 |  **18.1** |      12.3 |
| Correctness               |          99% |       99% |       99% |
