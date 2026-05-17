# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:02 AM PT, May 17 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **90.8s (1.5m)** | `13d21ac` |
| vllm         |  1212.3s (20.2m) | `1c8e9c0` |
| sglang       |    177.3s (3.0m) | `89e501c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        285.6 |    171.1 | **147.1** |
| TPOT median (ms)          |        161.3 | **60.4** |      78.0 |
| E2E median (ms)           |        387.8 |    228.4 | **217.7** |
| Throughput median (tok/s) |          3.9 |  **6.5** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        289.1 | **174.8** |  220.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        312.8 | **208.3** |  359.2 |
| Throughput median (tok/s) |          3.2 |   **4.8** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1133.4 |     187.6 | **169.2** |
| TPOT median (ms)          |        120.7 |  **59.6** |     115.1 |
| E2E median (ms)           |       1202.2 | **245.7** |     280.4 |
| Throughput median (tok/s) |          1.1 |   **5.6** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        402.6 | **61.7** |   79.1 |
| TPOT median (ms)          |        136.6 | **28.2** |   49.8 |
| E2E median (ms)           |        516.6 | **83.0** |  139.0 |
| Throughput median (tok/s) |          2.5 | **15.0** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        968.7 |      90.0 | **76.7** |
| TPOT median (ms)          |         15.7 |  **15.0** |     21.7 |
| E2E median (ms)           |       1645.0 | **633.0** |    854.7 |
| Throughput median (tok/s) |         21.7 |  **57.3** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        615.9 | **137.1** |  138.5 |
| TPOT median (ms)          |         86.8 |  **32.6** |   52.9 |
| E2E median (ms)           |        812.9 | **279.7** |  370.2 |
| Throughput median (tok/s) |          6.5 |  **17.8** |   12.9 |
| Correctness               |          99% |       99% |    99% |
