# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `cc375d515dd4e9501f2f5ffeeb91bf8c74e9c5bb`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`cbc3a872005d595493b546acf46f94a9c9f68cbb` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`9a0bd24bed1828cb0c6728262580306f8fd8ec02` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 AM PT, Jul 27 2026

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
| torchinferno |     361.6s (6.0m) | `ed3588b` |
| vllm         |     271.8s (4.5m) | `cbc3a87` |
| sglang       | **200.2s (3.3m)** | `9a0bd24` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.4** |  99.7 |   79.8 |
| TPOT median (ms)          |     **53.1** |  58.1 |   79.7 |
| E2E median (ms)           |    **111.0** | 143.4 |  140.8 |
| Throughput median (tok/s) |     **12.7** |   9.6 |    9.6 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **52.4** | 118.3 |  137.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **75.7** | 137.2 |  209.7 |
| Throughput median (tok/s) |     **13.2** |   7.3 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **67.3** | 102.0 |   85.5 |
| TPOT median (ms)          |     **49.8** |  64.9 |   88.1 |
| E2E median (ms)           |    **103.3** | 142.3 |  155.6 |
| Throughput median (tok/s) |     **13.2** |   9.6 |    8.8 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.0** | 49.9 |   56.5 |
| TPOT median (ms)          |     **26.7** | 34.7 |  128.4 |
| E2E median (ms)           |     **67.7** | 75.1 |  207.3 |
| Throughput median (tok/s) |     **18.9** | 16.4 |    6.8 |
| Correctness               |          96% |  96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.9** |  63.3 |   56.4 |
| TPOT median (ms)          |     **18.5** |  21.4 |   31.9 |
| E2E median (ms)           |    **707.4** | 819.6 | 1138.5 |
| Throughput median (tok/s) |     **50.8** |  43.4 |   30.7 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.4** |  86.6 |   83.1 |
| TPOT median (ms)          |     **29.6** |  35.8 |   65.6 |
| E2E median (ms)           |    **213.0** | 263.5 |  370.4 |
| Throughput median (tok/s) |     **21.8** |  17.3 |   12.1 |
| Correctness               |          98% |   98% |    99% |
