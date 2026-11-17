from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    elements: set = dark_spell_allowed_ingredients()
    arg_ele: set = set(ingredients.split())
    if elements & arg_ele:
        return "VALID"
    else:
        return "INVALID"
