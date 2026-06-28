# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, Jun 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     404.7s (6.7m) | `467c3c3` |
| vllm         |     546.8s (9.1m) | `6eb63a1` |
| sglang       | **251.7s (4.2m)** | `828411e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     148.2 | **146.3** |
| TPOT median (ms)          |            - |  **49.1** |      78.8 |
| E2E median (ms)           |            - | **188.4** |     220.5 |
| Throughput median (tok/s) |            - |   **7.6** |       5.6 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800009 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7fc74ff09611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7fc74ff153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7fc74ff16847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7fc74f6915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank6]:[E628 09:54:15.885613614 ProcessGroupNCCL.cpp:818] [Rank 6] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank6]:[E628 09:54:15.885638456 ProcessGroupNCCL.cpp:832] [Rank 6] To avoid data inconsistency, we are taking the entire process down.
[rank6]:[E628 09:54:15.886208728 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f0a07a915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 09:59:16.486000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1803 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1804 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1805 closing signal SIGTERM
E0628 09:59:18.010000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 3 (pid: 1801) of binary: /workspace/submit-12542fe0/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1798)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1798
[2]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[3]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[4]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
[5]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1803)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1803
[6]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1804)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1804
[7]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1805)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1805
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_09:59:16
  host      : gpu-dev-12542fe0
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
======================================================
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **194.6** |  218.9 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **219.6** |  353.6 |
| Throughput median (tok/s) |            - |   **4.6** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800009 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7fc74ff09611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7fc74ff153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7fc74ff16847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7fc74f6915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank6]:[E628 09:54:15.885613614 ProcessGroupNCCL.cpp:818] [Rank 6] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank6]:[E628 09:54:15.885638456 ProcessGroupNCCL.cpp:832] [Rank 6] To avoid data inconsistency, we are taking the entire process down.
[rank6]:[E628 09:54:15.886208728 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f0a07a915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 09:59:16.486000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1803 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1804 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1805 closing signal SIGTERM
E0628 09:59:18.010000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 3 (pid: 1801) of binary: /workspace/submit-12542fe0/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1798)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1798
[2]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[3]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[4]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
[5]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1803)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1803
[6]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1804)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1804
[7]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1805)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1805
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_09:59:16
  host      : gpu-dev-12542fe0
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
======================================================
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **164.7** |  168.1 |
| TPOT median (ms)          |            - |  **49.4** |  113.2 |
| E2E median (ms)           |            - | **209.7** |  276.6 |
| Throughput median (tok/s) |            - |   **6.4** |    4.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800009 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7fc74ff09611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7fc74ff153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7fc74ff16847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7fc74f6915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank6]:[E628 09:54:15.885613614 ProcessGroupNCCL.cpp:818] [Rank 6] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank6]:[E628 09:54:15.885638456 ProcessGroupNCCL.cpp:832] [Rank 6] To avoid data inconsistency, we are taking the entire process down.
[rank6]:[E628 09:54:15.886208728 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f0a07a915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 09:59:16.486000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1803 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1804 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1805 closing signal SIGTERM
E0628 09:59:18.010000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 3 (pid: 1801) of binary: /workspace/submit-12542fe0/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1798)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1798
[2]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[3]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[4]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
[5]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1803)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1803
[6]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1804)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1804
[7]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1805)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1805
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_09:59:16
  host      : gpu-dev-12542fe0
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
======================================================
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **62.4** |   81.3 |
| TPOT median (ms)          |            - | **32.3** |   49.7 |
| E2E median (ms)           |            - | **85.8** |  139.4 |
| Throughput median (tok/s) |            - | **14.3** |    9.5 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800009 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7fc74ff09611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7fc74ff153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7fc74ff16847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7fc74f6915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank6]:[E628 09:54:15.885613614 ProcessGroupNCCL.cpp:818] [Rank 6] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank6]:[E628 09:54:15.885638456 ProcessGroupNCCL.cpp:832] [Rank 6] To avoid data inconsistency, we are taking the entire process down.
[rank6]:[E628 09:54:15.886208728 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f0a07a915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 09:59:16.486000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1803 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1804 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1805 closing signal SIGTERM
E0628 09:59:18.010000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 3 (pid: 1801) of binary: /workspace/submit-12542fe0/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1798)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1798
[2]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[3]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[4]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
[5]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1803)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1803
[6]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1804)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1804
[7]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1805)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1805
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_09:59:16
  host      : gpu-dev-12542fe0
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
======================================================
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      73.7 | **73.4** |
| TPOT median (ms)          |            - |  **15.1** |     22.0 |
| E2E median (ms)           |            - | **623.4** |    827.7 |
| Throughput median (tok/s) |            - |  **58.4** |     42.4 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
 called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800009 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7fc74ff09611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7fc74ff153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7fc74ff16847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7fc805b6afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7fc74f6915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7fc7d546edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7fc806dbbaa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7fc806e48c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank6]:[E628 09:54:15.885613614 ProcessGroupNCCL.cpp:818] [Rank 6] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank6]:[E628 09:54:15.885638456 ProcessGroupNCCL.cpp:832] [Rank 6] To avoid data inconsistency, we are taking the entire process down.
[rank6]:[E628 09:54:15.886208728 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 6] Process group watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=78, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800043 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f0a08309611 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f0a083153b1 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f0a08316847 in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f0abe36afad in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f0a07a915eb in /workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f0a8d86edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f0abf236aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f0abf2c3c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 09:59:16.486000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
W0628 09:59:16.488000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1803 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1804 closing signal SIGTERM
W0628 09:59:16.489000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1805 closing signal SIGTERM
E0628 09:59:18.010000 1002 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 3 (pid: 1801) of binary: /workspace/submit-12542fe0/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-12542fe0/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1798)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1798
[2]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[3]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[4]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
[5]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1803)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1803
[6]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1804)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1804
[7]:
  time      : 2026-06-28_09:59:18
  host      : gpu-dev-12542fe0
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1805)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1805
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_09:59:16
  host      : gpu-dev-12542fe0
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
======================================================
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **128.7** |  137.6 |
| TPOT median (ms)          |            - |  **29.2** |   52.8 |
| E2E median (ms)           |            - | **265.4** |  363.6 |
| Throughput median (tok/s) |            - |  **18.3** |   13.0 |
| Correctness               |            - |       99% |    99% |
