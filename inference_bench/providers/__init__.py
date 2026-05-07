from __future__ import annotations

from .base import Provider


_REGISTRY: dict[str, type[Provider]] = {}


def register(name: str):
    def decorator(cls: type[Provider]):
        _REGISTRY[name] = cls
        return cls
    return decorator


def get_provider(name: str, **kwargs) -> Provider:
    if name not in _REGISTRY:
        from . import vllm as _vllm, sglang as _sglang  # noqa: F811

    if name not in _REGISTRY:
        raise ValueError(
            f"Unknown provider: {name}. Available: {list(_REGISTRY.keys())}"
        )
    return _REGISTRY[name](**kwargs)
