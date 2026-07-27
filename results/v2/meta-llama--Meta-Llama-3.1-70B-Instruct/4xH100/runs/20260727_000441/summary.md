# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `a8473df14dc23afea6da70d1b3a054daa3ccf26d`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100; vllm=NVIDIA H100; sglang=NVIDIA H100
- **Provider source:** torchinferno=`e6338eef28571978b5cfaaa2476659076ed31a88`; vllm=`0934b267906f8cd9459f287b31647c3ed5c58e01` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`38636120238b58efd6776ceff0caba474453925b` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 5:04 PM PT, Jul 26 2026

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
| torchinferno | **55.3s (0.9m)** | `e6338ee` |
| vllm         |    172.6s (2.9m) | `0934b26` |
| sglang       |    147.6s (2.5m) | `3863612` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **66.9** | 104.3 |   91.5 |
| TPOT median (ms)          |     **53.9** |  63.3 |   94.7 |
| E2E median (ms)           |    **104.2** | 155.0 |  171.1 |
| Throughput median (tok/s) |     **13.3** |   8.7 |    7.6 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **43.1** |  86.3 |  110.8 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **68.1** | 111.7 |  228.8 |
| Throughput median (tok/s) |     **14.7** |   9.0 |    4.4 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **62.9** | 111.1 |   93.0 |
| TPOT median (ms)          |     **51.3** |  60.1 |  123.5 |
| E2E median (ms)           |     **97.6** | 156.5 |  186.1 |
| Throughput median (tok/s) |     **13.8** |   8.8 |    6.8 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **39.7** | 61.6 |   60.2 |
| TPOT median (ms)          |     **28.5** | 42.8 |  405.9 |
| E2E median (ms)           |     **60.6** | 91.1 |  471.2 |
| Throughput median (tok/s) |     **23.3** | 13.5 |    3.0 |
| Correctness               |          97% |  96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **53.9** |  78.2 |   68.2 |
| TPOT median (ms)          |     **21.0** |  26.3 |   37.5 |
| E2E median (ms)           |    **778.8** | 994.1 | 1365.1 |
| Throughput median (tok/s) |     **44.8** |  35.6 |   25.9 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **53.3** |  88.3 |   84.7 |
| TPOT median (ms)          |     **30.9** |  38.5 |  132.3 |
| E2E median (ms)           |    **221.9** | 301.7 |  484.5 |
| Throughput median (tok/s) |     **22.0** |  15.1 |    9.5 |
| Correctness               |          98% |   98% |    99% |
