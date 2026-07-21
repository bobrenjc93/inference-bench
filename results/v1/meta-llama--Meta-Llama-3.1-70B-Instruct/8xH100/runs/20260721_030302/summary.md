# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, Jul 20 2026

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
| torchinferno |     490.1s (8.2m) | `5badf18` |
| vllm         |     247.5s (4.1m) | `6bcda97` |
| sglang       | **216.3s (3.6m)** | `d6ef688` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **50.9** |     78.1 |  105.9 |
| TPOT median (ms)          |         47.7 | **40.0** |   64.9 |
| E2E median (ms)           |     **88.8** |    106.0 |  160.7 |
| Throughput median (tok/s) |     **14.2** |     12.2 |    8.2 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **32.1** | 69.7 |  158.8 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **48.1** | 87.0 |  248.7 |
| Throughput median (tok/s) |     **20.8** | 11.5 |    4.0 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **42.5** |     86.7 |   90.0 |
| TPOT median (ms)          |         38.2 | **34.0** |   80.8 |
| E2E median (ms)           |     **76.2** |    116.2 |  156.1 |
| Throughput median (tok/s) |     **17.4** |     11.4 |    8.6 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **24.6** | 35.3 |   68.2 |
| TPOT median (ms)          |     **16.3** | 23.4 |  470.1 |
| E2E median (ms)           |     **36.5** | 53.8 |  533.0 |
| Throughput median (tok/s) |     **38.3** | 24.5 |    2.7 |
| Correctness               |          96% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **45.9** |  45.9 |   58.1 |
| TPOT median (ms)          |     **14.1** |  15.4 |   27.5 |
| E2E median (ms)           |    **532.8** | 575.9 | 1050.2 |
| Throughput median (tok/s) |     **65.4** |  61.3 |   35.0 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **39.2** |     63.1 |   96.2 |
| TPOT median (ms)          |         23.3 | **22.6** |  128.7 |
| E2E median (ms)           |    **156.5** |    187.8 |  429.8 |
| Throughput median (tok/s) |     **31.2** |     24.2 |   11.7 |
| Correctness               |          98% |      99% |    99% |
