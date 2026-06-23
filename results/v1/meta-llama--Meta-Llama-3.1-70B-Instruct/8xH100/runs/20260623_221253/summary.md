# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 PM PT, Jun 23 2026

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
| torchinferno |     405.7s (6.8m) | `5ad5429` |
| vllm         |     523.2s (8.7m) | `abc3313` |
| sglang       | **269.8s (4.5m)** | `11e7c9e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **137.4** |  143.7 |
| TPOT median (ms)          |            - |  **48.5** |   72.8 |
| E2E median (ms)           |            - | **177.9** |  211.1 |
| Throughput median (tok/s) |            - |   **7.8** |    5.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
erminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600007 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f3e6f709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f3e6f7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f3e6f716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f3e6ee915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

gpu-dev-7ab11a40:1138:1684 [5] NCCL INFO comm 0x55d0ccb13020 rank 5 nranks 8 cudaDev 5 busId a8000 - Abort COMPLETE
[rank5]:[E623 21:21:18.894757790 ProcessGroupNCCL.cpp:818] [Rank 5] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank5]:[E623 21:21:18.894772491 ProcessGroupNCCL.cpp:832] [Rank 5] To avoid data inconsistency, we are taking the entire process down.
[rank5]:[E623 21:21:18.895381245 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f571be915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0623 21:26:19.639000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1133 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1135 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1136 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1137 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1138 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1139 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1140 closing signal SIGTERM
E0623 21:26:20.461000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1134) of binary: /workspace/submit-7ab11a40/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1133)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1133
[2]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[3]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[4]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[5]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[6]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
[7]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1140)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1140
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_21:26:19
  host      : gpu-dev-7ab11a40
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **197.1** |  215.8 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **240.7** |  356.5 |
| Throughput median (tok/s) |            - |   **4.2** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
erminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600007 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f3e6f709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f3e6f7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f3e6f716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f3e6ee915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

gpu-dev-7ab11a40:1138:1684 [5] NCCL INFO comm 0x55d0ccb13020 rank 5 nranks 8 cudaDev 5 busId a8000 - Abort COMPLETE
[rank5]:[E623 21:21:18.894757790 ProcessGroupNCCL.cpp:818] [Rank 5] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank5]:[E623 21:21:18.894772491 ProcessGroupNCCL.cpp:832] [Rank 5] To avoid data inconsistency, we are taking the entire process down.
[rank5]:[E623 21:21:18.895381245 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f571be915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0623 21:26:19.639000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1133 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1135 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1136 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1137 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1138 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1139 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1140 closing signal SIGTERM
E0623 21:26:20.461000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1134) of binary: /workspace/submit-7ab11a40/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1133)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1133
[2]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[3]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[4]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[5]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[6]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
[7]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1140)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1140
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_21:26:19
  host      : gpu-dev-7ab11a40
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **167.3** |  168.2 |
| TPOT median (ms)          |            - |  **54.7** |  116.7 |
| E2E median (ms)           |            - | **214.5** |  283.9 |
| Throughput median (tok/s) |            - |   **6.3** |    4.9 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
erminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600007 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f3e6f709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f3e6f7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f3e6f716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f3e6ee915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

gpu-dev-7ab11a40:1138:1684 [5] NCCL INFO comm 0x55d0ccb13020 rank 5 nranks 8 cudaDev 5 busId a8000 - Abort COMPLETE
[rank5]:[E623 21:21:18.894757790 ProcessGroupNCCL.cpp:818] [Rank 5] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank5]:[E623 21:21:18.894772491 ProcessGroupNCCL.cpp:832] [Rank 5] To avoid data inconsistency, we are taking the entire process down.
[rank5]:[E623 21:21:18.895381245 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f571be915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0623 21:26:19.639000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1133 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1135 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1136 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1137 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1138 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1139 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1140 closing signal SIGTERM
E0623 21:26:20.461000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1134) of binary: /workspace/submit-7ab11a40/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1133)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1133
[2]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[3]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[4]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[5]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[6]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
[7]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1140)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1140
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_21:26:19
  host      : gpu-dev-7ab11a40
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **62.1** |   87.4 |
| TPOT median (ms)          |            - | **31.3** |   48.4 |
| E2E median (ms)           |            - | **86.3** |  153.4 |
| Throughput median (tok/s) |            - | **14.5** |    9.2 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
erminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600007 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f3e6f709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f3e6f7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f3e6f716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f3e6ee915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

gpu-dev-7ab11a40:1138:1684 [5] NCCL INFO comm 0x55d0ccb13020 rank 5 nranks 8 cudaDev 5 busId a8000 - Abort COMPLETE
[rank5]:[E623 21:21:18.894757790 ProcessGroupNCCL.cpp:818] [Rank 5] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank5]:[E623 21:21:18.894772491 ProcessGroupNCCL.cpp:832] [Rank 5] To avoid data inconsistency, we are taking the entire process down.
[rank5]:[E623 21:21:18.895381245 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f571be915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0623 21:26:19.639000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1133 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1135 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1136 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1137 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1138 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1139 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1140 closing signal SIGTERM
E0623 21:26:20.461000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1134) of binary: /workspace/submit-7ab11a40/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1133)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1133
[2]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[3]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[4]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[5]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[6]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
[7]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1140)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1140
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_21:26:19
  host      : gpu-dev-7ab11a40
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      80.1 | **74.8** |
| TPOT median (ms)          |            - |  **14.9** |     21.9 |
| E2E median (ms)           |            - | **630.6** |    852.9 |
| Throughput median (tok/s) |            - |  **58.0** |     42.4 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
erminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600007 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f3e6f709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f3e6f7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f3e6f716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f3f2436afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f3e6ee915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f3ef4c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f3f252aaaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f3f25337c6c in /lib/x86_64-linux-gnu/libc.so.6)

gpu-dev-7ab11a40:1138:1684 [5] NCCL INFO comm 0x55d0ccb13020 rank 5 nranks 8 cudaDev 5 busId a8000 - Abort COMPLETE
[rank5]:[E623 21:21:18.894757790 ProcessGroupNCCL.cpp:818] [Rank 5] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank5]:[E623 21:21:18.894772491 ProcessGroupNCCL.cpp:832] [Rank 5] To avoid data inconsistency, we are taking the entire process down.
[rank5]:[E623 21:21:18.895381245 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=10, OpType=BROADCAST, NumelIn=234881024, NumelOut=234881024, Timeout(ms)=600000) ran for 600021 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f571c709611 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f571c7153b1 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f571c716847 in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f57d0f6afad in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f571be915eb in /workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f57a1c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f57d21d8aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f57d2265c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0623 21:26:19.639000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1133 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1135 closing signal SIGTERM
W0623 21:26:19.640000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1136 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1137 closing signal SIGTERM
W0623 21:26:19.641000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1138 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1139 closing signal SIGTERM
W0623 21:26:19.642000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1140 closing signal SIGTERM
E0623 21:26:20.461000 1000 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1134) of binary: /workspace/submit-7ab11a40/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-7ab11a40/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1133)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1133
[2]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1135)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1135
[3]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1136)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1136
[4]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1137)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1137
[5]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1138)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1138
[6]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1139)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1139
[7]:
  time      : 2026-06-23_21:26:20
  host      : gpu-dev-7ab11a40
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1140)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1140
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-23_21:26:19
  host      : gpu-dev-7ab11a40
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1134)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1134
======================================================
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **128.8** |  138.0 |
| TPOT median (ms)          |            - |  **29.9** |   52.0 |
| E2E median (ms)           |            - | **270.0** |  371.6 |
| Throughput median (tok/s) |            - |  **18.1** |   13.0 |
| Correctness               |            - |       98% |    99% |
