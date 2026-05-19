# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:02 PM PT, May 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     391.9s (6.5m) | `e5272ff` |
| vllm         |   1136.8s (18.9m) | `239b5ff` |
| sglang       | **193.8s (3.2m)** | `a7b3ced` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        295.3 |    157.9 | **142.4** |
| TPOT median (ms)          |        154.6 | **57.0** |      76.4 |
| E2E median (ms)           |        400.0 |    212.6 | **210.9** |
| Throughput median (tok/s) |          3.6 |  **7.3** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        285.5 | **182.6** |  206.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        310.4 | **204.0** |  346.5 |
| Throughput median (tok/s) |          3.2 |   **4.9** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        540.7 |     171.0 | **155.0** |
| TPOT median (ms)          |        193.1 |  **59.9** |      97.6 |
| E2E median (ms)           |        631.0 | **218.4** |     254.1 |
| Throughput median (tok/s) |          2.0 |   **6.3** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        308.9 | **57.6** |   77.3 |
| TPOT median (ms)          |        131.4 | **27.1** |   60.5 |
| E2E median (ms)           |        412.0 | **77.8** |  150.5 |
| Throughput median (tok/s) |          3.4 | **15.8** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        770.3 |  **69.2** |   69.5 |
| TPOT median (ms)          |         15.8 |  **15.0** |   22.2 |
| E2E median (ms)           |       1429.3 | **617.0** |  832.0 |
| Throughput median (tok/s) |         22.2 |  **59.1** |   42.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        440.1 | **127.7** |  130.1 |
| TPOT median (ms)          |         99.0 |  **31.8** |   51.3 |
| E2E median (ms)           |        636.5 | **266.0** |  358.8 |
| Throughput median (tok/s) |          6.9 |  **18.7** |   13.2 |
| Correctness               |          99% |       99% |    98% |
