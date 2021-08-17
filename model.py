"""Models for bread baking journal."""

from flask_sqlalchemy import SQLAlchemy
import requests, os

db_url = os.environ.get("DATABASE", 'postgresql:///breadjournal')

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    # standard for storing passwords is hashing
    # one way encryption, not decryptable
    # check user input, get hash, check if hashes match
    # then hackers still wouldn't have pws
    # find library to hash them, hash when pw is set

    recipes = db.relationship("Recipe")

    def __repr__(self):
        return f'<User id={self.id} email={self.email}>'


class Recipe(db.Model):
    """A recipe."""

    __tablename__ = "recipes"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    instructions = db.Column(db.Text, nullable=False)

    name = db.Column(db.String(50), nullable=True)
    observations = db.Column(db.Text, nullable=True)
    baking_time = db.Column(db.Integer, nullable=True)
    baking_temp = db.Column(db.Integer, nullable=True)
    picture = db.Column(db.String, nullable=True)
    is_starter_feeding = db.Column(db.Boolean, nullable=False)

    user = db.relationship("User")
    recipes_ingredients = db.relationship("RecipeIngredient")

    def __repr__(self):
        return f'<Recipe id={self.id} date={self.date}>'

class RecipeIngredient(db.Model):
    """Middle table between a recipe and an ingredient indicating amount of ingredient in said recipe."""

    __tablename__ = "recipes_ingredients"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), nullable=False)
    amount_in_grams = db.Column(db.Integer, nullable=False)

    recipe = db.relationship("Recipe")
    ingredient = db.relationship("Ingredient")

    def __repr__(self):
        return f'<Ingredient {self.ingredient_id} for recipe {self.recipe_id}>'

class Ingredient(db.Model):
    """An ingredient."""

    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)

    recipes_ingredients = db.relationship("RecipeIngredient")

    def __repr__(self):
        return f'<Ingredient id={self.id} name={self.name}>'


def connect_to_db(app, db_uri=db_url, echo=True):
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
