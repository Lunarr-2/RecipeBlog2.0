from flask import Blueprint, request, jsonify
from services.recipe_service import (
    create_recipe,
    get_all_recipes,
    get_recipe_by_id,
    delete_recipe
)

recipe_bp = Blueprint("recipes", __name__)


@recipe_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    recipe = create_recipe(data)
    return jsonify(recipe), 201


@recipe_bp.route("/", methods=["GET"])
def get_all():
    recipes = get_all_recipes()
    return jsonify(recipes), 200


@recipe_bp.route("/<int:recipe_id>", methods=["GET"])
def get_one(recipe_id):
    recipe = get_recipe_by_id(recipe_id)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    return jsonify(recipe), 200


@recipe_bp.route("/<int:recipe_id>", methods=["DELETE"])
def delete(recipe_id):
    success = delete_recipe(recipe_id)
    if not success:
        return jsonify({"error": "Recipe not found"}), 404
    return jsonify({"message": "Recipe deleted"}), 200