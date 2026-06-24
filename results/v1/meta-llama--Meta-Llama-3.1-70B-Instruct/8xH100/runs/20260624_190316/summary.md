# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 PM PT, Jun 24 2026

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
| torchinferno |     445.1s (7.4m) | `76107de` |
| vllm         |    612.2s (10.2m) | `49f2104` |
| sglang       | **295.7s (4.9m)** | `d5e9176` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     143.6 | **142.3** |
| TPOT median (ms)          |            - |  **47.8** |      76.2 |
| E2E median (ms)           |            - | **188.0** |     211.7 |
| Throughput median (tok/s) |            - |   **7.6** |       5.6 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
ess] Device 3 CPU core 19
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-380a2107:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x56339b5a3930 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d85cc955e0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-380a2107:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x56220f0efa00 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.21, bootstrap 0.03, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x562f0f6e5af0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x55d973739e00 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-380a2107:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x5640fc9ce9f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-380a2107:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x55d3fa60a4b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a82.15, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x5635d3121940 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd0d2de678d972b12 - Init COMPLETE
000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.23, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
1.46, bootstrap 0.79, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.33, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.34, alloc 1.23, bootstrap 1.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
2.20, bootstrap 0.04, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.99, rest 0.04)
2.19, bootstrap 0.04, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **185.5** |  199.7 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **235.5** |  331.6 |
| Throughput median (tok/s) |            - |   **4.2** |    3.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
ess] Device 3 CPU core 19
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-380a2107:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x56339b5a3930 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d85cc955e0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-380a2107:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x56220f0efa00 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.21, bootstrap 0.03, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x562f0f6e5af0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x55d973739e00 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-380a2107:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x5640fc9ce9f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-380a2107:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x55d3fa60a4b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a82.15, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x5635d3121940 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd0d2de678d972b12 - Init COMPLETE
000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.23, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
1.46, bootstrap 0.79, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.33, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.34, alloc 1.23, bootstrap 1.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
2.20, bootstrap 0.04, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.99, rest 0.04)
2.19, bootstrap 0.04, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **156.8** |  170.1 |
| TPOT median (ms)          |            - |  **57.1** |   95.9 |
| E2E median (ms)           |            - | **204.4** |  266.0 |
| Throughput median (tok/s) |            - |   **6.6** |    5.0 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
ess] Device 3 CPU core 19
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-380a2107:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x56339b5a3930 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d85cc955e0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-380a2107:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x56220f0efa00 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.21, bootstrap 0.03, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x562f0f6e5af0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x55d973739e00 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-380a2107:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x5640fc9ce9f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-380a2107:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x55d3fa60a4b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a82.15, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x5635d3121940 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd0d2de678d972b12 - Init COMPLETE
000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.23, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
1.46, bootstrap 0.79, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.33, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.34, alloc 1.23, bootstrap 1.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
2.20, bootstrap 0.04, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.99, rest 0.04)
2.19, bootstrap 0.04, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.5** |   87.2 |
| TPOT median (ms)          |            - | **29.7** |   36.4 |
| E2E median (ms)           |            - | **82.1** |  135.0 |
| Throughput median (tok/s) |            - | **14.8** |    9.8 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
ess] Device 3 CPU core 19
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-380a2107:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x56339b5a3930 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d85cc955e0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-380a2107:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x56220f0efa00 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.21, bootstrap 0.03, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x562f0f6e5af0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x55d973739e00 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-380a2107:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x5640fc9ce9f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-380a2107:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x55d3fa60a4b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a82.15, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x5635d3121940 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd0d2de678d972b12 - Init COMPLETE
000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.23, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
1.46, bootstrap 0.79, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.33, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.34, alloc 1.23, bootstrap 1.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
2.20, bootstrap 0.04, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.99, rest 0.04)
2.19, bootstrap 0.04, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      75.2 | **71.2** |
| TPOT median (ms)          |            - |  **15.0** |     22.2 |
| E2E median (ms)           |            - | **619.9** |    831.8 |
| Throughput median (tok/s) |            - |  **58.2** |     42.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
ess] Device 3 CPU core 19
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1804:1804 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1798:1798 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1799:1799 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-380a2107:1797:1797 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-380a2107:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-380a2107:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-380a2107:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-380a2107:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-380a2107:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-380a2107:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x56339b5a3930 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d85cc955e0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-380a2107:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x56220f0efa00 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.21, bootstrap 0.03, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
gpu-dev-380a2107:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x562f0f6e5af0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x55d973739e00 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-380a2107:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x5640fc9ce9f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-380a2107:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x55d3fa60a4b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a82.15, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.33, alloc 000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x5635d3121940 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd0d2de678d972b12 - Init COMPLETE
000 commId 0xd0d2de678d972b12 - Init COMPLETE
2.23, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
1.46, bootstrap 0.79, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
000 commId 0xd0d2de678d972b12 - Init COMPLETE
gpu-dev-380a2107:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.34, alloc gpu-dev-380a2107:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.33, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-380a2107:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.33, alloc gpu-dev-380a2107:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.34, alloc 1.23, bootstrap 1.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.01, rest 0.02)
2.20, bootstrap 0.04, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.99, rest 0.04)
2.19, bootstrap 0.04, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.1** |  134.1 |
| TPOT median (ms)          |            - |  **29.9** |   46.1 |
| E2E median (ms)           |            - | **266.0** |  355.2 |
| Throughput median (tok/s) |            - |  **18.3** |   13.1 |
| Correctness               |            - |       99% |    99% |
