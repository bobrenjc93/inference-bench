# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 AM PT, Jun 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     479.0s (8.0m) | `a180fbb` |
| vllm         |    649.8s (10.8m) | `cf57311` |
| sglang       | **320.9s (5.3m)** | `d6aacd2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **143.2** |  148.4 |
| TPOT median (ms)          |            - |  **48.7** |   77.7 |
| E2E median (ms)           |            - | **188.5** |  216.7 |
| Throughput median (tok/s) |            - |   **7.7** |    5.6 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
NFO [Proxy Progress] Device 0 CPU core 11
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1797:2394 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 119
gpu-dev-7d5e8186:1796:2395 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 46
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1798:2396 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 30
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55cb64daf560 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.56 (kernels 0.35, alloc 1.53, bootstrap 0.58, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.96, rest 0.04)
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x560a1709db70 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x56041de2ba00 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-7d5e8186:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x55b7ede6e730 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x563759d5ae50 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55a1975c0bd0 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c1508d4310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.56 (kernels 0.35, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d96402b010 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.56 (kernels 0.35, alloc gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.56 (kernels 0.35, alloc 2.04, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
2.05, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.56 (kernels 0.39, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.56 (kernels 0.35, alloc 2.10, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.56 (kernels 0.35, alloc 2.06, bootstrap 0.00, allgathers 0.00, topo 0.09, graphs 0.01, connections 0.98, rest 0.03)
2.00, bootstrap 0.11, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
1.63, bootstrap 0.48, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.00)
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.55 (kernels 0.39, alloc 2.06, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.04)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=1
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **195.1** |  217.2 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **219.2** |  365.6 |
| Throughput median (tok/s) |            - |   **4.6** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
NFO [Proxy Progress] Device 0 CPU core 11
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1797:2394 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 119
gpu-dev-7d5e8186:1796:2395 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 46
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1798:2396 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 30
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55cb64daf560 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.56 (kernels 0.35, alloc 1.53, bootstrap 0.58, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.96, rest 0.04)
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x560a1709db70 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x56041de2ba00 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-7d5e8186:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x55b7ede6e730 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x563759d5ae50 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55a1975c0bd0 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c1508d4310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.56 (kernels 0.35, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d96402b010 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.56 (kernels 0.35, alloc gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.56 (kernels 0.35, alloc 2.04, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
2.05, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.56 (kernels 0.39, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.56 (kernels 0.35, alloc 2.10, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.56 (kernels 0.35, alloc 2.06, bootstrap 0.00, allgathers 0.00, topo 0.09, graphs 0.01, connections 0.98, rest 0.03)
2.00, bootstrap 0.11, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
1.63, bootstrap 0.48, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.00)
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.55 (kernels 0.39, alloc 2.06, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.04)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=1
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     165.0 | **159.5** |
| TPOT median (ms)          |            - |  **45.2** |     111.2 |
| E2E median (ms)           |            - | **203.1** |     259.6 |
| Throughput median (tok/s) |            - |   **6.8** |       5.2 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
NFO [Proxy Progress] Device 0 CPU core 11
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1797:2394 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 119
gpu-dev-7d5e8186:1796:2395 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 46
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1798:2396 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 30
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55cb64daf560 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.56 (kernels 0.35, alloc 1.53, bootstrap 0.58, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.96, rest 0.04)
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x560a1709db70 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x56041de2ba00 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-7d5e8186:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x55b7ede6e730 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x563759d5ae50 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55a1975c0bd0 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c1508d4310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.56 (kernels 0.35, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d96402b010 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.56 (kernels 0.35, alloc gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.56 (kernels 0.35, alloc 2.04, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
2.05, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.56 (kernels 0.39, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.56 (kernels 0.35, alloc 2.10, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.56 (kernels 0.35, alloc 2.06, bootstrap 0.00, allgathers 0.00, topo 0.09, graphs 0.01, connections 0.98, rest 0.03)
2.00, bootstrap 0.11, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
1.63, bootstrap 0.48, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.00)
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.55 (kernels 0.39, alloc 2.06, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.04)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=1
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.6** |   81.9 |
| TPOT median (ms)          |            - | **29.2** |   59.5 |
| E2E median (ms)           |            - | **80.2** |  157.4 |
| Throughput median (tok/s) |            - | **15.0** |    9.3 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
NFO [Proxy Progress] Device 0 CPU core 11
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1797:2394 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 119
gpu-dev-7d5e8186:1796:2395 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 46
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1798:2396 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 30
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55cb64daf560 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.56 (kernels 0.35, alloc 1.53, bootstrap 0.58, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.96, rest 0.04)
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x560a1709db70 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x56041de2ba00 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-7d5e8186:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x55b7ede6e730 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x563759d5ae50 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55a1975c0bd0 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c1508d4310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.56 (kernels 0.35, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d96402b010 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.56 (kernels 0.35, alloc gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.56 (kernels 0.35, alloc 2.04, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
2.05, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.56 (kernels 0.39, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.56 (kernels 0.35, alloc 2.10, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.56 (kernels 0.35, alloc 2.06, bootstrap 0.00, allgathers 0.00, topo 0.09, graphs 0.01, connections 0.98, rest 0.03)
2.00, bootstrap 0.11, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
1.63, bootstrap 0.48, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.00)
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.55 (kernels 0.39, alloc 2.06, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.04)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=1
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      75.0 | **71.2** |
| TPOT median (ms)          |            - |  **14.8** |     22.3 |
| E2E median (ms)           |            - | **622.5** |    840.9 |
| Throughput median (tok/s) |            - |  **59.1** |     42.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
NFO [Proxy Progress] Device 0 CPU core 11
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1797:2394 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 119
gpu-dev-7d5e8186:1796:2395 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 46
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1798:2396 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 30
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55cb64daf560 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.56 (kernels 0.35, alloc 1.53, bootstrap 0.58, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.96, rest 0.04)
gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x560a1709db70 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x56041de2ba00 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-7d5e8186:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x55b7ede6e730 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x563759d5ae50 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55a1975c0bd0 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c1508d4310 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-7d5e8186:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.56 (kernels 0.35, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d96402b010 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.56 (kernels 0.35, alloc gpu-dev-7d5e8186:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.56 (kernels 0.35, alloc 2.04, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
2.05, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.56 (kernels 0.39, alloc 000 commId 0xd5d1c00bcbb9dc1d - Init COMPLETE
gpu-dev-7d5e8186:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.56 (kernels 0.35, alloc 2.10, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-7d5e8186:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.56 (kernels 0.35, alloc 2.06, bootstrap 0.00, allgathers 0.00, topo 0.09, graphs 0.01, connections 0.98, rest 0.03)
2.00, bootstrap 0.11, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
1.63, bootstrap 0.48, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.00, rest 0.00)
gpu-dev-7d5e8186:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.55 (kernels 0.39, alloc 2.06, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.97, rest 0.04)
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=1
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **127.4** |  135.6 |
| TPOT median (ms)          |            - |  **27.6** |   54.2 |
| E2E median (ms)           |            - | **262.7** |  368.0 |
| Throughput median (tok/s) |            - |  **18.6** |   13.0 |
| Correctness               |            - |       99% |    99% |
