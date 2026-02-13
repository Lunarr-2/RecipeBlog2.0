from extensions import db

class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    servings = db.Column(db.Integer)
    description = db.Column(db.Text)

    ingredients = db.relationship(
        "Ingredient",
        backref="recipe",
        cascade="all, delete-orphan",
        lazy=True
    )