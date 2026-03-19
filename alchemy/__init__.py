__version__ = "1.0.0"
__author__ = "Master Pythonnicius"

from typing import Any
from .elements import create_water, create_fire

__all__ = ["create_water", "create_fire"]


def __getattr__(name: str) -> Any:
    raise ImportError(
            "AttributeError - not exposed"
            )
