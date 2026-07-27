# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `35248d550b1be4b2e0af128bd322a10f9b622607`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`b5bcb3ce881e1d324ff7f6176ef27606558dbd74` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`8a311d1c889244ab1f857d7df79de7e5f0a6891c` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 PM PT, Jul 27 2026

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
| vllm         | **212.3s (3.5m)** | `b5bcb3c` |
| sglang       |     276.1s (4.6m) | `8a311d1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **68.0** |  97.6 |   81.1 |
| TPOT median (ms)          |     **52.9** |  58.5 |   72.4 |
| E2E median (ms)           |    **109.5** | 150.8 |  142.3 |
| Throughput median (tok/s) |     **12.7** |   9.1 |    9.4 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **53.6** | 120.7 |  132.5 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **77.3** | 139.9 |  201.1 |
| Throughput median (tok/s) |     **12.9** |   7.1 |    5.0 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **65.1** | 103.3 |   86.4 |
| TPOT median (ms)          |     **50.7** |  60.5 |   81.1 |
| E2E median (ms)           |    **100.2** | 145.6 |  152.8 |
| Throughput median (tok/s) |     **13.6** |   9.2 |    8.9 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **43.8** | 49.9 |   57.5 |
| TPOT median (ms)          |     **26.5** | 34.7 |  126.6 |
| E2E median (ms)           |     **69.1** | 74.4 |  213.6 |
| Throughput median (tok/s) |     **18.5** | 16.3 |    6.6 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **50.5** |  62.9 |   56.7 |
| TPOT median (ms)          |     **18.6** |  21.3 |   31.3 |
| E2E median (ms)           |    **705.3** | 818.5 | 1111.3 |
| Throughput median (tok/s) |     **50.7** |  43.5 |   31.2 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.2** |  86.9 |   82.8 |
| TPOT median (ms)          |     **29.7** |  35.0 |   62.3 |
| E2E median (ms)           |    **212.3** | 265.9 |  364.2 |
| Throughput median (tok/s) |     **21.7** |  17.1 |   12.2 |
| Correctness               |          99% |   98% |    99% |
