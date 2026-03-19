try:
    from alchemy.elements import (create_fire, create_water,
                                  create_earth, create_air)
except Exception as e:
    print(e)


def healing_potion() -> str:
    try:
        result = f"Healing potion brewed with {create_fire()} "
        result += f"and {create_water()}"
        return result
    except Exception as e:
        return f"{e}"


def strength_potion() -> str:
    try:
        result = f"Strength potion brewed with {create_earth()} "
        result += f"and {create_fire()}"
        return result
    except Exception as e:
        return f"{e}"


def invisibility_potion() -> str:
    try:
        result = f"Invisibility potion brewed with {create_air()} "
        result += f"and {create_water()}"
        return result
    except Exception as e:
        return f"{e}"


def wisdom_potion() -> str:
    try:
        result = "Wisdom potion brewed with all elements: "
        result += f"{create_air()} {create_earth()} {create_water()} "
        result += create_fire()
        return result
    except Exception as e:
        return f"{e}"
