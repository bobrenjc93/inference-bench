# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 20 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **3/4** |  1/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **3/4** |  1/4 |    0/4 |
| tree_of_thought  |      **4/4** |  0/4 |    0/4 |
| long_output      |      **4/4** |  0/4 |    0/4 |
| **Total**        |    **17/20** | 2/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     219.4s (3.7m) | `5badf18` |
| vllm         | **216.9s (3.6m)** | `97a9800` |
| sglang       |     245.5s (4.1m) | `d6ef688` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **51.0** |     78.7 |   90.5 |
| TPOT median (ms)          |         47.5 | **37.6** |   67.5 |
| E2E median (ms)           |     **89.5** |    107.7 |  150.9 |
| Throughput median (tok/s) |     **14.2** |     12.5 |    8.9 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **32.0** | 72.9 |  160.9 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **47.9** | 90.9 |  256.3 |
| Throughput median (tok/s) |     **20.9** | 11.0 |    3.9 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **42.2** |     84.8 |  106.1 |
| TPOT median (ms)          |         37.6 | **34.6** |   90.8 |
| E2E median (ms)           |     **76.1** |    109.4 |  181.1 |
| Throughput median (tok/s) |     **17.4** |     12.1 |    7.0 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **24.1** | 37.7 |   63.1 |
| TPOT median (ms)          |     **16.3** | 24.5 |  393.1 |
| E2E median (ms)           |     **36.3** | 56.6 |  495.7 |
| Throughput median (tok/s) |     **37.8** | 22.7 |    2.9 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **46.0** |  49.6 |   57.6 |
| TPOT median (ms)          |     **14.0** |  15.4 |   26.8 |
| E2E median (ms)           |    **531.1** | 578.8 | 1050.7 |
| Throughput median (tok/s) |     **65.5** |  60.5 |   35.9 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **39.1** |     64.7 |   95.6 |
| TPOT median (ms)          |         23.1 | **22.4** |  115.6 |
| E2E median (ms)           |    **156.2** |    188.7 |  426.9 |
| Throughput median (tok/s) |     **31.2** |     23.8 |   11.7 |
| Correctness               |          98% |      98% |    99% |
