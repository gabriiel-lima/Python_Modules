from alchemy.grimoire.light_spellbook import light_spell_record 


def main() -> None:
    checker = light_spell_record("Fantasy", "Earth, Wind, fire")
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: Spell recorded: {checker}")


if __name__ == "__main__":
    main()
