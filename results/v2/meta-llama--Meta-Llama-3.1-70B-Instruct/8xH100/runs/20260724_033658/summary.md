# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `706105c880f120395d563759b4d3e128332a7fa4`
- **TP:** 8
- **Hardware:** 8xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=8/8, vllm=8/8, sglang=8/8
- **Observed GPU products:** torchinferno=NVIDIA H100; vllm=NVIDIA H100; sglang=NVIDIA H100
- **Provider source:** torchinferno=`1e7c5c4766a6365a8eeda84f947cce9f771f75e1`; vllm=`2ac125123a8d312823cf4ef56ca165f04f579dd1` + build patch `d22bf8e0c0e1802dc97fcb8743d32ecc762682c00f595f2b82434af9f0b94ca6`; sglang=`99b29bf1889c7bf84973596a5273adc80a15b523` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:36 PM PT, Jul 23 2026

## Scorecard

| Benchmark        | torchinferno |    vllm | sglang |
| :--------------- | -----------: | ------: | -----: |
| few_shot         |          2/4 |     2/4 |    0/4 |
| self_consistency |      **3/4** |     0/4 |    0/4 |
| multi_turn       |      **3/4** |     1/4 |    0/4 |
| tree_of_thought  |      **4/4** |     0/4 |    0/4 |
| long_output      |          0/4 | **3/4** |    1/4 |
| **Total**        |    **12/20** |    6/20 |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.8s (0.7m)** | `1e7c5c4` |
| vllm         |    141.6s (2.4m) | `2ac1251` |
| sglang       |    144.3s (2.4m) | `99b29bf` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **64.4** |     78.0 |   72.3 |
| TPOT median (ms)          |         61.8 | **38.2** |   83.7 |
| E2E median (ms)           |    **105.1** |    106.6 |  135.8 |
| Throughput median (tok/s) |         11.6 | **12.7** |   10.0 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **35.4** | 64.0 |  102.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **54.4** | 78.4 |  228.1 |
| Throughput median (tok/s) |     **18.4** | 12.7 |    4.4 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **57.7** |     92.2 |   70.6 |
| TPOT median (ms)          |         54.2 | **37.3** |   90.7 |
| E2E median (ms)           |     **96.6** |    122.7 |  140.3 |
| Throughput median (tok/s) |     **13.0** |     11.4 |    9.6 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **34.6** | 37.9 |   43.7 |
| TPOT median (ms)          |     **22.7** | 25.3 |  202.2 |
| E2E median (ms)           |     **50.9** | 55.3 |  219.6 |
| Throughput median (tok/s) |     **27.7** | 21.9 |    6.1 |
| Correctness               |          97% |  96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         63.0 |      52.7 | **45.3** |
| TPOT median (ms)          |         18.6 |  **17.1** |     25.9 |
| E2E median (ms)           |        687.3 | **649.1** |    910.2 |
| Throughput median (tok/s) |         49.0 |  **54.5** |     37.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **51.0** |     65.0 |   66.9 |
| TPOT median (ms)          |         31.5 | **23.6** |   80.5 |
| E2E median (ms)           |    **198.9** |    202.4 |  326.8 |
| Throughput median (tok/s) |     **23.9** |     22.7 |   13.6 |
| Correctness               |          99% |      98% |    99% |
