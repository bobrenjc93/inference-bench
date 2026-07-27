# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `413488ba176f9d6346788b5c6ebeb0e54d9f05c7`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100; vllm=NVIDIA H100; sglang=NVIDIA H100
- **Provider source:** torchinferno=`e6338eef28571978b5cfaaa2476659076ed31a88`; vllm=`fdaa0d9e59238b6884f9515fa3245dea118edc66` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`38636120238b58efd6776ceff0caba474453925b` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 5:33 PM PT, Jul 26 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **46.6s (0.8m)** | `e6338ee` |
| vllm         |    177.7s (3.0m) | `fdaa0d9` |
| sglang       |    161.0s (2.7m) | `3863612` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **65.6** | 115.3 |   89.2 |
| TPOT median (ms)          |     **53.0** |  64.8 |   93.4 |
| E2E median (ms)           |    **104.4** | 160.6 |  173.1 |
| Throughput median (tok/s) |     **13.5** |   8.2 |    7.5 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **42.6** |  77.4 |  115.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **68.0** | 100.9 |  255.1 |
| Throughput median (tok/s) |     **14.7** |   9.9 |    3.9 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **64.6** | 101.5 |   97.3 |
| TPOT median (ms)          |     **51.5** |  64.2 |  106.3 |
| E2E median (ms)           |    **101.8** | 147.6 |  187.7 |
| Throughput median (tok/s) |     **13.7** |   9.2 |    6.9 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **40.3** | 61.6 |   59.8 |
| TPOT median (ms)          |     **28.4** | 42.8 |  394.3 |
| E2E median (ms)           |     **61.5** | 90.5 |  464.5 |
| Throughput median (tok/s) |     **23.2** | 13.4 |    3.1 |
| Correctness               |          97% |  97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |   vllm | sglang |
| :------------------------ | -----------: | -----: | -----: |
| TTFT median (ms)          |     **55.6** |   77.7 |   68.5 |
| TPOT median (ms)          |     **20.9** |   26.1 |   38.6 |
| E2E median (ms)           |    **770.7** | 1019.0 | 1432.6 |
| Throughput median (tok/s) |     **45.2** |   35.7 |   25.2 |
| Correctness               |         100% |   100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **53.7** |  86.7 |   86.1 |
| TPOT median (ms)          |     **30.8** |  39.6 |  126.5 |
| E2E median (ms)           |    **221.3** | 303.7 |  502.6 |
| Throughput median (tok/s) |     **22.1** |  15.3 |    9.3 |
| Correctness               |          98% |   98% |    98% |
