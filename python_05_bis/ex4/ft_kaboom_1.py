from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Acess to alchemy/grimoire/dark_spellbook.py directly")
    print("Test now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    msg = dark_spell_record("Rocket", "Fire, rock, water")
    print(msg)
