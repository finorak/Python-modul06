try:
    from alchemy.grimoire.spellbook import record_spell as rsp
except Exception as e:
    print(e)
try:
    from alchemy.grimoire.validator import validate_ingredients
except Exception as e:
    print(e)


def main() -> str:
    try:
        print("Testing ingredient validation:")
        print('validate_ingredients("fire aire")', end=": ")
        print(validate_ingredients("fire aire"))
    except Exception as e:
        print(e)
    print()
    try:
        print("Testing spell recording with validation")
        print('record_spell("Fireball", "fire air")', end=": ")
        print(rsp("Fireball", "fire air"))
        print('record_spell("Dark Magic", "shadow")', end=": ")
        print(rsp("Dark Magic", "shadow"))
    except Exception as e:
        print(e)
    print()
    try:
        from alchemy.grimoire.spellbook import record_spell
        print("Testing late import technique:")
        print('record_spell("Lightning", "air")', end=": ")
        print(record_spell("Lightning", "air"))
    except Exception as e:
        print(e)
    print()
    print("All spells processed safely!")
    return "done"


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===")
    main()
