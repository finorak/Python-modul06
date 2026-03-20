from .spellbook import record_spell
from .validator import validate_ingredients

__all__ = ["record_spell", "validate_ingredients"]


def __getattr__(name: str) -> None:
    raise ImportError(
            "AttributeError - not exposed"
            )
