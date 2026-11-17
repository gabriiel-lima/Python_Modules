from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> set:
    return {"bats", "frogs", "arsenic", "eye-ball"}


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return dark_validate_ingredients(ingredients)
