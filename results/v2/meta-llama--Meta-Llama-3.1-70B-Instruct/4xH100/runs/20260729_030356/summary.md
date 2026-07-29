# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `f08fb6f477bfd134da8dc5078485d4db3e9a678e`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`f37f03db4af69e4969242767734db3d9175055f7` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`68673fe6c58b907a5da89b1f92a6972f74dc0086` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:03 PM PT, Jul 28 2026

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
| torchinferno |     390.1s (6.5m) | `ed3588b` |
| vllm         |     208.6s (3.5m) | `f37f03d` |
| sglang       | **207.5s (3.5m)** | `68673fe` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **69.7** |  96.2 |   81.3 |
| TPOT median (ms)          |     **52.3** |  56.7 |   76.8 |
| E2E median (ms)           |    **111.2** | 144.2 |  141.5 |
| Throughput median (tok/s) |     **12.7** |   9.3 |    9.4 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **51.3** | 122.3 |  139.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **73.5** | 142.4 |  214.8 |
| Throughput median (tok/s) |     **13.6** |   7.0 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **66.5** | 103.2 |   87.4 |
| TPOT median (ms)          |     **51.0** |  61.4 |   84.4 |
| E2E median (ms)           |    **101.8** | 144.0 |  156.0 |
| Throughput median (tok/s) |     **13.3** |   9.6 |    8.6 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.2** | 49.8 |   58.8 |
| TPOT median (ms)          |     **26.6** | 34.5 |  133.9 |
| E2E median (ms)           |     **67.1** | 74.4 |  212.1 |
| Throughput median (tok/s) |     **19.2** | 16.4 |    6.5 |
| Correctness               |          97% |  97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **50.6** |  62.5 |   56.9 |
| TPOT median (ms)          |     **18.4** |  21.3 |   31.2 |
| E2E median (ms)           |    **704.2** | 812.1 | 1111.2 |
| Throughput median (tok/s) |     **50.7** |  43.7 |   31.4 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.1** |  86.8 |   84.7 |
| TPOT median (ms)          |     **29.7** |  34.8 |   65.2 |
| E2E median (ms)           |    **211.5** | 263.4 |  367.1 |
| Throughput median (tok/s) |     **21.9** |  17.2 |   12.1 |
| Correctness               |          98% |   98% |    98% |
