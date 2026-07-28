# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `3bb98b352356212c2b2ac07ac492b6bbe225e053`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`5ed3faa43ddf075f24482396b634edc33e047a40` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`60d6914f17ec691edb3258601a3c65b1e4f8de61` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 AM PT, Jul 28 2026

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
| torchinferno |     533.1s (8.9m) | `ed3588b` |
| vllm         |     219.7s (3.7m) | `5ed3faa` |
| sglang       | **196.9s (3.3m)** | `60d6914` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.9** |  97.1 |   81.1 |
| TPOT median (ms)          |     **51.8** |  57.4 |   78.0 |
| E2E median (ms)           |    **110.1** | 148.2 |  141.1 |
| Throughput median (tok/s) |     **12.8** |   9.4 |    9.3 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **51.0** | 123.4 |  133.1 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **74.4** | 143.8 |  220.3 |
| Throughput median (tok/s) |     **13.4** |   7.0 |    4.5 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **63.7** | 105.2 |   87.9 |
| TPOT median (ms)          |     **50.1** |  62.4 |   93.8 |
| E2E median (ms)           |     **98.4** | 146.1 |  162.3 |
| Throughput median (tok/s) |     **14.2** |   9.4 |    8.4 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.1** | 49.7 |   57.5 |
| TPOT median (ms)          |     **26.9** | 34.6 |  140.8 |
| E2E median (ms)           |     **68.8** | 74.7 |  207.7 |
| Throughput median (tok/s) |     **19.1** | 16.5 |    6.7 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **51.3** |  63.2 |   56.0 |
| TPOT median (ms)          |     **18.8** |  21.3 |   31.3 |
| E2E median (ms)           |    **712.0** | 813.4 | 1128.8 |
| Throughput median (tok/s) |     **50.0** |  43.6 |   31.0 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **55.8** |  87.7 |   83.1 |
| TPOT median (ms)          |     **29.5** |  35.2 |   68.8 |
| E2E median (ms)           |    **212.7** | 265.2 |  372.1 |
| Throughput median (tok/s) |     **21.9** |  17.2 |   12.0 |
| Correctness               |          98% |   98% |    98% |
