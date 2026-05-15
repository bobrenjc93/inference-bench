# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:01 AM PT, May 15 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **86.5s (1.4m)** | `d648af4` |
| vllm         |  1259.9s (21.0m) | `75fd68c` |
| sglang       |    172.7s (2.9m) | `0c19540` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        339.4 |     168.0 | **159.9** |
| TPOT median (ms)          |        171.5 |  **56.6** |      76.3 |
| E2E median (ms)           |        442.5 | **219.9** |     233.2 |
| Throughput median (tok/s) |          3.2 |   **6.5** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        327.0 | **194.3** |  220.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        408.1 | **223.1** |  352.5 |
| Throughput median (tok/s) |          2.5 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1060.0 |     192.9 | **172.3** |
| TPOT median (ms)          |        145.2 |  **57.8** |     108.6 |
| E2E median (ms)           |       1135.6 | **248.2** |     287.5 |
| Throughput median (tok/s) |          1.2 |   **5.8** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        417.6 | **61.8** |   80.3 |
| TPOT median (ms)          |        142.5 | **27.6** |   50.2 |
| E2E median (ms)           |        520.2 | **83.1** |  136.0 |
| Throughput median (tok/s) |          2.6 | **14.8** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1130.9 |      77.0 | **76.0** |
| TPOT median (ms)          |         17.3 |  **15.0** |     22.1 |
| E2E median (ms)           |       1805.0 | **622.7** |    810.3 |
| Throughput median (tok/s) |         17.4 |  **57.8** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        655.0 | **138.8** |  141.9 |
| TPOT median (ms)          |         95.3 |  **31.4** |   51.4 |
| E2E median (ms)           |        862.3 | **279.4** |  363.9 |
| Throughput median (tok/s) |          5.4 |  **17.9** |   12.8 |
| Correctness               |          99% |       99% |    99% |
