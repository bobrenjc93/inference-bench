# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `aa2e4cccddb1a1b8f8a43e8aa23af795e3c87d7c`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** vllm=4/4, sglang=4/4
- **Observed GPU products:** vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`2d2dcfc5e2c7cb8420383ad7cbf872c43fb67ea2`; vllm=`9e6746b3c7b4ec9bcc234db9a654df8eca5781ce` + build patch `d22bf8e0c0e1802dc97fcb8743d32ecc762682c00f595f2b82434af9f0b94ca6`; sglang=`be7cc173075c1c906f9a6589d04ba20eb03064d5` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 PM PT, Jul 24 2026

## Integrity Warnings

- **torchinferno:** TorchInferno score-facing cache integrity could not be verified (queue profile is missing). Treat TorchInferno metrics in this run as not comparable.
- **torchinferno:** Provider reported benchmark or deployment errors under the result eligibility policy.
- **torchinferno:** Benchmark 'few_shot' has no completed result.
- **torchinferno:** Benchmark 'self_consistency' has no completed result.
- **torchinferno:** Benchmark 'multi_turn' has no completed result.
- **torchinferno:** Benchmark 'tree_of_thought' has no completed result.
- **torchinferno:** Benchmark 'long_output' has no completed result.

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          N/C |       1/4 | **3/4** |
| self_consistency |          N/C |   **3/4** |     0/4 |
| multi_turn       |          N/C |   **3/4** |     1/4 |
| tree_of_thought  |          N/C |   **4/4** |     0/4 |
| long_output      |          N/C |   **3/4** |     1/4 |
| **Total**        |          N/C | **14/20** |    5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.
N/C = excluded from scoring because integrity validation did not pass.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     343.1s (5.7m) | `2d2dcfc` |
| vllm         |     200.7s (3.3m) | `9e6746b` |
| sglang       | **190.4s (3.2m)** | `be7cc17` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |     98.0 |  **80.3** |
| TPOT median (ms)          |            - | **58.2** |      71.3 |
| E2E median (ms)           |            - |    148.0 | **139.6** |
| Throughput median (tok/s) |            - |      9.5 |   **9.6** |
| Correctness               |            - |      98% |       98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
oupNCCL.cpp:750] [Rank 2] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank2]:[E724 20:42:34.306638268 ProcessGroupNCCL.cpp:764] [Rank 2] To avoid data inconsistency, we are taking the entire process down.
[rank1]:[E724 20:42:34.306947846 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7f782168ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank2]:[E724 20:42:34.307280375 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7ff59988ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0724 20:47:35.221000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1733 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1735 closing signal SIGTERM
E0724 20:47:36.140000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 2 (pid: 1734) of binary: /workspace/submit-1549413b/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1732
[2]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1733)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1733
[3]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1735)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1735
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-24_20:47:35
  host      : gpu-dev-1549413b
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1734)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1734
======================================================
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **108.0** |  137.6 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **126.8** |  216.5 |
| Throughput median (tok/s) |            - |   **7.9** |    4.6 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
oupNCCL.cpp:750] [Rank 2] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank2]:[E724 20:42:34.306638268 ProcessGroupNCCL.cpp:764] [Rank 2] To avoid data inconsistency, we are taking the entire process down.
[rank1]:[E724 20:42:34.306947846 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7f782168ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank2]:[E724 20:42:34.307280375 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7ff59988ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0724 20:47:35.221000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1733 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1735 closing signal SIGTERM
E0724 20:47:36.140000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 2 (pid: 1734) of binary: /workspace/submit-1549413b/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1732
[2]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1733)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1733
[3]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1735)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1735
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-24_20:47:35
  host      : gpu-dev-1549413b
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1734)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1734
======================================================
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |     102.7 | **85.3** |
| TPOT median (ms)          |            - |  **58.1** |     82.7 |
| E2E median (ms)           |            - | **149.1** |    152.4 |
| Throughput median (tok/s) |            - |   **9.4** |      9.1 |
| Correctness               |            - |       98% |      98% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
oupNCCL.cpp:750] [Rank 2] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank2]:[E724 20:42:34.306638268 ProcessGroupNCCL.cpp:764] [Rank 2] To avoid data inconsistency, we are taking the entire process down.
[rank1]:[E724 20:42:34.306947846 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7f782168ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank2]:[E724 20:42:34.307280375 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7ff59988ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0724 20:47:35.221000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1733 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1735 closing signal SIGTERM
E0724 20:47:36.140000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 2 (pid: 1734) of binary: /workspace/submit-1549413b/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1732
[2]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1733)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1733
[3]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1735)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1735
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-24_20:47:35
  host      : gpu-dev-1549413b
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1734)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1734
======================================================
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **49.1** |   56.8 |
| TPOT median (ms)          |            - | **34.3** |  124.6 |
| E2E median (ms)           |            - | **73.4** |  214.1 |
| Throughput median (tok/s) |            - | **16.6** |    6.6 |
| Correctness               |            - |      97% |    96% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
oupNCCL.cpp:750] [Rank 2] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank2]:[E724 20:42:34.306638268 ProcessGroupNCCL.cpp:764] [Rank 2] To avoid data inconsistency, we are taking the entire process down.
[rank1]:[E724 20:42:34.306947846 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7f782168ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank2]:[E724 20:42:34.307280375 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7ff59988ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0724 20:47:35.221000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1733 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1735 closing signal SIGTERM
E0724 20:47:36.140000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 2 (pid: 1734) of binary: /workspace/submit-1549413b/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1732
[2]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1733)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1733
[3]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1735)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1735
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-24_20:47:35
  host      : gpu-dev-1549413b
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1734)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1734
======================================================
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      62.8 | **55.7** |
| TPOT median (ms)          |            - |  **21.3** |     29.9 |
| E2E median (ms)           |            - | **813.0** |   1075.9 |
| Throughput median (tok/s) |            - |  **43.8** |     32.6 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server process exited with code 1.
Log tail:
oupNCCL.cpp:750] [Rank 2] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank2]:[E724 20:42:34.306638268 ProcessGroupNCCL.cpp:764] [Rank 2] To avoid data inconsistency, we are taking the entire process down.
[rank1]:[E724 20:42:34.306947846 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800058 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7f7821f02ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7f7821f07fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7f7821f093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7f78d5f7305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7f782168ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7f78a6c6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7f78d7187aa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7f78d7214c6c in /lib/x86_64-linux-gnu/libc.so.6)

[rank2]:[E724 20:42:34.307280375 ProcessGroupNCCL.cpp:2119] [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG ID 0 PG GUID 0(default_pg) Rank 2] Process group watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=2415, OpType=ALLREDUCE, NumelIn=8192, NumelOut=8192, Timeout(ms)=1800000) ran for 1800077 milliseconds before timing out.
Exception raised from checkTimeout at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:692 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x2a7 (0x7ff59a102ba7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::Watchdog::runLoop() + 0x17b1 (0x7ff59a107fc1 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::Watchdog::run() + 0x157 (0x7ff59a1093b7 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from run at /pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2125 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9d (0x7ff64e17305d in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x68ef03 (0x7ff59988ef03 in /workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xecdb4 (0x7ff61ee6edb4 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x9caa4 (0x7ff64f40baa4 in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x129c6c (0x7ff64f498c6c in /lib/x86_64-linux-gnu/libc.so.6)

W0724 20:47:35.221000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1732 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1733 closing signal SIGTERM
W0724 20:47:35.222000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:1012] Sending process 1735 closing signal SIGTERM
E0724 20:47:36.140000 1237 venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/api.py:986] failed (exitcode: -6) local_rank: 2 (pid: 1734) of binary: /workspace/submit-1549413b/builds/v3/torchinferno/venv/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 994, in <module>
    main()
    ~~~~^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 362, in wrapper
    return f(*args, **kwargs)
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 990, in main
    run(args)
    ~~~^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/run.py", line 981, in run
    elastic_launch(
    ~~~~~~~~~~~~~~~
        config=config,
        ~~~~~~~~~~~~~~
        entrypoint=cmd,
        ~~~~~~~~~~~~~~~
    )(*cmd_args)
    ~^^^^^^^^^^^
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 170, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/workspace/submit-1549413b/builds/v3/torchinferno/venv/lib/python3.13/site-packages/torch/distributed/launcher/api.py", line 317, in launch_agent
    raise ChildFailedError(
    ...<2 lines>...
    )
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
======================================================
torchinferno.openai_server FAILED
------------------------------------------------------
Failures:
[1]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 0 (local_rank: 0)
  exitcode  : -15 (pid: 1732)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1732
[2]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 1 (local_rank: 1)
  exitcode  : -6 (pid: 1733)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1733
[3]:
  time      : 2026-07-24_20:47:36
  host      : gpu-dev-1549413b
  rank      : 3 (local_rank: 3)
  exitcode  : -15 (pid: 1735)
  error_file: <N/A>
  traceback : Signal 15 (SIGTERM) received by PID 1735
------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-07-24_20:47:35
  host      : gpu-dev-1549413b
  rank      : 2 (local_rank: 2)
  exitcode  : -6 (pid: 1734)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 1734
======================================================
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      84.1 | **83.1** |
| TPOT median (ms)          |            - |  **34.4** |     61.7 |
| E2E median (ms)           |            - | **262.1** |    359.7 |
| Throughput median (tok/s) |            - |  **17.4** |     12.5 |
| Correctness               |            - |       98% |      98% |
