# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `8f73eb8bd9aef46a860c5bbe774ace659d59fd72`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; sglang=`67c2258906d1898391cdcdfe871c94a79e4a6580` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 4:03 AM PT, Jul 29 2026

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
| torchinferno |   346.2s (5.8m) | `ed3588b` |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |   205.1s (3.4m) | `67c2258` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **70.0** |    - |   86.2 |
| TPOT median (ms)          |     **54.1** |    - |   73.6 |
| E2E median (ms)           |    **112.9** |    - |  144.9 |
| Throughput median (tok/s) |     **12.4** |    - |    9.0 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-f3eb154f/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **62.9** |    - |  135.4 |
| TPOT median (ms)          |          0.0 |    - |    0.0 |
| E2E median (ms)           |     **89.1** |    - |  212.1 |
| Throughput median (tok/s) |     **11.2** |    - |    4.7 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-f3eb154f/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **70.4** |    - |   84.6 |
| TPOT median (ms)          |     **51.9** |    - |   84.7 |
| E2E median (ms)           |    **109.4** |    - |  152.1 |
| Throughput median (tok/s) |     **12.4** |    - |    8.7 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-f3eb154f/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.0** |    - |   57.2 |
| TPOT median (ms)          |     **27.0** |    - |  144.2 |
| E2E median (ms)           |     **68.7** |    - |  227.8 |
| Throughput median (tok/s) |     **19.0** |    - |    6.3 |
| Correctness               |          97% |    - |    97% |

> **vllm error:** `Command '['/workspace/submit-f3eb154f/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **49.4** |    - |   57.2 |
| TPOT median (ms)          |     **18.7** |    - |   31.2 |
| E2E median (ms)           |    **717.1** |    - | 1111.2 |
| Throughput median (tok/s) |     **50.2** |    - |   31.3 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-f3eb154f/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **58.9** |    - |   84.1 |
| TPOT median (ms)          |     **30.4** |    - |   66.7 |
| E2E median (ms)           |    **219.4** |    - |  369.6 |
| Throughput median (tok/s) |     **21.0** |    - |   12.0 |
| Correctness               |          98% |    - |    99% |
