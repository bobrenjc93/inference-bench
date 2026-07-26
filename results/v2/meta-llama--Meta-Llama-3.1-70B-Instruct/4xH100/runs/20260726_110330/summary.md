# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `69d611f0dd50cb32a245753a8b691c3141e61f94`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`5559679229bc961848b121ccdeaa8fa5d79bec98` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`78d7928296a5395e6241440ab238b74aaf262e15` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 4:03 AM PT, Jul 26 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **3/4** |       1/4 |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          2/4 |       2/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         8/20 | **10/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     436.1s (7.3m) | `b2bb774` |
| vllm         |     207.0s (3.5m) | `5559679` |
| sglang       | **196.6s (3.3m)** | `78d7928` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **76.9** |    105.0 |   80.4 |
| TPOT median (ms)          |         74.6 | **55.6** |   80.1 |
| E2E median (ms)           |    **124.6** |    155.1 |  142.3 |
| Throughput median (tok/s) |      **9.5** |      9.5 |    9.2 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **67.0** | 110.8 |  133.6 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **95.9** | 130.3 |  206.5 |
| Throughput median (tok/s) |     **10.4** |   7.7 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **78.9** |     98.8 |   85.6 |
| TPOT median (ms)          |         76.9 | **64.5** |   88.6 |
| E2E median (ms)           |    **126.3** |    139.0 |  152.8 |
| Throughput median (tok/s) |          9.2 |  **9.3** |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         66.7 | **49.5** |   57.5 |
| TPOT median (ms)          |         41.6 | **34.6** |  123.6 |
| E2E median (ms)           |        103.1 | **74.8** |  220.7 |
| Throughput median (tok/s) |         12.4 | **16.5** |    6.4 |
| Correctness               |          97% |      96% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         79.6 |      63.1 | **56.2** |
| TPOT median (ms)          |         26.1 |  **21.4** |     31.6 |
| E2E median (ms)           |       1056.6 | **817.5** |   1125.3 |
| Throughput median (tok/s) |         36.0 |  **43.5** |     30.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **73.8** |      85.4 |   82.7 |
| TPOT median (ms)          |         43.8 |  **35.2** |   64.8 |
| E2E median (ms)           |        301.3 | **263.4** |  369.5 |
| Throughput median (tok/s) |         15.5 |  **17.3** |   12.0 |
| Correctness               |          99% |       98% |    98% |
