# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `7015a4f65ffcf4cac74ca40f707532a95295e673`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`54ab69b14eeafd5c8dcf818cfcc0eeb26d2ebddb` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`dac4325c0e4da9791c2e2810d51886d678d9f7a1` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 6:04 PM PT, Jul 28 2026

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
| torchinferno |     522.1s (8.7m) | `ed3588b` |
| vllm         |     225.8s (3.8m) | `54ab69b` |
| sglang       | **199.4s (3.3m)** | `dac4325` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **69.3** |  96.0 |   83.6 |
| TPOT median (ms)          |     **51.8** |  58.9 |   81.2 |
| E2E median (ms)           |    **110.6** | 145.9 |  143.7 |
| Throughput median (tok/s) |     **13.1** |   8.9 |    9.1 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.5** | 124.1 |  141.5 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **73.1** | 144.3 |  213.3 |
| Throughput median (tok/s) |     **13.7** |   6.9 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **65.8** |  98.8 |   90.8 |
| TPOT median (ms)          |     **50.5** |  62.5 |   84.6 |
| E2E median (ms)           |    **101.2** | 140.1 |  158.0 |
| Throughput median (tok/s) |     **13.3** |   9.6 |    8.6 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **41.7** | 49.8 |   59.2 |
| TPOT median (ms)          |     **26.9** | 34.4 |  127.5 |
| E2E median (ms)           |     **65.9** | 74.7 |  217.4 |
| Throughput median (tok/s) |     **19.5** | 16.4 |    6.5 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.8** |  63.0 |   57.2 |
| TPOT median (ms)          |     **18.5** |  21.3 |   31.5 |
| E2E median (ms)           |    **709.1** | 814.6 | 1133.3 |
| Throughput median (tok/s) |     **50.8** |  43.7 |   30.9 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **55.2** |  86.4 |   86.5 |
| TPOT median (ms)          |     **29.5** |  35.4 |   65.0 |
| E2E median (ms)           |    **212.0** | 263.9 |  373.1 |
| Throughput median (tok/s) |     **22.1** |  17.1 |   12.0 |
| Correctness               |          98% |   99% |    98% |
