# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:04 AM PT, May 19 2026

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

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     347.6s (5.8m) | `9f91b40` |
| vllm         |   1190.9s (19.8m) | `42b4f1f` |
| sglang       | **194.2s (3.2m)** | `4c0ce03` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        249.8 |    158.7 | **142.3** |
| TPOT median (ms)          |        149.5 | **57.3** |      72.9 |
| E2E median (ms)           |        352.7 |    217.0 | **208.4** |
| Throughput median (tok/s) |          4.2 |  **7.0** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        268.2 | **182.3** |  196.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        301.5 | **206.7** |  325.6 |
| Throughput median (tok/s) |          3.3 |   **4.8** |    3.1 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        549.2 |     168.7 | **155.1** |
| TPOT median (ms)          |        169.5 |  **54.3** |      99.6 |
| E2E median (ms)           |        634.2 | **217.9** |     247.5 |
| Throughput median (tok/s) |          2.0 |   **6.4** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        361.1 | **57.4** |   76.3 |
| TPOT median (ms)          |        130.5 | **26.7** |   53.6 |
| E2E median (ms)           |        471.3 | **77.8** |  146.2 |
| Throughput median (tok/s) |          2.9 | **15.9** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        754.9 |      67.5 | **65.9** |
| TPOT median (ms)          |         15.9 |  **15.0** |     22.2 |
| E2E median (ms)           |       1431.1 | **598.9** |    820.3 |
| Throughput median (tok/s) |         24.4 |  **59.5** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        436.6 | **126.9** |  127.3 |
| TPOT median (ms)          |         93.1 |  **30.7** |   49.7 |
| E2E median (ms)           |        638.2 | **263.6** |  349.6 |
| Throughput median (tok/s) |          7.4 |  **18.7** |   13.3 |
| Correctness               |          98% |       99% |    99% |
