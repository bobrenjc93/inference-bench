# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `f4fc46cf2ad71f8be82d4fea7dc31112c5bf0bd0`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`02b6ecf07cf6a3e6dd395f73af5d1904312165cf` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`b79388f33856d40a40dfb622c05cedb131637d61` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 6:03 PM PT, Jul 27 2026

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
| torchinferno |     412.9s (6.9m) | `ed3588b` |
| vllm         | **200.1s (3.3m)** | `02b6ecf` |
| sglang       |     258.7s (4.3m) | `b79388f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **69.0** |  99.3 |   83.3 |
| TPOT median (ms)          |     **51.9** |  57.2 |   81.9 |
| E2E median (ms)           |    **108.0** | 143.0 |  143.4 |
| Throughput median (tok/s) |     **12.7** |   9.7 |    9.1 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **50.4** | 118.3 |  130.0 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **73.1** | 138.4 |  209.9 |
| Throughput median (tok/s) |     **13.7** |   7.2 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **66.8** | 101.6 |   86.1 |
| TPOT median (ms)          |     **50.6** |  63.1 |   87.7 |
| E2E median (ms)           |    **102.4** | 141.4 |  154.6 |
| Throughput median (tok/s) |     **13.5** |   9.3 |    8.6 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.0** | 49.5 |   58.7 |
| TPOT median (ms)          |     **26.7** | 34.7 |  108.4 |
| E2E median (ms)           |     **67.1** | 74.0 |  206.1 |
| Throughput median (tok/s) |     **19.5** | 16.4 |    6.7 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **48.8** |  63.1 |   57.0 |
| TPOT median (ms)          |     **18.5** |  21.3 |   31.2 |
| E2E median (ms)           |    **710.7** | 812.2 | 1131.0 |
| Throughput median (tok/s) |     **50.6** |  43.6 |   31.3 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **55.4** |  86.3 |   83.0 |
| TPOT median (ms)          |     **29.6** |  35.3 |   61.8 |
| E2E median (ms)           |    **212.3** | 261.8 |  369.0 |
| Throughput median (tok/s) |     **22.0** |  17.2 |   12.1 |
| Correctness               |          99% |   98% |    98% |
