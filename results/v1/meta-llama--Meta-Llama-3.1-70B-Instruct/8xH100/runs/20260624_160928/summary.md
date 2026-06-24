# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jun 24 2026

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
| torchinferno |     439.1s (7.3m) | `8546437` |
| vllm         |     547.8s (9.1m) | `1cd3e0e` |
| sglang       | **282.3s (4.7m)** | `4a4f063` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **136.9** |  151.2 |
| TPOT median (ms)          |            - |  **47.8** |   77.6 |
| E2E median (ms)           |            - | **180.0** |  225.6 |
| Throughput median (tok/s) |            - |   **7.8** |    5.3 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
u-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1795:2393 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 127
gpu-dev-57704f5a:1799:2394 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 60
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-57704f5a:1793:1793 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO ncclCommInitRankConfig comm 0x55580bc0bab0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO ncclCommInitRankConfig comm 0x561cf22c7920 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-57704f5a:1796:1796 [3] NCCL INFO ncclCommInitRankConfig comm 0x55f179799370 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.16, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.72 (kernels 0.35, alloc gpu-dev-57704f5a:1794:1794 [1] NCCL INFO ncclCommInitRankConfig comm 0x5630b9bfa310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.72 (kernels 0.39, alloc 2.12, bootstrap 0.13, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.21, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.02)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO ncclCommInitRankConfig comm 0x555f799c2090 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.72 (kernels 0.35, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO ncclCommInitRankConfig comm 0x55d3e368c020 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-57704f5a:1795:1795 [2] NCCL INFO ncclCommInitRankConfig comm 0x55c5f3c6fe30 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 752.19, bootstrap 0.07, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO ncclCommInitRankConfig comm 0x56107b04aee0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.72 (kernels 0.35, alloc 2.22, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.72 (kernels 0.39, alloc gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.72 (kernels 0.35, alloc 2.06, bootstrap 0.19, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.01)
2.20, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.02)
1.84, bootstrap 0.42, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.00)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0
[Llama3TP] loaded 10/80 layers in 612.9s
[Llama3TP] loaded 20/80 layers in 835.6s
[Llama3TP] loaded 30/80 layers in 1032.8s
[Llama3TP] loaded 40/80 layers in 1214.5s
[Llama3TP] loaded 50/80 layers in 1392.8s
[Llama3TP] loaded 60/80 layers in 1581.1s
[Llama3TP] loaded 70/80 layers in 1745.0s
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **183.9** |  215.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **241.3** |  367.6 |
| Throughput median (tok/s) |            - |   **4.1** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
u-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1795:2393 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 127
gpu-dev-57704f5a:1799:2394 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 60
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-57704f5a:1793:1793 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO ncclCommInitRankConfig comm 0x55580bc0bab0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO ncclCommInitRankConfig comm 0x561cf22c7920 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-57704f5a:1796:1796 [3] NCCL INFO ncclCommInitRankConfig comm 0x55f179799370 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.16, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.72 (kernels 0.35, alloc gpu-dev-57704f5a:1794:1794 [1] NCCL INFO ncclCommInitRankConfig comm 0x5630b9bfa310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.72 (kernels 0.39, alloc 2.12, bootstrap 0.13, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.21, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.02)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO ncclCommInitRankConfig comm 0x555f799c2090 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.72 (kernels 0.35, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO ncclCommInitRankConfig comm 0x55d3e368c020 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-57704f5a:1795:1795 [2] NCCL INFO ncclCommInitRankConfig comm 0x55c5f3c6fe30 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 752.19, bootstrap 0.07, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO ncclCommInitRankConfig comm 0x56107b04aee0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.72 (kernels 0.35, alloc 2.22, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.72 (kernels 0.39, alloc gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.72 (kernels 0.35, alloc 2.06, bootstrap 0.19, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.01)
2.20, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.02)
1.84, bootstrap 0.42, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.00)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0
[Llama3TP] loaded 10/80 layers in 612.9s
[Llama3TP] loaded 20/80 layers in 835.6s
[Llama3TP] loaded 30/80 layers in 1032.8s
[Llama3TP] loaded 40/80 layers in 1214.5s
[Llama3TP] loaded 50/80 layers in 1392.8s
[Llama3TP] loaded 60/80 layers in 1581.1s
[Llama3TP] loaded 70/80 layers in 1745.0s
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **156.6** |  157.6 |
| TPOT median (ms)          |            - |  **57.3** |  100.2 |
| E2E median (ms)           |            - | **202.2** |  255.0 |
| Throughput median (tok/s) |            - |   **6.6** |    5.3 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
u-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1795:2393 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 127
gpu-dev-57704f5a:1799:2394 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 60
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-57704f5a:1793:1793 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO ncclCommInitRankConfig comm 0x55580bc0bab0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO ncclCommInitRankConfig comm 0x561cf22c7920 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-57704f5a:1796:1796 [3] NCCL INFO ncclCommInitRankConfig comm 0x55f179799370 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.16, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.72 (kernels 0.35, alloc gpu-dev-57704f5a:1794:1794 [1] NCCL INFO ncclCommInitRankConfig comm 0x5630b9bfa310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.72 (kernels 0.39, alloc 2.12, bootstrap 0.13, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.21, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.02)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO ncclCommInitRankConfig comm 0x555f799c2090 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.72 (kernels 0.35, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO ncclCommInitRankConfig comm 0x55d3e368c020 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-57704f5a:1795:1795 [2] NCCL INFO ncclCommInitRankConfig comm 0x55c5f3c6fe30 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 752.19, bootstrap 0.07, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO ncclCommInitRankConfig comm 0x56107b04aee0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.72 (kernels 0.35, alloc 2.22, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.72 (kernels 0.39, alloc gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.72 (kernels 0.35, alloc 2.06, bootstrap 0.19, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.01)
2.20, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.02)
1.84, bootstrap 0.42, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.00)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0
[Llama3TP] loaded 10/80 layers in 612.9s
[Llama3TP] loaded 20/80 layers in 835.6s
[Llama3TP] loaded 30/80 layers in 1032.8s
[Llama3TP] loaded 40/80 layers in 1214.5s
[Llama3TP] loaded 50/80 layers in 1392.8s
[Llama3TP] loaded 60/80 layers in 1581.1s
[Llama3TP] loaded 70/80 layers in 1745.0s
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.3** |   81.2 |
| TPOT median (ms)          |            - | **28.4** |   40.2 |
| E2E median (ms)           |            - | **80.9** |  131.3 |
| Throughput median (tok/s) |            - | **15.4** |   10.3 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
u-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1795:2393 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 127
gpu-dev-57704f5a:1799:2394 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 60
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-57704f5a:1793:1793 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO ncclCommInitRankConfig comm 0x55580bc0bab0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO ncclCommInitRankConfig comm 0x561cf22c7920 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-57704f5a:1796:1796 [3] NCCL INFO ncclCommInitRankConfig comm 0x55f179799370 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.16, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.72 (kernels 0.35, alloc gpu-dev-57704f5a:1794:1794 [1] NCCL INFO ncclCommInitRankConfig comm 0x5630b9bfa310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.72 (kernels 0.39, alloc 2.12, bootstrap 0.13, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.21, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.02)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO ncclCommInitRankConfig comm 0x555f799c2090 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.72 (kernels 0.35, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO ncclCommInitRankConfig comm 0x55d3e368c020 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-57704f5a:1795:1795 [2] NCCL INFO ncclCommInitRankConfig comm 0x55c5f3c6fe30 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 752.19, bootstrap 0.07, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO ncclCommInitRankConfig comm 0x56107b04aee0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.72 (kernels 0.35, alloc 2.22, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.72 (kernels 0.39, alloc gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.72 (kernels 0.35, alloc 2.06, bootstrap 0.19, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.01)
2.20, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.02)
1.84, bootstrap 0.42, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.00)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0
[Llama3TP] loaded 10/80 layers in 612.9s
[Llama3TP] loaded 20/80 layers in 835.6s
[Llama3TP] loaded 30/80 layers in 1032.8s
[Llama3TP] loaded 40/80 layers in 1214.5s
[Llama3TP] loaded 50/80 layers in 1392.8s
[Llama3TP] loaded 60/80 layers in 1581.1s
[Llama3TP] loaded 70/80 layers in 1745.0s
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      79.7 | **69.6** |
| TPOT median (ms)          |            - |  **14.9** |     22.8 |
| E2E median (ms)           |            - | **634.0** |    848.9 |
| Throughput median (tok/s) |            - |  **57.8** |     41.4 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
u-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1795:2393 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 127
gpu-dev-57704f5a:1799:2394 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 60
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-57704f5a:1793:1793 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-57704f5a:1800:1800 [7] NCCL INFO ncclCommInitRankConfig comm 0x55580bc0bab0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO ncclCommInitRankConfig comm 0x561cf22c7920 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-57704f5a:1796:1796 [3] NCCL INFO ncclCommInitRankConfig comm 0x55f179799370 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-57704f5a:1800:1800 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.16, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1798:1798 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.72 (kernels 0.35, alloc gpu-dev-57704f5a:1794:1794 [1] NCCL INFO ncclCommInitRankConfig comm 0x5630b9bfa310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-57704f5a:1796:1796 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.72 (kernels 0.39, alloc 2.12, bootstrap 0.13, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
2.21, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.02)
gpu-dev-57704f5a:1799:1799 [6] NCCL INFO ncclCommInitRankConfig comm 0x555f799c2090 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-57704f5a:1794:1794 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.72 (kernels 0.35, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO ncclCommInitRankConfig comm 0x55d3e368c020 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-57704f5a:1795:1795 [2] NCCL INFO ncclCommInitRankConfig comm 0x55c5f3c6fe30 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 752.19, bootstrap 0.07, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1793:1793 [0] NCCL INFO ncclCommInitRankConfig comm 0x56107b04aee0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-57704f5a:1799:1799 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.72 (kernels 0.38, alloc 000 commId 0xf9c27b9b4212767e - Init COMPLETE
000 commId 0xf9c27b9b4212767e - Init COMPLETE
gpu-dev-57704f5a:1797:1797 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.72 (kernels 0.35, alloc 2.22, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-57704f5a:1795:1795 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.72 (kernels 0.39, alloc gpu-dev-57704f5a:1793:1793 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.72 (kernels 0.35, alloc 2.06, bootstrap 0.19, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.01, rest 0.01)
2.20, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.02)
1.84, bootstrap 0.42, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.00)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0
[Llama3TP] loaded 10/80 layers in 612.9s
[Llama3TP] loaded 20/80 layers in 835.6s
[Llama3TP] loaded 30/80 layers in 1032.8s
[Llama3TP] loaded 40/80 layers in 1214.5s
[Llama3TP] loaded 50/80 layers in 1392.8s
[Llama3TP] loaded 60/80 layers in 1581.1s
[Llama3TP] loaded 70/80 layers in 1745.0s
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **123.1** |  135.0 |
| TPOT median (ms)          |            - |  **29.7** |   48.1 |
| E2E median (ms)           |            - | **267.7** |  365.7 |
| Throughput median (tok/s) |            - |  **18.3** |   13.0 |
| Correctness               |            - |       98% |    99% |
