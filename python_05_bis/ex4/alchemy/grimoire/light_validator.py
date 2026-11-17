def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_ingredients    
    elements: set = light_spell_ingredients()
    arg_element: set = set(ingredients.split())
    if elements & arg_element:
        return "VALID"
    else:
        return "INVALID"
