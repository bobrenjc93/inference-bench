# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 8 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |          0/4 |  0/4 |    0/4 |
| self_consistency |          0/4 |  0/4 |    0/4 |
| multi_turn       |          0/4 |  0/4 |    0/4 |
| tree_of_thought  |          0/4 |  0/4 |    0/4 |
| long_output      |          0/4 |  0/4 |    0/4 |
| **Total**        |         0/20 | 0/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **42.4s (0.7m)** | `f6e4a02` |
| vllm         |    249.8s (4.2m) | `51e5372` |
| sglang       |    167.9s (2.8m) | `669b4bc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  132.3 |
| TPOT median (ms)          |            - |    - |   81.8 |
| E2E median (ms)           |            - |    - |  209.7 |
| Throughput median (tok/s) |            - |    - |    5.8 |
| Correctness               |            - |    - |    98% |

> **torchinferno error:** `timed out`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-88e49aad/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-88e49aad/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-88e49aad/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  216.7 |
| TPOT median (ms)          |            - |    - |    0.0 |
| E2E median (ms)           |            - |    - |  357.0 |
| Throughput median (tok/s) |            - |    - |    2.8 |
| Correctness               |            - |    - |   100% |

> **torchinferno error:** `Connection error.`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-88e49aad/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-88e49aad/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-88e49aad/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  159.4 |
| TPOT median (ms)          |            - |    - |  110.4 |
| E2E median (ms)           |            - |    - |  268.3 |
| Throughput median (tok/s) |            - |    - |    4.8 |
| Correctness               |            - |    - |    98% |

> **torchinferno error:** `Connection error.`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-88e49aad/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-88e49aad/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-88e49aad/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |   43.3 |
| TPOT median (ms)          |            - |    - |  241.4 |
| E2E median (ms)           |            - |    - |  243.4 |
| Throughput median (tok/s) |            - |    - |    6.3 |
| Correctness               |            - |    - |    97% |

> **torchinferno error:** `Connection error.`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-88e49aad/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-88e49aad/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-88e49aad/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |   67.3 |
| TPOT median (ms)          |            - |    - |   22.1 |
| E2E median (ms)           |            - |    - |  933.9 |
| Throughput median (tok/s) |            - |    - |   41.7 |
| Correctness               |            - |    - |   100% |

> **torchinferno error:** `Connection error.`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-88e49aad/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-88e49aad/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-88e49aad/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-88e49aad/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-88e49aad/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  123.8 |
| TPOT median (ms)          |            - |    - |   91.1 |
| E2E median (ms)           |            - |    - |  402.5 |
| Throughput median (tok/s) |            - |    - |   12.3 |
| Correctness               |            - |    - |    99% |
