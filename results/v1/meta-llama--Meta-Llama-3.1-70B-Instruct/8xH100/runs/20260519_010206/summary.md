# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:02 PM PT, May 18 2026

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
| torchinferno |     305.4s (5.1m) | `c837893` |
| vllm         |   1104.3s (18.4m) | `239b5ff` |
| sglang       | **171.8s (2.9m)** | `dbac464` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        288.2 |     149.9 | **138.2** |
| TPOT median (ms)          |        148.9 |  **52.6** |      79.1 |
| E2E median (ms)           |        383.9 | **200.8** |     208.4 |
| Throughput median (tok/s) |          4.0 |   **7.1** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        289.3 | **180.4** |  204.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        319.9 | **199.1** |  343.9 |
| Throughput median (tok/s) |          3.1 |   **5.0** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        552.0 |     169.1 | **155.3** |
| TPOT median (ms)          |        125.6 |  **51.8** |      97.9 |
| E2E median (ms)           |        641.7 | **213.8** |     255.9 |
| Throughput median (tok/s) |          2.0 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        311.7 | **57.7** |   73.7 |
| TPOT median (ms)          |        130.6 | **26.5** |   54.4 |
| E2E median (ms)           |        410.8 | **77.5** |  144.1 |
| Throughput median (tok/s) |          3.5 | **15.8** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        764.8 |      68.7 | **64.7** |
| TPOT median (ms)          |         16.8 |  **15.0** |     22.3 |
| E2E median (ms)           |       1431.6 | **624.7** |    827.4 |
| Throughput median (tok/s) |         21.6 |  **59.3** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        441.2 | **125.1** |  127.3 |
| TPOT median (ms)          |         84.4 |  **29.2** |   50.7 |
| E2E median (ms)           |        637.6 | **263.2** |  355.9 |
| Throughput median (tok/s) |          6.9 |  **18.7** |   13.3 |
| Correctness               |          99% |       99% |    99% |
