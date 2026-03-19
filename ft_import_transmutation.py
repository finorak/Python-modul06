try:
    import alchemy
except Exception as e:
    print(e)
try:
    from alchemy.elements import create_water
except Exception as e:
    print(e)
try:
    from alchemy.potions import healing_potion as heal
except Exception as e:
    print(e)
try:
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
except Exception as e:
    print(e)


def main() -> str:
    print()
    print("Method 1 - Full module import:")
    try:
        print("alchemy.elements.create_fire()", end=": ")
        print(alchemy.elements.create_fire())
    except Exception as e:
        print(e)
    print()
    print("Method 2 - Specific function import")
    try:
        print("create_water()", end=": ")
        print(create_water())
    except Exception as e:
        print(e)
    print()
    print("Method 3 - Aliased import")
    try:
        print("heal()", end=": ")
        print(heal())
    except Exception as e:
        print(e)
    print()
    print("Method 4 - Multiple imports")
    print("create_earth()", end=": ")
    try:
        print(create_earth())
    except Exception as e:
        print(e)
    print("create_fire()", end=": ")
    try:
        print(create_fire())
    except Exception as e:
        print(e)
    print("strength_potion()", end=": ")
    try:
        print(strength_potion())
    except Exception as e:
        print(e)
    print()
    print("All import transmutation methods mastered!")
    return "done"


if __name__ == "__main__":
    print("=== Import Transutation Mastery ===")
    try:
        main()
    except Exception as e:
        print(e)
