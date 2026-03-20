def validate_ingredients(ingredients: str) -> str:
    spells = ["fire", "water", "earth", "air"]
    if not ingredients:
        return f"{ingredients} - INVALID"
    try:
        for spell in spells:
            if spell in ingredients:
                return f"{ingredients} - VALID"
        return f"{ingredients} - INVALID"
    except Exception as e:
        return f"{e}"
