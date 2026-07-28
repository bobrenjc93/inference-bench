# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `131e94aa4d968e09e903fede25a25055a53373f3`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`0b6aa3c47ce69a1f3c8a19cafe3b9dc2871d1f6b` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`4e5a05148a2b3cc55eadbf48ff39c99a94546a35` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 PM PT, Jul 28 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **3/4** |  1/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **4/4** |  0/4 |    0/4 |
| tree_of_thought  |      **4/4** |  0/4 |    0/4 |
| long_output      |      **4/4** |  0/4 |    0/4 |
| **Total**        |    **18/20** | 1/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     487.0s (8.1m) | `ed3588b` |
| vllm         | **181.9s (3.0m)** | `0b6aa3c` |
| sglang       |     207.7s (3.5m) | `4e5a051` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **68.9** |    107.3 |   82.6 |
| TPOT median (ms)          |         51.8 | **51.4** |   72.9 |
| E2E median (ms)           |    **110.3** |    155.3 |  143.3 |
| Throughput median (tok/s) |     **12.8** |      9.7 |    9.4 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **54.4** | 129.7 |  138.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **77.3** | 149.7 |  212.6 |
| Throughput median (tok/s) |     **12.9** |   6.7 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **66.7** | 103.6 |   86.7 |
| TPOT median (ms)          |     **49.3** |  63.7 |   86.6 |
| E2E median (ms)           |    **102.3** | 143.7 |  156.1 |
| Throughput median (tok/s) |     **13.3** |   9.4 |    8.7 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **43.3** | 49.3 |   59.0 |
| TPOT median (ms)          |     **26.8** | 34.4 |  121.2 |
| E2E median (ms)           |     **68.6** | 73.7 |  217.7 |
| Throughput median (tok/s) |     **18.5** | 16.5 |    6.5 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.5** |  62.9 |   56.9 |
| TPOT median (ms)          |     **18.5** |  21.3 |   31.4 |
| E2E median (ms)           |    **706.8** | 811.7 | 1120.7 |
| Throughput median (tok/s) |     **50.7** |  43.7 |   31.1 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.5** |  90.6 |   84.8 |
| TPOT median (ms)          |     **29.3** |  34.1 |   62.4 |
| E2E median (ms)           |    **213.0** | 266.8 |  370.1 |
| Throughput median (tok/s) |     **21.6** |  17.2 |   12.1 |
| Correctness               |          98% |   98% |    99% |
