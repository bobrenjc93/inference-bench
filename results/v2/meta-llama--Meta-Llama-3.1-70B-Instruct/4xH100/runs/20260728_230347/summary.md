# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `11240607da6dd104a5949a6f5ad3905c26ea9273`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`56f31af62afe6553369b14af225bfafb788e99a0` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`16a52bff2306a886cdd7a21be4b6d927f2ede9cd` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 4:03 PM PT, Jul 28 2026

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
| torchinferno |     463.2s (7.7m) | `ed3588b` |
| vllm         | **221.3s (3.7m)** | `56f31af` |
| sglang       |     243.1s (4.1m) | `16a52bf` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **71.7** | 101.2 |   85.2 |
| TPOT median (ms)          |     **51.9** |  54.6 |   71.5 |
| E2E median (ms)           |    **110.4** | 148.6 |  145.4 |
| Throughput median (tok/s) |     **12.6** |   9.5 |    9.0 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.4** | 116.0 |  137.5 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **72.0** | 137.2 |  209.5 |
| Throughput median (tok/s) |     **13.9** |   7.3 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **66.8** |  98.8 |   89.2 |
| TPOT median (ms)          |     **49.3** |  64.2 |   79.7 |
| E2E median (ms)           |    **102.4** | 142.9 |  155.0 |
| Throughput median (tok/s) |     **13.2** |   9.3 |    8.8 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.2** | 49.7 |   59.1 |
| TPOT median (ms)          |     **26.4** | 34.4 |  115.5 |
| E2E median (ms)           |     **67.0** | 74.5 |  217.6 |
| Throughput median (tok/s) |     **18.7** | 16.3 |    6.6 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **48.9** |  62.6 |   56.7 |
| TPOT median (ms)          |     **18.5** |  21.3 |   31.6 |
| E2E median (ms)           |    **697.0** | 811.9 | 1127.5 |
| Throughput median (tok/s) |     **50.9** |  43.7 |   30.9 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **55.8** |  85.7 |   85.5 |
| TPOT median (ms)          |     **29.2** |  34.9 |   59.6 |
| E2E median (ms)           |    **209.8** | 263.0 |  371.0 |
| Throughput median (tok/s) |     **21.9** |  17.2 |   12.0 |
| Correctness               |          98% |   99% |    99% |
