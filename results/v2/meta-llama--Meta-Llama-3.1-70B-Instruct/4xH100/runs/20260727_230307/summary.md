# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `8de08f0de73311c786d6042f0e6ea27006ae5bb5`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`60b3d39cd36c53a698040edbf51406d3febc97a7` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`c19a333944728975df389af508e24a062f44eaa3` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 4:03 PM PT, Jul 27 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **4/4** |  0/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **4/4** |  0/4 |    0/4 |
| tree_of_thought  |      **4/4** |  0/4 |    0/4 |
| long_output      |      **4/4** |  0/4 |    0/4 |
| **Total**        |    **19/20** | 0/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     360.7s (6.0m) | `ed3588b` |
| vllm         | **195.9s (3.3m)** | `60b3d39` |
| sglang       |     261.9s (4.4m) | `c19a333` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **69.6** |  95.8 |   82.5 |
| TPOT median (ms)          |     **52.5** |  57.5 |   80.6 |
| E2E median (ms)           |    **111.3** | 149.0 |  142.7 |
| Throughput median (tok/s) |     **12.8** |   9.3 |    9.2 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **50.8** | 125.8 |  132.5 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **74.2** | 145.7 |  205.2 |
| Throughput median (tok/s) |     **13.5** |   6.9 |    4.9 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **65.7** | 100.2 |   84.7 |
| TPOT median (ms)          |     **49.8** |  64.5 |   80.0 |
| E2E median (ms)           |    **101.2** | 144.0 |  151.5 |
| Throughput median (tok/s) |     **13.7** |   9.2 |    8.9 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **43.2** | 49.6 |   57.3 |
| TPOT median (ms)          |     **27.0** | 34.3 |  124.7 |
| E2E median (ms)           |     **68.9** | 74.4 |  213.9 |
| Throughput median (tok/s) |     **18.3** | 16.5 |    6.5 |
| Correctness               |          97% |  96% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.7** |  63.2 |   56.0 |
| TPOT median (ms)          |     **18.5** |  21.3 |   31.2 |
| E2E median (ms)           |    **709.5** | 813.2 | 1112.2 |
| Throughput median (tok/s) |     **50.6** |  43.6 |   31.4 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **55.8** |  86.9 |   82.6 |
| TPOT median (ms)          |     **29.6** |  35.5 |   63.3 |
| E2E median (ms)           |    **213.0** | 265.3 |  365.1 |
| Throughput median (tok/s) |     **21.8** |  17.1 |   12.2 |
| Correctness               |          98% |   98% |    98% |
