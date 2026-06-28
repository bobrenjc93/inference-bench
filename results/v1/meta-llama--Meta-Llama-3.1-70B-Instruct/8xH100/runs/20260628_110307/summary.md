# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 AM PT, Jun 28 2026

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
| torchinferno |     409.1s (6.8m) | `ed7f29b` |
| vllm         |     523.3s (8.7m) | `6eb63a1` |
| sglang       | **266.0s (4.4m)** | `828411e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     148.5 | **141.7** |
| TPOT median (ms)          |            - |  **50.5** |      74.7 |
| E2E median (ms)           |            - | **194.4** |     210.3 |
| Throughput median (tok/s) |            - |   **7.1** |       5.7 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
7/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
[rank5]:[E628 11:53:47.544493410 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 3] Process group watchdog thread terminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800087 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f13e6509611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f13e65153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f13e6516847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f13e5c915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f52b12915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 11:58:48.365000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1795 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1797 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 11:58:48.367000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1801 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
E0628 11:58:49.487000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1796) of binary: /workspace/submit-83ea8777/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1795)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1795
[2]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1797)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1797
[3]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1798)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1798
[4]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[5]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[6]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
[7]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_11:58:48
  host      : gpu-dev-83ea8777
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1796)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1796
======================================================
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **205.8** |  216.8 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **231.4** |  369.3 |
| Throughput median (tok/s) |            - |   **4.3** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
7/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
[rank5]:[E628 11:53:47.544493410 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 3] Process group watchdog thread terminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800087 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f13e6509611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f13e65153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f13e6516847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f13e5c915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f52b12915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 11:58:48.365000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1795 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1797 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 11:58:48.367000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1801 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
E0628 11:58:49.487000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1796) of binary: /workspace/submit-83ea8777/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1795)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1795
[2]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1797)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1797
[3]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1798)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1798
[4]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[5]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[6]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
[7]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_11:58:48
  host      : gpu-dev-83ea8777
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1796)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1796
======================================================
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     164.6 | **162.2** |
| TPOT median (ms)          |            - |  **57.8** |     103.1 |
| E2E median (ms)           |            - | **210.9** |     258.7 |
| Throughput median (tok/s) |            - |   **6.4** |       5.2 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
7/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
[rank5]:[E628 11:53:47.544493410 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 3] Process group watchdog thread terminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800087 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f13e6509611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f13e65153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f13e6516847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f13e5c915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f52b12915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 11:58:48.365000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1795 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1797 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 11:58:48.367000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1801 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
E0628 11:58:49.487000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1796) of binary: /workspace/submit-83ea8777/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1795)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1795
[2]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1797)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1797
[3]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1798)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1798
[4]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[5]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[6]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
[7]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_11:58:48
  host      : gpu-dev-83ea8777
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1796)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1796
======================================================
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **62.9** |   82.0 |
| TPOT median (ms)          |            - | **31.0** |   55.2 |
| E2E median (ms)           |            - | **85.7** |  146.4 |
| Throughput median (tok/s) |            - | **14.4** |    9.5 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
7/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
[rank5]:[E628 11:53:47.544493410 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 3] Process group watchdog thread terminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800087 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f13e6509611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f13e65153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f13e6516847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f13e5c915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f52b12915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 11:58:48.365000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1795 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1797 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 11:58:48.367000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1801 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
E0628 11:58:49.487000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1796) of binary: /workspace/submit-83ea8777/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1795)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1795
[2]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1797)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1797
[3]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1798)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1798
[4]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[5]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[6]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
[7]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_11:58:48
  host      : gpu-dev-83ea8777
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1796)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1796
======================================================
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      77.5 | **70.3** |
| TPOT median (ms)          |            - |  **14.8** |     22.6 |
| E2E median (ms)           |            - | **633.6** |    830.0 |
| Throughput median (tok/s) |            - |  **58.7** |     41.5 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
7/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
[rank5]:[E628 11:53:47.544493410 ProcessGroupNCCL.cpp:2197] [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 3] Process group watchdog thread terminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800087 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f13e6509611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f13e65153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f13e6516847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f149ad6afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f13e5c915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f146ba6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f149bf95aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f149c022c6c in /lib/x86_64-linux-gnu/libc.so.6)

  what():  [PG ID 0 PG GUID 0(default_pg) Rank 5] Process group watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=77, OpType=SCATTER, NumelIn=29360128, NumelOut=0, Timeout(ms)=1800000) ran for 1800047 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:760 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2b1 (0x7f52b1b09611 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x14f1 (0x7f52b1b153b1 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f52b1b16847 in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f536636afad in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x6915eb (0x7f52b12915eb in /workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f533706edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f5367501aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f536758ec6c in /lib/x86_64-linux-gnu/libc.so.6)

W0628 11:58:48.365000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1795 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1797 closing signal SIGTERM
W0628 11:58:48.366000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1798 closing signal SIGTERM
W0628 11:58:48.367000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1799 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1800 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1801 closing signal SIGTERM
W0628 11:58:48.368000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1014] Sending process 1802 closing signal SIGTERM
E0628 11:58:49.487000 999 builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:988] failed (exitcode: -6) local_rank: 1 (pid: 1796) of binary: /workspace/submit-83ea8777/builds/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1020, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 367, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1016, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 1007, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 191, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-83ea8777/builds/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 371, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1795)  (SIGTERM)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1795
[2]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1797)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1797
[3]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 3 (local_rank: 3)
  exitcode  : -6 (pid: 1798)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1798
[4]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 4 (local_rank: 4)
  exitcode  : -6 (pid: 1799)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1799
[5]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 5 (local_rank: 5)
  exitcode  : -6 (pid: 1800)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1800
[6]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 6 (local_rank: 6)
  exitcode  : -6 (pid: 1801)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1801
[7]:
  time      : 2026-06-28_11:58:49
  host      : gpu-dev-83ea8777
  rank      : 7 (local_rank: 7)
  exitcode  : -6 (pid: 1802)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1802
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-28_11:58:48
  host      : gpu-dev-83ea8777
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1796)  (SIGABRT)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1796
======================================================
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **131.9** |  134.6 |
| TPOT median (ms)          |            - |  **30.8** |   51.1 |
| E2E median (ms)           |            - | **271.2** |  363.0 |
| Throughput median (tok/s) |            - |  **18.2** |   12.9 |
| Correctness               |            - |       99% |    99% |
