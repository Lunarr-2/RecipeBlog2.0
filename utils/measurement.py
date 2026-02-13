def scale_ingredients(ingredients, original_servings, new_servings):
    if not original_servings or original_servings == 0:
        return ingredients

    factor = new_servings / original_servings

    scaled = []
    for item in ingredients:
        scaled.append({
            "name": item["name"],
            "quantity": item["quantity"] * factor if item["quantity"] else None,
            "unit": item["unit"]
        })

    return scaled