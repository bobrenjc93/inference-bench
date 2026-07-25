# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `2a2ef31b9cf87c4358f180a203253bdfe8e3ab9e`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100; vllm=NVIDIA H100; sglang=NVIDIA H100
- **Provider source:** torchinferno=`db30bee1ce57016983d4526883e75e516639768a`; vllm=`33ef67e9fb5f3f9c2dfe1aa95e9880d5ecd7b38b` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`69a3c54c7023d1cdcc15e16131a3d6ef128f430d` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:05 AM PT, Jul 25 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **3/4** |  1/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **4/4** |  0/4 |    0/4 |
| tree_of_thought  |      **4/4** |  0/4 |    0/4 |
| long_output      |      **3/4** |  0/4 |    1/4 |
| **Total**        |    **17/20** | 1/20 |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.2s (0.7m)** | `db30bee` |
| vllm         |    206.8s (3.4m) | `33ef67e` |
| sglang       |    144.6s (2.4m) | `69a3c54` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **69.0** |    105.8 |   89.3 |
| TPOT median (ms)          |         66.8 | **64.7** |   93.7 |
| E2E median (ms)           |    **112.8** |    155.1 |  174.5 |
| Throughput median (tok/s) |     **11.0** |      8.8 |    7.2 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **44.1** |  84.7 |  111.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **69.3** | 109.9 |  293.3 |
| Throughput median (tok/s) |     **14.4** |   9.1 |    3.4 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **62.7** | 108.9 |   94.8 |
| TPOT median (ms)          |     **58.4** |  64.8 |  115.9 |
| E2E median (ms)           |    **110.2** | 154.2 |  192.1 |
| Throughput median (tok/s) |     **11.5** |   8.7 |    6.7 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **45.8** | 61.4 |   60.4 |
| TPOT median (ms)          |     **30.3** | 42.8 |  365.4 |
| E2E median (ms)           |     **68.6** | 91.1 |  454.0 |
| Throughput median (tok/s) |     **21.2** | 13.4 |    3.1 |
| Correctness               |          97% |  96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |   vllm |   sglang |
| :------------------------ | -----------: | -----: | -------: |
| TTFT median (ms)          |         73.3 |   77.8 | **67.6** |
| TPOT median (ms)          |     **22.7** |   26.2 |     38.9 |
| E2E median (ms)           |    **873.7** | 1001.3 |   1453.6 |
| Throughput median (tok/s) |     **40.6** |   35.6 |     24.8 |
| Correctness               |         100% |   100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **59.0** |  87.7 |   84.7 |
| TPOT median (ms)          |     **35.6** |  39.7 |  122.8 |
| E2E median (ms)           |    **246.9** | 302.3 |  513.5 |
| Throughput median (tok/s) |     **19.8** |  15.1 |    9.0 |
| Correctness               |          98% |   98% |    99% |
