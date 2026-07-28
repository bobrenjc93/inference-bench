# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `87e1096fdb1c22930df1d69926197c88f994e428`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`bb3b61f2fd2333ab165ebaba13f133db4210b9f2` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`7778dd23ead27c34bd2c3b758a6cf8cf8012aca5` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 2:03 PM PT, Jul 28 2026

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
| torchinferno |     343.9s (5.7m) | `ed3588b` |
| vllm         | **208.1s (3.5m)** | `bb3b61f` |
| sglang       |     260.2s (4.3m) | `7778dd2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **68.1** |  99.7 |   81.0 |
| TPOT median (ms)          |     **53.1** |  58.9 |   72.0 |
| E2E median (ms)           |    **109.4** | 149.5 |  141.7 |
| Throughput median (tok/s) |     **12.6** |   8.7 |    9.4 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **48.8** | 122.3 |  135.1 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **71.7** | 144.0 |  209.2 |
| Throughput median (tok/s) |     **14.0** |   6.9 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **64.5** |  98.4 |   85.3 |
| TPOT median (ms)          |     **50.3** |  63.3 |   86.7 |
| E2E median (ms)           |     **98.9** | 139.1 |  152.3 |
| Throughput median (tok/s) |     **13.8** |   9.7 |    8.8 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.3** | 49.5 |   57.0 |
| TPOT median (ms)          |     **26.5** | 34.5 |  145.3 |
| E2E median (ms)           |     **66.9** | 74.1 |  221.7 |
| Throughput median (tok/s) |     **19.3** | 16.5 |    6.5 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **50.2** |  63.0 |   57.0 |
| TPOT median (ms)          |     **18.5** |  21.3 |   31.5 |
| E2E median (ms)           |    **708.3** | 814.1 | 1142.9 |
| Throughput median (tok/s) |     **50.6** |  43.8 |   30.9 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **54.8** |  86.6 |   83.1 |
| TPOT median (ms)          |     **29.7** |  35.6 |   67.1 |
| E2E median (ms)           |    **211.0** | 264.1 |  373.5 |
| Throughput median (tok/s) |     **22.0** |  17.1 |   12.1 |
| Correctness               |          98% |   98% |    99% |
