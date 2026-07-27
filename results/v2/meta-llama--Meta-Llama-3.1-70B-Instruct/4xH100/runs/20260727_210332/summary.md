# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `c050f419482a9a94173479480b6f535da7b14bfc`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`53f6dd5c6f7725df4e5ac9441569860023100870` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`3005af09412cedb988a5871a3441ae49424a13bb` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 2:03 PM PT, Jul 27 2026

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
| torchinferno |     426.4s (7.1m) | `ed3588b` |
| vllm         | **188.4s (3.1m)** | `53f6dd5` |
| sglang       |     263.8s (4.4m) | `3005af0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **71.0** |  96.3 |   83.4 |
| TPOT median (ms)          |     **51.4** |  58.0 |   74.0 |
| E2E median (ms)           |    **110.4** | 144.0 |  144.9 |
| Throughput median (tok/s) |     **12.8** |   9.3 |    9.2 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **51.3** | 125.4 |  134.7 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **73.5** | 145.4 |  211.7 |
| Throughput median (tok/s) |     **13.6** |   6.9 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **64.6** | 102.6 |   92.4 |
| TPOT median (ms)          |     **50.0** |  62.9 |   89.2 |
| E2E median (ms)           |    **102.0** | 143.8 |  167.6 |
| Throughput median (tok/s) |     **13.8** |   9.6 |    7.9 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **41.8** | 49.7 |   62.4 |
| TPOT median (ms)          |     **26.7** | 34.6 |  126.7 |
| E2E median (ms)           |     **66.7** | 74.3 |  217.8 |
| Throughput median (tok/s) |     **19.9** | 16.4 |    6.5 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.6** |  63.3 |   56.7 |
| TPOT median (ms)          |     **18.4** |  21.4 |   31.1 |
| E2E median (ms)           |    **709.3** | 813.1 | 1121.7 |
| Throughput median (tok/s) |     **50.9** |  43.5 |   31.4 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **55.7** |  87.5 |   85.9 |
| TPOT median (ms)          |     **29.3** |  35.4 |   64.2 |
| E2E median (ms)           |    **212.4** | 264.1 |  372.7 |
| Throughput median (tok/s) |     **22.2** |  17.1 |   11.9 |
| Correctness               |          98% |   99% |    99% |
