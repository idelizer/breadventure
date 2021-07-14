"""CRUD operations for bread journal."""

from model import db, connect_to_db, User, Recipe, RecipeIngredient, Ingredient 

def create_user(username, email, password):
    """Create and return a new user."""

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Get a user object by its id."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Get a user object by its email."""

    return User.query.filter(User.email == email).first()

def create_recipe(user_id, date, instructions, name=None, observations=None, baking_time=None, baking_temp=None, is_starter_feeding=False):
    """Make a new recipe."""
    # Required arguments: user_id, date, instructions, is_starter_feeding
    # Optional parameters: name, observations, baking_time, baking_temp, ambient_temp

    recipe = Recipe(user_id=user_id, date=date, instructions=instructions, name=name, observations=observations, baking_time=baking_time, baking_temp=baking_temp, is_starter_feeding=is_starter_feeding)

    db.session.add(recipe)
    db.session.commit()

    return recipe

def get_recipes():
    """Return all recipes."""

    return Recipe.query.all()

def get_recipe_by_id(recipe_id):
    """Return a recipe given its id."""

    return Recipe.query.get(recipe_id)

def get_recipes_by_user(user_id):
    """Return all recipes given a user_id."""

    return Recipe.query.filter(User.id == user_id).all()

# ... how does search function work here?
# search through entire table
# or add special indexes for text search as opposed to exact searches (regex)
# specify how search term relates to table item
# substring matches, text pattern operations
# function for each table per each function
# or query that unions all things I want to search

def create_starter_feeding(user_id, date, instructions, name=None, observations=None, baking_time=None, baking_temp=None, is_starter_feeding=True):
    """Create starter feeding, a recipe object where is_starter_feeding is set to True."""

    starter_feeding = Recipe(user_id=user_id, date=date, instructions=instructions, name=name, observations=observations, baking_time=baking_time, baking_temp=baking_temp, is_starter_feeding=is_starter_feeding)

    db.session.add(starter_feeding)
    db.session.commit()

    return starter_feeding

def create_ingredient(name):
    """Create and return a new ingredient."""

    ingredient = Ingredient(name=name)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient

def get_ingredients():
    """Get all ingredients."""

    return Ingredient.query.all()

def get_ingredient_by_id(ingredient_id):
    """Get an ingredient given its id."""

    return Ingredient.query.get(ingredient_id)

def create_amount(recipe_id, ingredient_id, amount_in_grams):
    """Set amount for an ingredient in a user's recipe."""

    amount = RecipeIngredient(recipe_id=recipe_id, ingredient_id=ingredient_id, amount_in_grams=amount_in_grams)

    db.session.add(amount)
    db.session.commit()

    return amount

def get_amount_by_id(amount_id):
    """Get an amount by its id."""

    return RecipeIngredient.query.get(amount_id)

def get_amounts_by_recipe(recipe_id):

    return RecipeIngredient.query.filter(Recipe.id == recipe_id).all()

