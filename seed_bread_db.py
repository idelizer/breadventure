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


# seeding users incrementally
for n in range(1, 11):
    username = f"user{n}"
    email = f"user{n}@test.com"
    password = "test"

    new_user = crud.create_user(username, email, password)

# #seeding ingredients from list for testing purposes
# ingredient_list = ["flour", "salt", "water", "starter", "yeast",]

# for ingredient in ingredient_list:
#     new_test_ingredient = crud.create_ingredient(ingredient)

# seeding ingredients from textfile
ingredients_file = open("data/ingredients.txt")
ingredients = ingredients_file.read().split("\n")

for ingredient in ingredients:
    if ingredient != "":
        new_ingredient = crud.create_ingredient(ingredient)

# seeding recipes
recipe1 = crud.create_recipe(1, '01-01-2011', 'instructions1', 'name1', 'observations1', 11, 111)
recipe2 = crud.create_recipe(1, '02-02-2022', 'instructions2', None, 'observations2', None, 222)
recipe3 = crud.create_recipe(1, '03-03-2033', 'instructions3')
recipe4 = crud.create_recipe(1, '02-02-2022', 'instructions4', None, None, None, None, None, True)


# seeding amounts (middle table between recipe and ingredients)
    # set amounts for first recipe of first user
amount1flour = crud.create_amount(1, 1, 400)
amount2salt = crud.create_amount(1, 2, 10)
amount3water = crud.create_amount(1, 3, 300)
amount4starter = crud.create_amount(1, 4, 100)

amount5flour = crud.create_amount(2, 1, 500)
amount6water = crud.create_amount(2, 3, 600)

amount7flour = crud.create_amount(3, 1, 100)
amount8water = crud.create_amount(3, 27, 80)
amount9starter = crud.create_amount(3, 37, 10)
amount10salt = crud.create_amount(3, 41, 2)