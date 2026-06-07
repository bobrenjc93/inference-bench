# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 AM PT, Jun 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     426.3s (7.1m) | `73aa664` |
| vllm         |   1332.6s (22.2m) | `228bcc4` |
| sglang       | **178.4s (3.0m)** | `a07d813` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        291.3 |     153.8 | **140.5** |
| TPOT median (ms)          |     **51.5** |      56.2 |      72.3 |
| E2E median (ms)           |        340.9 | **204.4** |     209.0 |
| Throughput median (tok/s) |          3.5 |   **7.0** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        223.5 | **185.7** |  203.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        350.5 | **208.8** |  330.7 |
| Throughput median (tok/s) |          2.9 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        642.5 |     177.0 | **162.6** |
| TPOT median (ms)          |     **59.9** |      64.0 |      95.2 |
| E2E median (ms)           |        712.7 | **240.2** |     255.6 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        391.2 | **58.1** |   78.2 |
| TPOT median (ms)          |         31.6 | **28.8** |   44.7 |
| E2E median (ms)           |        433.7 | **79.7** |  136.4 |
| Throughput median (tok/s) |          3.1 | **15.0** |   10.1 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        590.5 |  **70.4** |   75.3 |
| TPOT median (ms)          |         33.9 |  **15.2** |   24.2 |
| E2E median (ms)           |       1856.2 | **621.4** |  900.8 |
| Throughput median (tok/s) |         19.8 |  **58.0** |   38.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        427.8 | **129.0** |  132.0 |
| TPOT median (ms)          |         35.4 |  **32.8** |   47.3 |
| E2E median (ms)           |        738.8 | **270.9** |  366.5 |
| Throughput median (tok/s) |          6.2 |  **18.2** |   12.5 |
| Correctness               |          98% |       98% |    99% |
