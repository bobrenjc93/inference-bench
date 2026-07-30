# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `d1969cc8c6d7536e6556fb344bc086f370bb653f`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; sglang=`fc007e1f00fdadc25e831364a2df63a64af61fb9` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 AM PT, Jul 30 2026

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
| torchinferno |   392.3s (6.5m) | `ed3588b` |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |   241.6s (4.0m) | `fc007e1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **73.0** |    - |   84.5 |
| TPOT median (ms)          |     **52.1** |    - |   80.2 |
| E2E median (ms)           |    **112.0** |    - |  144.4 |
| Throughput median (tok/s) |     **12.5** |    - |    9.1 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-49e1faa3/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **54.1** |    - |  139.5 |
| TPOT median (ms)          |          0.0 |    - |    0.0 |
| E2E median (ms)           |     **77.4** |    - |  214.4 |
| Throughput median (tok/s) |     **12.9** |    - |    4.7 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-49e1faa3/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **68.8** |    - |   86.3 |
| TPOT median (ms)          |     **52.4** |    - |   78.9 |
| E2E median (ms)           |    **107.5** |    - |  151.6 |
| Throughput median (tok/s) |     **12.8** |    - |    8.8 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-49e1faa3/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.4** |    - |   58.4 |
| TPOT median (ms)          |     **26.7** |    - |  110.9 |
| E2E median (ms)           |     **69.1** |    - |  212.8 |
| Throughput median (tok/s) |     **19.5** |    - |    6.5 |
| Correctness               |          97% |    - |    97% |

> **vllm error:** `Command '['/workspace/submit-49e1faa3/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **50.0** |    - |   57.6 |
| TPOT median (ms)          |     **18.5** |    - |   31.0 |
| E2E median (ms)           |    **720.5** |    - | 1084.3 |
| Throughput median (tok/s) |     **50.4** |    - |   31.5 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-49e1faa3/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.6** |    - |   85.3 |
| TPOT median (ms)          |     **29.9** |    - |   60.2 |
| E2E median (ms)           |    **217.3** |    - |  361.5 |
| Throughput median (tok/s) |     **21.6** |    - |   12.1 |
| Correctness               |          99% |    - |    98% |
