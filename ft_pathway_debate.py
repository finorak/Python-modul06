try:
    from alchemy.transmutation.advanced import (elixir_of_life,
                                                philosophers_stone)
except Exception as e:
    print(e)
try:
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
except Exception as e:
    print(e)
try:
    import alchemy.transmutation as transmutation
except Exception as e:
    print(e)


def absolute_path() -> str:
    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold()", end=": ")
    try:
        print(lead_to_gold())
    except Exception as e:
        print(e)
    print("stone_to_gem()", end=": ")
    try:
        print(stone_to_gem())
    except Exception as e:
        print(e)
    print()
    return "done"


def relative_path() -> str:
    print("Testing Relative Imports (from advanced.py):")
    print("philosophers_stone()", end=": ")
    try:
        print(philosophers_stone())
    except Exception as e:
        print(e)
    print("elixir of life()", end=": ")
    try:
        print(elixir_of_life())
    except Exception as e:
        print(e)
    print()
    return "done"


def package_access() -> str:
    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold()", end=": ")
    try:
        print(transmutation.lead_to_gold())
    except Exception as e:
        print(e)
    print("alchemy.transmutation.philosophers_stone()", end=": ")
    try:
        print(transmutation.philosophers_stone())
    except Exception as e:
        print(e)
    return "done"


def main() -> str:
    print()
    absolute_path()
    relative_path()
    package_access()
    return "done"


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===")
    main()
    print()
    print("Both pathways work Absolute: clear, Relative: concise")
