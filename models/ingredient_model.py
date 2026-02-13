from extensions import db

class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey("recipes.id"),
        nullable=False
    )
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(50))