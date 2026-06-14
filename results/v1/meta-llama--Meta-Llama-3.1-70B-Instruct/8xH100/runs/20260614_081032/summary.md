# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     312.0s (5.2m) | `a102128` |
| vllm         |   1300.2s (21.7m) | `e2bf2b3` |
| sglang       | **209.0s (3.5m)** | `8c334e2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        298.4 |     151.8 | **144.5** |
| TPOT median (ms)          |         87.2 |  **51.0** |      74.5 |
| E2E median (ms)           |        375.6 | **194.6** |     215.8 |
| Throughput median (tok/s) |          3.4 |   **7.2** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        310.0 | **178.1** |  210.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        427.8 | **199.0** |  354.3 |
| Throughput median (tok/s) |          2.3 |   **5.0** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        699.9 |     172.6 | **162.4** |
| TPOT median (ms)          |         64.0 |  **61.6** |     104.2 |
| E2E median (ms)           |        778.8 | **223.6** |     262.9 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        268.4 | **59.3** |   78.8 |
| TPOT median (ms)          |         48.8 | **28.6** |   45.7 |
| E2E median (ms)           |        317.4 | **80.9** |  129.1 |
| Throughput median (tok/s) |          4.5 | **14.8** |   10.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        363.2 |      67.9 | **64.5** |
| TPOT median (ms)          |         21.5 |  **15.1** |     22.6 |
| E2E median (ms)           |       1129.6 | **603.9** |    824.4 |
| Throughput median (tok/s) |         31.5 |  **59.2** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        388.0 | **125.9** |  132.2 |
| TPOT median (ms)          |         44.3 |  **31.3** |   49.4 |
| E2E median (ms)           |        605.8 | **260.4** |  357.3 |
| Throughput median (tok/s) |          8.7 |  **18.4** |   13.3 |
| Correctness               |          98% |       99% |    99% |
