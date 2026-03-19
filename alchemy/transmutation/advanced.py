try:
    from .basic import lead_to_gold
except Exception as e:
    print(e)
try:
    from ..potions import healing_potion
except Exception as e:
    print(e)


def philosophers_stone() -> str:
    try:
        value = f"Philosopher's stone created using {lead_to_gold()}"
        value += f" and {healing_potion()}"
        return value
    except Exception as e:
        return f"{e}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
