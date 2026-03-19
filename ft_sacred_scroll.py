try:
    from alchemy.elements import (
            create_air, create_earth,
            create_fire, create_water
            )
except Exception:
    print("Module not found")
try:
    import alchemy
except Exception:
    print("Module not found")


def direct_access() -> str:
    print("\nTesting direct module access:")
    print("alchemy.elements.create_fire()", end=": ")
    try:
        print(create_fire())
    except Exception as e:
        print(e)
    print("alchemy.elements.create_water()", end=": ")
    try:
        print(create_water())
    except Exception as e:
        print(e)
    print("alchemy.elements.create_earth()", end=": ")
    try:
        print(create_earth())
    except Exception as e:
        print(e)
    print("alchemy.elements.create_air()", end=": ")
    try:
        print(create_air())
    except Exception as e:
        print(e)
    print()
    return "done"


def controlled_access() -> str:
    print("Testing package-level access (controlled by __init__.py: ")
    print("alchemy.create_fire()", end=": ")
    try:
        print(alchemy.create_fire())
    except Exception as e:
        print(e)
    print("alchemy.create_water()", end=": ")
    try:
        print(alchemy.create_water())
    except Exception as e:
        print(e)
    print("alchemy.create_earth()", end=": ")
    try:
        print(alchemy.create_earth())
    except Exception as e:
        print(e)
    print("alchemy.create_air()", end=": ")
    try:
        print(alchemy.create_air())
    except Exception as e:
        print(e)
    return "done"


def main() -> str:
    try:
        direct_access()
    except Exception as e:
        print(e)
    try:
        controlled_access()
    except Exception as e:
        print(e)
    return "success"


if __name__ == "__main__":
    print("Sacred Scroll Mastery ===")
    main()
    print()
    try:
        print("Package metadata:")
        version = alchemy.__version__
        author = alchemy.__author__
        print("Version:", version)
        print("Author:", author)
    except Exception as e:
        print(e)
