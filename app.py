from flask import Flask
from config import Config
from extensions import db, cors
from routes.recipe_routes import recipe_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    cors.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(recipe_bp, url_prefix="/api/recipes")

    return app


app = create_app()

if __name__ == "__main__":

    app.run(debug=True)