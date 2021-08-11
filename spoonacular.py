"""Experiments with the spoonacular API."""

import os 
import requests
import json 

api_key = os.environ.get('SPOONACULAR_KEY')
print(api_key)

# REMEMBER source secret.sh !!!

QUERIES = ["flour", "water", "yeast", "grain", "nut", "seed", "berry", "berries", "cheese"]

def get_ingredients(query):
    """Send request to spoonacular API to get a list of ingredients matching the query string."""  
    # first query parameter is prefixed with a ? (question mark), all subsequent ones will be prefixed with a & (ampersand)
    # eg https://api.spoonacular.com/recipes/716429/information?apiKey=YOUR-API-KEY&includeNutrition=true.
    
    response = requests.get(f'https://api.spoonacular.com/food/ingredients/search?query={query}&apiKey={api_key}')
    # response = requests.get(f'https://api.spoonacular.com/food/ingredients/search?query=spinach&apiKey=199dd4808d7346558b9e5ff7a440e6cb')
    #print(response.status_code)

    # get reponse object, extract list of names of each food item
    ingredients = []
    results = response.json()
    ingredients_dict = results["results"]
    for ingredient in ingredients_dict:
         ingredients.append(ingredient["name"])
        
    return ingredients

data_file = open("data/ingredients.txt", "a")   # a tag to append, w to write

# pass in all bread-relevant search terms
for query in QUERIES:
    for result in (get_ingredients(query)):
        data_file.write(result)
        data_file.write("\n")


