# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 PM PT, Jun 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     457.7s (7.6m) | `4e9171b` |
| vllm         |     582.9s (9.7m) | `0775b88` |
| sglang       | **275.3s (4.6m)** | `b60185c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **142.7** |  147.1 |
| TPOT median (ms)          |            - |  **42.9** |   73.2 |
| E2E median (ms)           |            - | **177.4** |  218.9 |
| Throughput median (tok/s) |            - |   **8.0** |    5.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
args, **kwargs)
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[2]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1132)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1132
[3]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1133)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1133
[4]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[5]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[6]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[7]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **195.8** |  208.7 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **244.4** |  348.6 |
| Throughput median (tok/s) |            - |   **4.1** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
args, **kwargs)
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[2]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1132)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1132
[3]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1133)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1133
[4]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[5]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[6]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[7]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **159.8** |  168.3 |
| TPOT median (ms)          |            - |  **53.8** |  104.6 |
| E2E median (ms)           |            - | **202.8** |  276.9 |
| Throughput median (tok/s) |            - |   **6.5** |    4.9 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
args, **kwargs)
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[2]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1132)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1132
[3]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1133)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1133
[4]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[5]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[6]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[7]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **60.4** |   85.8 |
| TPOT median (ms)          |            - | **29.4** |   44.2 |
| E2E median (ms)           |            - | **82.9** |  139.8 |
| Throughput median (tok/s) |            - | **14.9** |    9.4 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
args, **kwargs)
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[2]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1132)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1132
[3]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1133)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1133
[4]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[5]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[6]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[7]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      75.7 | **70.1** |
| TPOT median (ms)          |            - |  **14.8** |     22.3 |
| E2E median (ms)           |            - | **615.0** |    830.1 |
| Throughput median (tok/s) |            - |  **58.9** |     41.9 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
args, **kwargs)
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-8b51ede9/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[2]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1132)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1132
[3]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1133)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1133
[4]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[5]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[6]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[7]:
  time      : 2026-06-23_19:27:09
  host      : gpu-dev-8b51ede9
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_19:27:08
  host      : gpu-dev-8b51ede9
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **126.9** |  136.0 |
| TPOT median (ms)          |            - |  **28.2** |   48.9 |
| E2E median (ms)           |            - | **264.5** |  362.8 |
| Throughput median (tok/s) |            - |  **18.5** |   12.9 |
| Correctness               |            - |       99% |    99% |
