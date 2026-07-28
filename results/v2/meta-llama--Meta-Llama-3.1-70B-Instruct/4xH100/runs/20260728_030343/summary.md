# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `92149a4fd25b6d68f13e7757d2fe56b56efe6a57`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`52c3c4a42fd13b62ba985b9ceb9b9969964ee83e` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`ec4a7fa2b78841de5c28f57d272c7f9404ec1ad8` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:03 PM PT, Jul 27 2026

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
| torchinferno |     420.3s (7.0m) | `ed3588b` |
| vllm         | **223.5s (3.7m)** | `52c3c4a` |
| sglang       |     242.6s (4.0m) | `ec4a7fa` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.5** |  95.9 |   85.3 |
| TPOT median (ms)          |     **52.0** |  58.7 |   74.2 |
| E2E median (ms)           |    **110.6** | 146.6 |  143.4 |
| Throughput median (tok/s) |     **12.9** |   9.4 |    9.1 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **51.6** | 119.5 |  136.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **73.2** | 140.8 |  213.7 |
| Throughput median (tok/s) |     **13.7** |   7.1 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **66.8** | 101.7 |   87.5 |
| TPOT median (ms)          |     **49.5** |  63.4 |   80.3 |
| E2E median (ms)           |    **103.6** | 141.6 |  155.5 |
| Throughput median (tok/s) |     **13.4** |   9.5 |    8.7 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.9** | 49.5 |   57.9 |
| TPOT median (ms)          |     **26.7** | 34.2 |  121.1 |
| E2E median (ms)           |     **69.1** | 73.9 |  208.2 |
| Throughput median (tok/s) |     **19.1** | 16.4 |    6.8 |
| Correctness               |          97% |  96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **50.6** |  62.6 |   56.0 |
| TPOT median (ms)          |     **18.5** |  21.2 |   31.4 |
| E2E median (ms)           |    **716.3** | 812.9 | 1101.6 |
| Throughput median (tok/s) |     **50.6** |  43.7 |   31.2 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.5** |  85.8 |   84.6 |
| TPOT median (ms)          |     **29.3** |  35.5 |   61.4 |
| E2E median (ms)           |    **214.6** | 263.2 |  364.5 |
| Throughput median (tok/s) |     **21.9** |  17.2 |   12.1 |
| Correctness               |          98% |   98% |    98% |
