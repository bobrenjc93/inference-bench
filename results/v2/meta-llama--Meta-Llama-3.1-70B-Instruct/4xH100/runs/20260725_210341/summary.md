# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `ac6c0cd35655d13e4977f5b4611734c0083d27b3`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`d30b1ecd1bdf7c3d92f3b444c4538efd8fbb40ac` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`d3cf4dfbaad59dde3e08388978a5ffdf051cad72` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 2:03 PM PT, Jul 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          2/4 |       2/4 |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          2/4 |       2/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         7/20 | **11/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     387.4s (6.5m) | `b2bb774` |
| vllm         |     199.6s (3.3m) | `d30b1ec` |
| sglang       | **195.2s (3.3m)** | `d3cf4df` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **76.2** |     98.8 |   82.3 |
| TPOT median (ms)          |         72.6 | **58.1** |   70.7 |
| E2E median (ms)           |    **122.6** |    146.1 |  142.2 |
| Throughput median (tok/s) |          9.5 |  **9.6** |    9.2 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **80.8** | 111.9 |  135.8 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **109.6** | 133.8 |  211.7 |
| Throughput median (tok/s) |      **9.1** |   7.5 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **77.9** |     99.8 |   86.0 |
| TPOT median (ms)          |         75.3 | **61.9** |   87.7 |
| E2E median (ms)           |    **124.4** |    141.3 |  153.7 |
| Throughput median (tok/s) |          9.4 |  **9.6** |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         64.3 | **49.5** |   58.5 |
| TPOT median (ms)          |         41.3 | **34.3** |  123.4 |
| E2E median (ms)           |         99.9 | **74.1** |  211.7 |
| Throughput median (tok/s) |         12.8 | **16.4** |    6.5 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         79.2 |      62.7 | **56.3** |
| TPOT median (ms)          |         26.1 |  **21.3** |     31.2 |
| E2E median (ms)           |       1062.5 | **813.8** |   1108.5 |
| Throughput median (tok/s) |         35.9 |  **43.6** |     31.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **75.7** |      84.5 |   83.8 |
| TPOT median (ms)          |         43.1 |  **35.1** |   62.6 |
| E2E median (ms)           |        303.8 | **261.9** |  365.6 |
| Throughput median (tok/s) |         15.4 |  **17.3** |   12.1 |
| Correctness               |          99% |       98% |    99% |
