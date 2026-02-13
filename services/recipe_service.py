from extensions import db
from models.recipe_model import Recipe
from models.ingredient_model import Ingredient


def create_recipe(data):
    recipe = Recipe(
        title=data["title"],
        servings=data.get("servings"),
        description=data.get("description")
    )

    for item in data["ingredients"]:
        ingredient = Ingredient(
            name=item["name"],
            quantity=item.get("quantity"),
            unit=item.get("unit")
        )
        recipe.ingredients.append(ingredient)

    db.session.add(recipe)
    db.session.commit()

    return serialize_recipe(recipe)


def get_all_recipes():
    recipes = Recipe.query.all()
    return [serialize_recipe(r) for r in recipes]


def get_recipe_by_id(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return None
    return serialize_recipe(recipe)


def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return False

    db.session.delete(recipe)
    db.session.commit()
    return True


def serialize_recipe(recipe):
    return {
        "id": recipe.id,
        "title": recipe.title,
        "servings": recipe.servings,
        "description": recipe.description,
        "ingredients": [
            {
                "id": ing.id,
                "name": ing.name,
                "quantity": ing.quantity,
                "unit": ing.unit
            }
            for ing in recipe.ingredients
        ]
    }