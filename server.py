"""Server for bread journal app."""

from flask import Flask, render_template, request, redirect, flash, session, jsonify, json
from model import connect_to_db
import crud
import os

from jinja2 import StrictUndefined

#########################################
import cloudinary.uploader
CLOUDINARY_KEY = os.environ.get('CLOUDINARY_KEY')
CLOUDINARY_SECRET = os.environ.get('CLOUDINARY_SECRET')
CLOUDINARY_NAME = os.environ.get('CLOUDINARY_NAME')
#########################################

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY') # autogenerated and in secrets.sh
app.jinja_env.undefined = StrictUndefined

@app.route('/')
@app.route('/home')
def view_home():
    """View home."""
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    """Process users login form."""
    # login page is not rendered, only redirects either 
    # back to home page or to user page- is slower but 
    # is cleaner; speed is negligible

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)
    if user and user.password == password: 
        session["user_id"] = user.id
        return redirect('/user')
    else:
        flash('There was an error logging in! Please try again or make an account.')
        return redirect('/')


@app.route('/user')
def user_page():

    if "user_id" in session:
        user = crud.get_user_by_id(session["user_id"])
        recipes = crud.get_recipes_by_user(session["user_id"])

        return render_template('user.html', username=user.username, recipes=recipes)
    else:
        flash('There was an error with your login! Please try again or make an account.')
        return redirect('/')

@app.route('/experiment/<recipe_id>')
def display_recipe_details(recipe_id):

    # get recipe by id
    recipe = crud.get_recipe_by_id(recipe_id)
    # get ingredients and their amounts
    amounts = crud.get_amounts_by_recipe(recipe_id)

    return render_template('recipe_details.html', recipe=recipe, amounts=amounts) # pass in ingredients

@app.route('/get-amounts', methods=['POST'])
def get_amounts():
    """Get a recipe's ingredients and associated amounts."""
    # most useful format for a bar graph?
    # json/dict {amount.ingredient.name: amount_in_grams}
    # or parallel lists?

    recipe_id = request.json.get("recipe_id")
    amounts = crud.get_amounts_by_recipe(recipe_id) # list of objects, can access grams and name
    
    # find baker's percentage of each ingredient

    # get ratio (find ingredient with flour in key, set to 100% --> 300 g = 100%)
    ratio = 0
    for amount in amounts:
        if "flour" in amount.ingredient.name:
            ratio += amount.amount_in_grams
            print()
            print(ratio)
            print()
    # for each ingredient, set ratio to grams to get percent
    for amount in amounts:
        percentage = (amount.amount_in_grams / ratio)
        amount.percentage = int(percentage * 100)
        print(amount.percentage)
 
    amount_data = []
    for amount in amounts:
        amount_data.append({"ingredient_name": amount.ingredient.name, "amount": amount.percentage})

    return jsonify({'data': amount_data})


@app.route('/delete-recipe', )
def delete_recipe():
    """Given a recipe id, delete recipe from db."""
    
    recipe_id = request.json.get("recipe_id")
    deleted_msg = crud.delete_recipe(recipe_id)

    return "Success!"

@app.route('/new-user')
def new_user():
    """View form to register new user."""

    return render_template('new_user.html')

@app.route('/register-user', methods=['POST'])
def register_new_user():
    """Process form from new user."""

    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # check if user already exists, flash message + redirect to top
    # how to handle unique fields
    new_user = crud.create_user(username, email, password)

    flash('Success! Account made. Please log in.')

    return redirect('/home')


@app.route('/get-ingredients')
def convert_all_ingr_to_json():
    """Convert ingredient object to JSON to pass to javascript."""

    ingredients = crud.get_ingredients()
    
    return jsonify({'ingredients': [ingredient.name for ingredient in ingredients]})
     

@app.route('/test-recipe')
def design_recipe():
    """View form for user to input new recipe details."""

    ingredients = crud.get_ingredients()

    return render_template('recipe_form.html', ingredients=ingredients)

# one route to show form, one route to process form

@app.route('/create-recipe', methods=['POST'])
def create_new_recipe():
    """Process form from new recipe form, add to database."""

    # get user id from session
    user_id = session["user_id"]

    # parse recipe data for recipe table
    date = request.form.get("date") 
    instructions = request.form.get("instructions")
    name = request.form.get("name") or None # may not need none with ajax!
    observations = request.form.get("observations") or None
    baking_time = request.form.get("bakingTime") or None
    baking_temp = request.form.get("bakingTemp") or None
    ingr_str = request.form.get("ingredients") or None # comes in as json str
    img = request.files.get('img') or None
    is_feeding_str = request.form.get("feeding") # comes in as lowercase str   

    # convert boolean str from form into bool type
    if is_feeding_str == "false":
        is_feeding = False
    elif is_feeding_str == "true":
        is_feeding = True

    # if user uploads a picture, get secure url using cloudinary api to be stored in db
    if img:
        result = cloudinary.uploader.upload(img, api_key=CLOUDINARY_KEY, api_secret=CLOUDINARY_SECRET, cloud_name=CLOUDINARY_NAME)
        img_url = result['secure_url']
    else:
        img_url = None
  
    # parse ingredients/amounts for middle table
    ingr_json = json.loads(ingr_str)
    ingr_ids = []
    amounts = []
    for ingredient in ingr_json:
        ingr = crud.get_ingredient_by_name(ingredient["ingredientName"])
        ingr_ids.append(ingr.id)
        amounts.append(int(ingredient["ingredientAmount"]))
    # maybe create function to process ingr, then use map function? instead of loop?

    # add data to recipe table
    new_recipe = crud.create_recipe(user_id, date, instructions, name, observations, baking_time, baking_temp, img_url, is_feeding)
    print(new_recipe)

    # add data to middle table
    for index, ingr_id in enumerate(ingr_ids):
        new_amount = crud.create_amount(new_recipe.id, ingr_id, amounts[index])

    flash("Recipe successfully created!")

    # TO BE FIXED: javascript currently expecting json
    return {"success": "success"}

# @app.route('/feed-starter')
# def feed_starter():
#     """View form for user to input starter feeding details."""

#     return render_template('feeding-form.html')

# @app.route('/create-feeding', methods=['POST'])
# def create_new_feeding():
#     """Process form from new starter feeding form, add to database."""

#     user_id = session["user_id"]

#     date = request.form['date']
#     instructions = request.form['instructions']
#     name = request.form['name']
#     observations = request.form['observations']
#     baking_time = request.form['baking-time']
#     baking_temp = request.form['baking-temp']
#     img = request.files['img']

#     if name == "":
#         name = None

#     if observations == "":
#         observations = None
    
#     if baking_time == "":
#         baking_time = None

#     if baking_temp == "":
#         baking_temp = None

#     flash(f"Starter successfully fed!")

#     new_feeding = crud.create_starter_feeding(user_id, date, instructions, name, observations, baking_time, baking_temp)
#     print(new_feeding)

#     return redirect('/user')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)