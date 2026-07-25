# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `9476ad3230d30b5315b3bd2dd7a9422bf206748f`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`97af8eca0494f263ac06d499989585a2b943b109`; vllm=`d1a8ba63d9d2bb51ebf60dd5ea1463cf61c70cea` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`e943e609dc5059ce64c81cf07a56c8a886d25fcb` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 6:03 AM PT, Jul 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |      **3/4** |       1/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **13/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     379.2s (6.3m) | `97af8ec` |
| vllm         |     202.7s (3.4m) | `d1a8ba6` |
| sglang       | **199.4s (3.3m)** | `e943e60` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        230.3 |     97.5 |  **85.5** |
| TPOT median (ms)          |        227.3 | **56.2** |      78.0 |
| E2E median (ms)           |        447.0 |    147.2 | **146.9** |
| Throughput median (tok/s) |          3.0 |  **9.6** |       8.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        366.1 | **104.4** |  136.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        459.1 | **123.4** |  210.8 |
| Throughput median (tok/s) |          2.2 |   **8.1** |    4.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **66.4** |    109.8 |   86.7 |
| TPOT median (ms)          |         62.8 | **50.8** |   86.1 |
| E2E median (ms)           |    **124.6** |    160.1 |  155.6 |
| Throughput median (tok/s) |     **10.6** |      9.3 |    8.6 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.4 | **49.1** |   56.4 |
| TPOT median (ms)          |         41.2 | **34.2** |  131.6 |
| E2E median (ms)           |        102.9 | **73.8** |  218.7 |
| Throughput median (tok/s) |         12.7 | **16.6** |    6.3 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        253.2 |      62.9 | **55.9** |
| TPOT median (ms)          |         59.9 |  **21.4** |     31.1 |
| E2E median (ms)           |       2472.4 | **812.6** |   1112.5 |
| Throughput median (tok/s) |         15.1 |  **43.6** |     31.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        196.3 |      84.7 | **84.3** |
| TPOT median (ms)          |         78.3 |  **32.5** |     65.3 |
| E2E median (ms)           |        721.2 | **263.4** |    368.9 |
| Throughput median (tok/s) |          8.7 |  **17.4** |     12.0 |
| Correctness               |          98% |       98% |      99% |
