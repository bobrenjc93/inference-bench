from __future__ import annotations

from .base import Benchmark, BenchmarkResult


_REGISTRY: dict[str, type[Benchmark]] = {}


def register(name: str):
    def decorator(cls: type[Benchmark]):
        _REGISTRY[name] = cls
        return cls
    return decorator


def get_benchmark(name: str) -> Benchmark:
    if name not in _REGISTRY:
        from . import few_shot as _fs, self_consistency as _sc  # noqa: F811
        from . import multi_turn as _mt, tree_of_thought as _tot  # noqa: F811
        from . import long_output as _lo  # noqa: F811

    if name not in _REGISTRY:
        raise ValueError(
            f"Unknown benchmark: {name}. Available: {list(_REGISTRY.keys())}"
        )
    return _REGISTRY[name]()
