# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `c0c916b27250ef87b7145e93a70c7cb5cc3c0529`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; sglang=`f4e0ac382e4e5d644f2fbe4a15c20da53500bbca` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:03 PM PT, Jul 29 2026

## Integrity Warnings

- **vllm:** Provider reported benchmark or deployment errors under the result eligibility policy.
- **vllm:** Benchmark 'few_shot' has no completed result.
- **vllm:** Benchmark 'self_consistency' has no completed result.
- **vllm:** Benchmark 'multi_turn' has no completed result.
- **vllm:** Benchmark 'tree_of_thought' has no completed result.
- **vllm:** Benchmark 'long_output' has no completed result.

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **4/4** |  N/C |    0/4 |
| self_consistency |      **3/4** |  N/C |    0/4 |
| multi_turn       |      **4/4** |  N/C |    0/4 |
| tree_of_thought  |      **4/4** |  N/C |    0/4 |
| long_output      |      **4/4** |  N/C |    0/4 |
| **Total**        |    **19/20** |  N/C |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.
N/C = excluded from scoring because integrity validation did not pass.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno |   348.3s (5.8m) | `ed3588b` |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |   260.5s (4.3m) | `f4e0ac3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **74.6** |    - |   81.2 |
| TPOT median (ms)          |     **52.0** |    - |   82.5 |
| E2E median (ms)           |    **113.2** |    - |  142.4 |
| Throughput median (tok/s) |     **12.4** |    - |    9.2 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-ba7c07de/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **54.8** |    - |  136.3 |
| TPOT median (ms)          |          0.0 |    - |    0.0 |
| E2E median (ms)           |     **77.2** |    - |  209.4 |
| Throughput median (tok/s) |     **13.0** |    - |    4.8 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-ba7c07de/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **69.6** |    - |   84.4 |
| TPOT median (ms)          |     **51.6** |    - |   81.4 |
| E2E median (ms)           |    **110.2** |    - |  150.6 |
| Throughput median (tok/s) |     **12.7** |    - |    9.0 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-ba7c07de/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.7** |    - |   58.8 |
| TPOT median (ms)          |     **26.5** |    - |  110.9 |
| E2E median (ms)           |     **68.3** |    - |  209.5 |
| Throughput median (tok/s) |     **19.1** |    - |    6.6 |
| Correctness               |          97% |    - |    97% |

> **vllm error:** `Command '['/workspace/submit-ba7c07de/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **50.8** |    - |   57.5 |
| TPOT median (ms)          |     **18.7** |    - |   31.1 |
| E2E median (ms)           |    **718.1** |    - | 1112.9 |
| Throughput median (tok/s) |     **49.9** |    - |   31.4 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-ba7c07de/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **58.5** |    - |   83.6 |
| TPOT median (ms)          |     **29.8** |    - |   61.2 |
| E2E median (ms)           |    **217.4** |    - |  365.0 |
| Throughput median (tok/s) |     **21.4** |    - |   12.2 |
| Correctness               |          98% |    - |    99% |
