try:
    from alchemy.elements import create_fire, create_earth
except Exception as e:
    print(e)


def lead_to_gold() -> str:
    try:
        return f"Lead transmuted to gold using {create_fire()}"
    except Exception as e:
        return f"{e}"


def stone_to_gem() -> str:
    try:
        return f"Stone transmuted to gem using {create_earth()}"
    except Exception as e:
        return f"{e}"
