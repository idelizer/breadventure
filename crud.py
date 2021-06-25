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

    return User.query.get(email)

def create_recipe(user_id, date, instructions, is_starter_feeding=False, name=None, observations=None, baking_time=None, baking_temp=None):
    """Make a new recipe."""
    # Required arguments: user_id, date, instructions, is_starter_feeding
    # Optional parameters: name, observations, baking_time, baking_temp, ambient_temp

    recipe = Recipe(user_id=user_id, date=date, instructions=instructions, is_starter_feeding=is_starter_feeding, name=name, observations=observations, baking_time=baking_time, baking_temp=baking_temp)

    db.session.add(recipe)
    db.session.commit()

    return recipe

def get_recipes():
    """Return all recipes."""

    return Recipe.query.all()

def get_recipes_by_id(recipe_id):
    """Return a recipe given its id."""

    return Recipe.query.get(recipe_id)

# get recipes by user id?
# ... how does search function work here?

def create_starter_feeding(user_id, date, instructions, is_starter_feeding=True, name=None, observations=None, baking_time=None, baking_temp=None):
    """Create starter feeding, a recipe object where is_starter_feeding is set to True."""

    starter_feeding = Recipe(user_id=user_id, date=date, instructions=instructions, is_starter_feeding=is_starter_feeding, name=name, observations=observations, baking_time=baking_time, baking_temp=baking_temp)

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



