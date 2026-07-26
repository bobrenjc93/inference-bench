# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `1bb77fb88965e665b35350d67e2dc2acd4f83334`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`c5ab7c804ee670e94de24370d85011ae54fd01c2`; vllm=`0934b267906f8cd9459f287b31647c3ed5c58e01` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`e14068d161a7de7b70bf309716e1df86830e208e` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 PM PT, Jul 26 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **4/4** |  0/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **4/4** |  0/4 |    0/4 |
| tree_of_thought  |      **3/4** |  1/4 |    0/4 |
| long_output      |      **4/4** |  0/4 |    0/4 |
| **Total**        |    **18/20** | 1/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     319.1s (5.3m) | `c5ab7c8` |
| vllm         | **244.7s (4.1m)** | `0934b26` |
| sglang       |     249.0s (4.1m) | `e14068d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **66.0** | 103.8 |   83.6 |
| TPOT median (ms)          |     **50.5** |  52.2 |   73.8 |
| E2E median (ms)           |    **106.4** | 151.1 |  143.8 |
| Throughput median (tok/s) |     **13.2** |   9.6 |    9.3 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **57.2** | 127.3 |  136.6 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **82.1** | 147.3 |  206.7 |
| Throughput median (tok/s) |     **12.2** |   6.8 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **61.7** | 102.4 |   85.5 |
| TPOT median (ms)          |     **49.1** |  62.9 |   87.6 |
| E2E median (ms)           |     **97.7** | 144.7 |  154.4 |
| Throughput median (tok/s) |     **13.7** |   9.1 |    8.8 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **45.9** |     49.7 |   59.1 |
| TPOT median (ms)          |     **28.8** |     34.8 |  105.0 |
| E2E median (ms)           |         75.2 | **74.5** |  203.4 |
| Throughput median (tok/s) |     **17.8** |     16.4 |    6.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **48.6** |  63.1 |   56.2 |
| TPOT median (ms)          |     **18.8** |  21.4 |   31.9 |
| E2E median (ms)           |    **708.2** | 818.1 | 1139.0 |
| Throughput median (tok/s) |     **50.1** |  43.3 |   30.7 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **55.9** |  89.2 |   84.2 |
| TPOT median (ms)          |     **29.4** |  34.3 |   59.7 |
| E2E median (ms)           |    **213.9** | 267.1 |  369.5 |
| Throughput median (tok/s) |     **21.4** |  17.1 |   12.1 |
| Correctness               |          98% |   98% |    99% |
