__version__ = "1.0.0"
__author__ = "Master Pythonnicius"

from .elements import create_water, create_fire

__all__ = ["create_water", "create_fire"]


def __getattr__(name: str) -> None:
    raise ImportError(
            "AttributeError - not exposed"
            )
