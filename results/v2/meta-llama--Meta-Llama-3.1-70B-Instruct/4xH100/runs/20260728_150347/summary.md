# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `040eec34bd21a6a91edad56a29e77e862d70f5e1`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`01661cc57f48ce95c639efce7c88e6dd37349007` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`1eee8fbdcc25b44e13bc097d5ff6ac24e8c24af4` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:03 AM PT, Jul 28 2026

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
| torchinferno |     437.6s (7.3m) | `ed3588b` |
| vllm         | **209.8s (3.5m)** | `01661cc` |
| sglang       |     214.0s (3.6m) | `1eee8fb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.6** |  96.6 |   81.0 |
| TPOT median (ms)          |     **52.5** |  58.5 |   72.7 |
| E2E median (ms)           |    **111.8** | 149.0 |  142.0 |
| Throughput median (tok/s) |     **12.5** |   9.2 |    9.2 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **52.7** | 122.6 |  136.1 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **75.6** | 143.1 |  210.4 |
| Throughput median (tok/s) |     **13.2** |   7.0 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **68.1** | 105.5 |   84.9 |
| TPOT median (ms)          |     **51.1** |  65.5 |   85.2 |
| E2E median (ms)           |    **105.8** | 146.5 |  150.9 |
| Throughput median (tok/s) |     **13.0** |   9.2 |    8.9 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.3** | 49.9 |   56.3 |
| TPOT median (ms)          |     **26.6** | 34.8 |  121.6 |
| E2E median (ms)           |     **67.5** | 74.6 |  215.5 |
| Throughput median (tok/s) |     **18.9** | 16.3 |    6.4 |
| Correctness               |          97% |  96% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.3** |  63.2 |   56.9 |
| TPOT median (ms)          |     **18.4** |  21.4 |   31.4 |
| E2E median (ms)           |    **709.6** | 818.7 | 1113.4 |
| Throughput median (tok/s) |     **50.7** |  43.4 |   31.0 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.6** |  87.6 |   83.0 |
| TPOT median (ms)          |     **29.7** |  36.1 |   62.2 |
| E2E median (ms)           |    **214.1** | 266.4 |  366.4 |
| Throughput median (tok/s) |     **21.7** |  17.0 |   12.1 |
| Correctness               |          99% |   98% |    98% |
