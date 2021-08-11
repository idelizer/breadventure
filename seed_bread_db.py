"""Create, seed, destroy database."""

import os
# import json

import crud
import model
import server

os.system('dropdb breadjournal')
os.system('createdb breadjournal')

model.connect_to_db(server.app)
model.db.create_all()

## create file for data, have .json file inside
# with open('data/filename.json') as x:
#     bread_data = json.loads(x.read())


# # TEST: seeding users incrementally
# for n in range(1, 11):
#     username = f"user{n}"
#     email = f"user{n}@test.com"
#     password = "test"

#     new_user = crud.create_user(username, email, password)

# DEMO: create user for demo
username = "idelizer"
email = "elizaofthebay@gmail.com"
password = "Testing!1234"

new_user = crud.create_user(username, email, password)


# # TEST: seeding ingredients from list for testing purposes
# ingredient_list = ["flour", "salt", "water", "starter", "yeast",]

# for ingredient in ingredient_list:
#     new_test_ingredient = crud.create_ingredient(ingredient)

# DEMO: seeding ingredients from textfile
ingredients_file = open("data/ingredients.txt")
ingredients = ingredients_file.read().split("\n")

for ingredient in ingredients:
    if ingredient != "":
        new_ingredient = crud.create_ingredient(ingredient)

# # TEST: seeding recipes
# recipe1 = crud.create_recipe(1, '01-01-2011', 'instructions1', 'name1', 'observations1', 11, 111)
# recipe2 = crud.create_recipe(1, '02-02-2022', 'instructions2', None, 'observations2', None, 222)
# recipe3 = crud.create_recipe(1, '03-03-2033', 'instructions3')
# recipe4 = crud.create_recipe(1, '02-02-2022', 'instructions4', None, None, None, None, None, True)

# DEMO: seeding recipes for demonstration
# user_id, date, instructions, name, observations, baking_time, baking_temp, picture, is_starter_feeding
recipe1 = crud.create_recipe(1, '08-01-2021', 'instructions1', 'Picnic Loaf', None, None, None, None, False)
recipe2 = crud.create_recipe(1, '08-03-2021', 'instructions2', 'Naturally Leavened Rye from Breadtopia', None, None, None, None, False)
recipe3 = crud.create_recipe(1, '08-06-2021', 'Mix leaven and water, then mix in flour by hand. Let dough rest for 30 min. Add salt, work to combine. Fold dough. Bulk ferment for 3 hours, folding every half hour. Shape into two boules. Let boules prove at room temp until they pass the poke test, then refrigerate for 12 hours. Score before baking. Bake in preheated dutch oven, with steam for first 20 min.', 'Tartine’s Basic Country Bread', 'Overproofed! Set a timer next time. Subtle sourness was nice.', 40, 500, None, False)
recipe4 = crud.create_recipe(1, '08-09-2021', 'instructions4', 'Yeast Bay', None, None, None, None, True)
recipe5 = crud.create_recipe(1, '08-09-2021', 'instructions5', 'Easy Whole Wheat', None, None, None, None, False)
recipe6 = crud.create_recipe(1, '08-13-2021', 'Autolyse water and flour for 20 min. Combine salt and yeast, hand mixing for 5 minutes. Let rise. Fold twice over the next one and a half hours. Divide into two when dough has tripled in volume. Shape loaves into boules. Proof for at least an hour. Bake in preheated dutch oven.', 'Saturday White Bread from FWSY', 'Came out very well! Already looking forward to making it again.', 30, 475, None, False)
recipe7 = crud.create_recipe(1, '08-16-2021', 'Discard until 100g of starter left. Add water and WW, mix with hand. Leave out for half an hour before returning to fridge.', 'Yeast Bay', "A little overly sour- perhaps feed every 6 days instead?", None, None, None, True)
recipe8 = crud.create_recipe(1, '08-16-2021', 'Mix water, starter, and flours for 5 min with paddle. Autolyse 30 min. Add salt, mix 5 min, rest 5 min. Fold 3 times, 30 min apart. Shape into boule, dusting baskets with 50/50 mix of AP and rice flour. Let proof out, then let ferment overnight in the fridge.', 'Easy Whole Wheat v2', "Not sour enough! Crumb is too dense- maybe less whole wheat?", 30, 500, None, False)
recipe9 = crud.create_recipe(1, '08-17-2021', 'instructions9', 'Jean Lukewarm Batard', None, None, None, None, True)


# # TEST: seeding amounts (middle table between recipe and ingredients)
#     # set amounts for first recipe of first user
# amount1flour = crud.create_amount(1, 1, 400)
# amount2salt = crud.create_amount(1, 2, 10)
# amount3water = crud.create_amount(1, 3, 300)
# amount4starter = crud.create_amount(1, 4, 100)

# amount5flour = crud.create_amount(2, 1, 500)
# amount6water = crud.create_amount(2, 3, 600)

# amount7flour = crud.create_amount(3, 1, 100)
# amount8water = crud.create_amount(3, 27, 80)
# amount9starter = crud.create_amount(3, 37, 10)
# amount10salt = crud.create_amount(3, 41, 2)

# DEMO: seed amounts
# recipe_id, ingredient_id, amount_in_grams
amount1 = crud.create_amount(3, 5, 900)       # white flour
amount2 = crud.create_amount(3, 3, 100)       # WW
amount3 = crud.create_amount(3, 28, 750)      # water
amount4 = crud.create_amount(3, 38, 50)       # starter
amount5 = crud.create_amount(3, 45, 20)       # salt

amount6 = crud.create_amount(6, 5, 1000)      # white flour
amount7 = crud.create_amount(6, 28, 720)      # water  
amount8 = crud.create_amount(6, 44, 21)       # sea salt
amount9 = crud.create_amount(6, 34, 4)        # instant dried yeast

amount10 = crud.create_amount(7, 38, 100)     # starter
amount11 = crud.create_amount(7, 28, 100)     # water
amount12 = crud.create_amount(7, 3, 100)      # WW

amount13 = crud.create_amount(8, 2, 175)      # AP
amount14 = crud.create_amount(8, 3, 175)      # WW
amount15 = crud.create_amount(8, 28, 290)     # water
amount16 = crud.create_amount(8, 38, 60)      # starter
amount17 = crud.create_amount(8, 45, 9)       # salt

# recipes to click on in demo:
# 3. Tartine
# 6. FSWY
# 7. Self - starter
# 8. Self - loaf

# recipe to input in demo:
# date = today
# name =
# instructions = 
# ingredients
#     flour - 100
#     water - 80
#     starter - 10
#     salt - 2
# temp = 500
# time = 30
# upload = ??
# observations = 


