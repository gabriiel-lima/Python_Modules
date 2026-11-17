

def light_spell_ingredients() -> set:
    return {"earth", "air", "fire", "water"}


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    msg = f"{spell_name} ({ingredients} - "
    msg = msg + f"{validate_ingredients(ingredients.lower())})"
    return msg
