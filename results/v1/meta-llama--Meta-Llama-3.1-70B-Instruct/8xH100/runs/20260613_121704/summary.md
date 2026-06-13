# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     366.5s (6.1m) | `8d2b743` |
| vllm         |   1369.8s (22.8m) | `470229c` |
| sglang       | **217.9s (3.6m)** | `f7041c9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     161.9 | **149.0** |
| TPOT median (ms)          |            - |  **57.7** |      74.7 |
| E2E median (ms)           |            - | **214.7** |     217.3 |
| Throughput median (tok/s) |            - |   **7.0** |       5.4 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
 capture bs=8 q=64: No module named 'flashinfer'



[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'

[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'




[WARMUP] FlashInfer prefill graphs: 0 captured in 32ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 31ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms




TorchInferno OpenAI server listening on http://0.0.0.0:8001/v1 model=meta-llama/Meta-Llama-3.1-70B-Instruct
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **181.7** |  219.6 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **205.6** |  364.3 |
| Throughput median (tok/s) |            - |   **4.9** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
 capture bs=8 q=64: No module named 'flashinfer'



[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'

[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'




[WARMUP] FlashInfer prefill graphs: 0 captured in 32ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 31ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms




TorchInferno OpenAI server listening on http://0.0.0.0:8001/v1 model=meta-llama/Meta-Llama-3.1-70B-Instruct
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     180.5 | **161.8** |
| TPOT median (ms)          |            - |  **57.8** |     106.1 |
| E2E median (ms)           |            - | **234.2** |     261.3 |
| Throughput median (tok/s) |            - |   **6.0** |       5.2 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
 capture bs=8 q=64: No module named 'flashinfer'



[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'

[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'




[WARMUP] FlashInfer prefill graphs: 0 captured in 32ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 31ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms




TorchInferno OpenAI server listening on http://0.0.0.0:8001/v1 model=meta-llama/Meta-Llama-3.1-70B-Instruct
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **60.2** |   83.6 |
| TPOT median (ms)          |            - | **29.3** |   44.9 |
| E2E median (ms)           |            - | **82.0** |  138.0 |
| Throughput median (tok/s) |            - | **14.7** |    9.9 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
 capture bs=8 q=64: No module named 'flashinfer'



[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'

[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'




[WARMUP] FlashInfer prefill graphs: 0 captured in 32ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 31ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms




TorchInferno OpenAI server listening on http://0.0.0.0:8001/v1 model=meta-llama/Meta-Llama-3.1-70B-Instruct
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      66.6 | **65.4** |
| TPOT median (ms)          |            - |  **15.1** |     22.7 |
| E2E median (ms)           |            - | **610.5** |    852.4 |
| Throughput median (tok/s) |            - |  **58.9** |     41.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Log tail:
 capture bs=8 q=64: No module named 'flashinfer'



[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=16 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=24 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'

[WARMUP] FI prefill graph capture bs=32 q=64: No module named 'flashinfer'




[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'
[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'[WARMUP] FI prefill graph capture bs=48 q=64: No module named 'flashinfer'




[WARMUP] FlashInfer prefill graphs: 0 captured in 32ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms[WARMUP] FlashInfer prefill graphs: 0 captured in 30ms[WARMUP] FlashInfer prefill graphs: 0 captured in 31ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms
[WARMUP] FlashInfer prefill graphs: 0 captured in 29ms




TorchInferno OpenAI server listening on http://0.0.0.0:8001/v1 model=meta-llama/Meta-Llama-3.1-70B-Instruct
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **130.2** |  135.9 |
| TPOT median (ms)          |            - |  **32.0** |   49.7 |
| E2E median (ms)           |            - | **269.4** |  366.6 |
| Throughput median (tok/s) |            - |  **18.3** |   13.0 |
| Correctness               |            - |       99% |    99% |
