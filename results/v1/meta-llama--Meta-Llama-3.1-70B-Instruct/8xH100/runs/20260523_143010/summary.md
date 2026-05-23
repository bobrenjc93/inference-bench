# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:03 AM PT, May 23 2026

## Scorecard

| Benchmark | torchinferno | vllm | sglang |
| :-------- | -----------: | ---: | -----: |
| **Total** |          0/0 |  0/0 |    0/0 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno | **103.9s (1.7m)** | `9f91b40` |
| vllm         |   1179.6s (19.7m) | `5bb8d27` |
| sglang       |     185.3s (3.1m) | `a5a64a3` |

## Per-Benchmark Results

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |      - |
| TPOT median (ms)          |            - |    - |      - |
| E2E median (ms)           |            - |    - |      - |
| Throughput median (tok/s) |            - |    - |      - |
| Correctness               |            - |    - |      - |
