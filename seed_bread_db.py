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


# users get seeded randomly
for n in range(10):
    username = f"user{n}"
    email = f"user{n}@test.com"
    password = "test"

    new_user = crud.create_user(username, email, password)

# recipes get seeded randomly
    # including ingredients
# ingredients available get seeded from json?

# how to seed middle table?