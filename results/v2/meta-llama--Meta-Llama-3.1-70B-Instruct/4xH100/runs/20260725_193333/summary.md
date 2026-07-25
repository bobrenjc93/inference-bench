# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `e7c2e308f4dea8d484a14ae43fccd3cd5eaa1d2c`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100; vllm=NVIDIA H100; sglang=NVIDIA H100
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`ee1d99636702b8ed9ad88c2c2b833d331dce01c1` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`9791fc70903b1144687571d7ac748fdf025ae1ec` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:33 PM PT, Jul 25 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **3/4** |  1/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **3/4** |  1/4 |    0/4 |
| tree_of_thought  |      **4/4** |  0/4 |    0/4 |
| long_output      |      **3/4** |  0/4 |    1/4 |
| **Total**        |    **16/20** | 2/20 |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **42.8s (0.7m)** | `b2bb774` |
| vllm         |    168.8s (2.8m) | `ee1d996` |
| sglang       |    145.1s (2.4m) | `9791fc7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **72.7** |    107.7 |   90.4 |
| TPOT median (ms)          |         70.3 | **60.9** |  103.6 |
| E2E median (ms)           |    **118.0** |    155.3 |  172.0 |
| Throughput median (tok/s) |     **10.8** |      9.0 |    7.6 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **46.2** |  84.3 |  104.1 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **71.1** | 107.3 |  207.3 |
| Throughput median (tok/s) |     **14.1** |   9.3 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **70.0** |    104.8 |   95.4 |
| TPOT median (ms)          |         67.6 | **65.5** |  114.9 |
| E2E median (ms)           |    **116.6** |    151.5 |  181.6 |
| Throughput median (tok/s) |     **11.0** |      9.1 |    6.9 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **45.0** | 60.4 |   59.2 |
| TPOT median (ms)          |     **30.4** | 42.7 |  440.0 |
| E2E median (ms)           |     **67.7** | 89.5 |  514.4 |
| Throughput median (tok/s) |     **21.3** | 13.6 |    3.0 |
| Correctness               |          97% |  96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm |   sglang |
| :------------------------ | -----------: | ----: | -------: |
| TTFT median (ms)          |         76.8 |  76.8 | **67.6** |
| TPOT median (ms)          |     **24.1** |  25.9 |     38.1 |
| E2E median (ms)           |    **885.2** | 989.4 |   1438.3 |
| Throughput median (tok/s) |     **38.6** |  36.0 |     25.5 |
| Correctness               |         100% |  100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **62.1** |  86.8 |   83.3 |
| TPOT median (ms)          |     **38.5** |  39.0 |  139.3 |
| E2E median (ms)           |    **251.7** | 298.6 |  502.7 |
| Throughput median (tok/s) |     **19.2** |  15.4 |    9.6 |
| Correctness               |          99% |   98% |    99% |
