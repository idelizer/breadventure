"""Models for bread baking journal."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    recipes = db.relationship("Recipe")

    def __repr__(self):
        return f'<User id={self.user_id} email={self.email}>'


class Recipe(db.Model):
    """A recipe."""

    __tablename__ = "recipes"
    
    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    is_starter_feeding = db.Column(db.Boolean, nullable=False)

    observations = db.Column(db.Text, nullable=True)
    baking_time = db.Column(db.Integer, nullable=True)
    baking_temp = db.Column(db.Integer, nullable=True)
    ambient_temp = db.Column(db.Integer, nullable=True)

    user = db.relationship("User")
    user_ingredients = db.relationship("UserIngredient")

    def __repr__(self):
        return f'<Recipe id={self.recipe_id} date={self.date}>'

class UserIngredient(db.Model):
    """Middle table between a recipe and an ingredient indicating amount of ingredient in said recipe."""

    __tablename__ = "user_ingredients"

    user_ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'), nullable=False)
    amount_in_grams = db.Column(db.Integer, nullable=False)

    recipe = db.relationship("Recipe")
    ingredient = db.relationship("Ingredient")

    def __repr__(self):
        return f'<Ingredient {self.ingredient_id} for recipe {self.recipe_id}>'

class Ingredient(db.Model):
    """An ingredient."""

    __tablename__ = "ingredients"

    ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)

    user_ingredients = db.relationship("UserIngredient")

    def __repr__(self):
        return f'<Ingredient id={self.ingredient_id} name={self.name}>'


def connect_to_db(app, db_uri='postgresql:///breadjournal', echo=True):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
