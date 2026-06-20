# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     392.1s (6.5m) | `00fa07d` |
| vllm         |     507.7s (8.5m) | `93bad11` |
| sglang       | **266.7s (4.4m)** | `45d203f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        306.2 | **138.3** |  155.7 |
| TPOT median (ms)          |         55.5 |  **42.2** |   78.4 |
| E2E median (ms)           |        357.1 | **173.7** |  231.2 |
| Throughput median (tok/s) |          3.6 |   **8.0** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        274.4 |     212.4 | **208.4** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        382.7 | **239.1** |     350.8 |
| Throughput median (tok/s) |          2.6 |   **4.2** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        704.6 | **161.1** |  171.5 |
| TPOT median (ms)          |     **57.1** |      57.5 |  102.2 |
| E2E median (ms)           |        761.4 | **206.0** |  280.5 |
| Throughput median (tok/s) |          1.7 |   **6.6** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        248.4 | **58.3** |   81.1 |
| TPOT median (ms)          |         35.9 | **29.0** |   48.7 |
| E2E median (ms)           |        288.2 | **80.7** |  142.1 |
| Throughput median (tok/s) |          5.0 | **15.3** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        353.2 |      68.7 | **67.2** |
| TPOT median (ms)          |         21.6 |  **15.0** |     22.4 |
| E2E median (ms)           |       1071.3 | **603.8** |    834.9 |
| Throughput median (tok/s) |         31.6 |  **59.5** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        377.4 | **127.8** |  136.8 |
| TPOT median (ms)          |         34.0 |  **28.7** |   50.3 |
| E2E median (ms)           |        572.1 | **260.6** |  367.9 |
| Throughput median (tok/s) |          8.9 |  **18.7** |   12.9 |
| Correctness               |          99% |       98% |    99% |
