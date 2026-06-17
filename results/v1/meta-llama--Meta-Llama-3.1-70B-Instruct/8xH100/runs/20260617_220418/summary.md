# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 PM PT, Jun 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **19/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     468.9s (7.8m) | `ccca738` |
| vllm         |     539.1s (9.0m) | `58b2e89` |
| sglang       | **284.3s (4.7m)** | `3b5aae2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        364.2 | **144.1** |      - |
| TPOT median (ms)          |         54.8 |  **53.4** |      - |
| E2E median (ms)           |        413.6 | **192.0** |      - |
| Throughput median (tok/s) |          3.4 |   **7.4** |      - |
| Correctness               |          98% |       98% |      - |

> **sglang error:** `[sglang] Server process exited with code -9.
Log tail:
rward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 327, in forward
    hidden_states = self.self_attn(
        positions=positions,
        hidden_states=hidden_states,
        forward_batch=forward_batch,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 251, in forward
    attn_output = self.attn(q, k, v, forward_batch)
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/radix_attention.py", line 145, in forward
    return get_attn_backend().forward(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/base_attn_backend.py", line 169, in forward
    return self.forward_decode(
           ~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/flashattention_backend.py", line 1448, in forward_decode
    result = flash_attn_with_kvcache(
        q=q_reshaped,
    ...<17 lines>...
        **kwargs,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention.py", line 137, in flash_attn_with_kvcache
    return fa3_flash_attn_with_kvcache(
        q,
    ...<31 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 149, in flash_attn_with_kvcache
    return _call_fa3_kernel(
        _load_fa3_kernels()["flash_attn_with_kvcache"],
    ...<32 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 21, in _call_fa3_kernel
    return kernel(*args, **kwargs)
TypeError: flash_attn_with_kvcache() got an unexpected keyword argument 'only_qv'

[2026-06-17 22:03:39] Received sigquit from a child process. It usually means the child failed.
[2026-06-17 22:03:39] kill_process_tree called: parent_pid=15387, include_parent=True, pid=15387
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        281.2 | **183.5** |      - |
| TPOT median (ms)          |          0.0 |       0.0 |      - |
| E2E median (ms)           |        385.9 | **204.3** |      - |
| Throughput median (tok/s) |          2.6 |   **4.9** |      - |
| Correctness               |         100% |      100% |      - |

> **sglang error:** `[sglang] Server process exited with code -9.
Log tail:
rward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 327, in forward
    hidden_states = self.self_attn(
        positions=positions,
        hidden_states=hidden_states,
        forward_batch=forward_batch,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 251, in forward
    attn_output = self.attn(q, k, v, forward_batch)
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/radix_attention.py", line 145, in forward
    return get_attn_backend().forward(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/base_attn_backend.py", line 169, in forward
    return self.forward_decode(
           ~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/flashattention_backend.py", line 1448, in forward_decode
    result = flash_attn_with_kvcache(
        q=q_reshaped,
    ...<17 lines>...
        **kwargs,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention.py", line 137, in flash_attn_with_kvcache
    return fa3_flash_attn_with_kvcache(
        q,
    ...<31 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 149, in flash_attn_with_kvcache
    return _call_fa3_kernel(
        _load_fa3_kernels()["flash_attn_with_kvcache"],
    ...<32 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 21, in _call_fa3_kernel
    return kernel(*args, **kwargs)
TypeError: flash_attn_with_kvcache() got an unexpected keyword argument 'only_qv'

[2026-06-17 22:03:39] Received sigquit from a child process. It usually means the child failed.
[2026-06-17 22:03:39] kill_process_tree called: parent_pid=15387, include_parent=True, pid=15387
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        722.7 | **162.7** |      - |
| TPOT median (ms)          |         62.4 |  **47.4** |      - |
| E2E median (ms)           |        789.2 | **206.1** |      - |
| Throughput median (tok/s) |          1.9 |   **6.7** |      - |
| Correctness               |          98% |       98% |      - |

> **sglang error:** `[sglang] Server process exited with code -9.
Log tail:
rward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 327, in forward
    hidden_states = self.self_attn(
        positions=positions,
        hidden_states=hidden_states,
        forward_batch=forward_batch,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 251, in forward
    attn_output = self.attn(q, k, v, forward_batch)
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/radix_attention.py", line 145, in forward
    return get_attn_backend().forward(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/base_attn_backend.py", line 169, in forward
    return self.forward_decode(
           ~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/flashattention_backend.py", line 1448, in forward_decode
    result = flash_attn_with_kvcache(
        q=q_reshaped,
    ...<17 lines>...
        **kwargs,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention.py", line 137, in flash_attn_with_kvcache
    return fa3_flash_attn_with_kvcache(
        q,
    ...<31 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 149, in flash_attn_with_kvcache
    return _call_fa3_kernel(
        _load_fa3_kernels()["flash_attn_with_kvcache"],
    ...<32 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 21, in _call_fa3_kernel
    return kernel(*args, **kwargs)
TypeError: flash_attn_with_kvcache() got an unexpected keyword argument 'only_qv'

[2026-06-17 22:03:39] Received sigquit from a child process. It usually means the child failed.
[2026-06-17 22:03:39] kill_process_tree called: parent_pid=15387, include_parent=True, pid=15387
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        191.2 | **60.1** |      - |
| TPOT median (ms)          |         31.4 | **27.6** |      - |
| E2E median (ms)           |        225.3 | **81.4** |      - |
| Throughput median (tok/s) |          5.7 | **14.8** |      - |
| Correctness               |          97% |      97% |      - |

> **sglang error:** `[sglang] Server process exited with code -9.
Log tail:
rward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 327, in forward
    hidden_states = self.self_attn(
        positions=positions,
        hidden_states=hidden_states,
        forward_batch=forward_batch,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 251, in forward
    attn_output = self.attn(q, k, v, forward_batch)
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/radix_attention.py", line 145, in forward
    return get_attn_backend().forward(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/base_attn_backend.py", line 169, in forward
    return self.forward_decode(
           ~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/flashattention_backend.py", line 1448, in forward_decode
    result = flash_attn_with_kvcache(
        q=q_reshaped,
    ...<17 lines>...
        **kwargs,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention.py", line 137, in flash_attn_with_kvcache
    return fa3_flash_attn_with_kvcache(
        q,
    ...<31 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 149, in flash_attn_with_kvcache
    return _call_fa3_kernel(
        _load_fa3_kernels()["flash_attn_with_kvcache"],
    ...<32 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 21, in _call_fa3_kernel
    return kernel(*args, **kwargs)
TypeError: flash_attn_with_kvcache() got an unexpected keyword argument 'only_qv'

[2026-06-17 22:03:39] Received sigquit from a child process. It usually means the child failed.
[2026-06-17 22:03:39] kill_process_tree called: parent_pid=15387, include_parent=True, pid=15387
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        335.4 |  **81.9** |      - |
| TPOT median (ms)          |         22.0 |  **15.0** |      - |
| E2E median (ms)           |       1086.1 | **642.5** |      - |
| Throughput median (tok/s) |         32.2 |  **57.3** |      - |
| Correctness               |         100% |      100% |      - |

> **sglang error:** `[sglang] Server process exited with code -9.
Log tail:
rward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 327, in forward
    hidden_states = self.self_attn(
        positions=positions,
        hidden_states=hidden_states,
        forward_batch=forward_batch,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/models/llama.py", line 251, in forward
    attn_output = self.attn(q, k, v, forward_batch)
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/workspace/submit-d1513b7f/builds/sglang/venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/radix_attention.py", line 145, in forward
    return get_attn_backend().forward(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/base_attn_backend.py", line 169, in forward
    return self.forward_decode(
           ~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/srt/layers/attention/flashattention_backend.py", line 1448, in forward_decode
    result = flash_attn_with_kvcache(
        q=q_reshaped,
    ...<17 lines>...
        **kwargs,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention.py", line 137, in flash_attn_with_kvcache
    return fa3_flash_attn_with_kvcache(
        q,
    ...<31 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 149, in flash_attn_with_kvcache
    return _call_fa3_kernel(
        _load_fa3_kernels()["flash_attn_with_kvcache"],
    ...<32 lines>...
        out=out,
    )
  File "/workspace/submit-d1513b7f/builds/sglang/python/sglang/jit_kernel/flash_attention_v3.py", line 21, in _call_fa3_kernel
    return kernel(*args, **kwargs)
TypeError: flash_attn_with_kvcache() got an unexpected keyword argument 'only_qv'

[2026-06-17 22:03:39] Received sigquit from a child process. It usually means the child failed.
[2026-06-17 22:03:39] kill_process_tree called: parent_pid=15387, include_parent=True, pid=15387
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        379.0 | **126.5** |      - |
| TPOT median (ms)          |         34.1 |  **28.7** |      - |
| E2E median (ms)           |        580.0 | **265.2** |      - |
| Throughput median (tok/s) |          9.1 |  **18.2** |      - |
| Correctness               |          99% |       99% |      - |
