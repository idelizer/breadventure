"use strict";
console.log('JS IS WORKING')

 // create functions to break this up further?

const addIngredients = document.getElementById("add-ingredients");
const ingredientInput = document.getElementById("ingredients-input");
const ingredientsTable = document.getElementById("ingredients-table");
const dbIngredients = [];

// inputted ingr/amounts for html display and pass to backend as json on submit
// array: [{ingredientName: "flour", ingredientAmount: '100'}, {ingredientName: "water", ingredientAmount: '100'}]
// dict: {"flour": 10, "water": 10, "love": 10}

const newRecipeIngredients = [];
// obj: const newRecipeIngredients = {};

// frontload all ingredients from database
// jquery's document.ready loads as page loads (up to 100 ingredients, don't worry about it, 500- 1000 ill take time, dont front load over 10,000)
// vanilla equivalent is: 
document.addEventListener("DOMContentLoaded", function() {
    fetch('/get-ingredients')
    .then((res) => res.json())  // response into json
    .then((data) => {console.log(data); return data})
    .then((data) => dbIngredients.push(data.ingredients))   // data is {ingredients; ingredients}
});
console.log(dbIngredients, "are ingredients from DB")

// create function to autofill input box from frontloaded ingredients
    // event listener that listens for whenever user inputs new character
        // check what is currenlty written in string against ingr list
        // store new list with ingr of exact same character
        // print on html to check if working (later style in css to dropdown)

// generate a html table row with a given objects data
const generateRow = (obj) => {
    return '<tr><td>' + obj.ingredientName + '</td><td>' + obj.ingredientAmount + '</td></tr>'
};

// render all inputted ingr/amounts in html display
const generateTable = (obj, elem) => {
    const allRows = obj.map(generateRow);
    const allRowsStr = allRows.join("");
    const headers = '<tr id="headers"><th>Ingredient</th><th>Amount</th></tr>'

    elem.innerHTML = headers + allRowsStr
};

// add an inputted ing/amount to newRecipeIngredients array
// const pushIngrAmount = (obj) => {
    
// };

// begin adding ingredients (box to add pops up)
addIngredients.addEventListener('click', () => {
    // when Add Ingredients clicked, creates new input box and Add button (could use document.createElement)
    ingredientInput.innerHTML = '<label>Ingredient Name</label>' +
        '<input type="text" id="ingredient-name">' +
        '<label>Amount in Grams</label>' +
        '<input type="number" id="ingredient-amount">' +
        '<button type="button" id="push-ingredient">Add</button>';
    addIngredients.style.display = "none";

    // add a single ingredient to array 
    const pushIngredient = document.getElementById("push-ingredient")
    pushIngredient.addEventListener('click', () => {
        const inputIngredient = document.getElementById("ingredient-name");
        const inputAmount = document.getElementById("ingredient-amount");
        if ((inputIngredient.value !== "") && (inputAmount.value !== "")) {     // handle case where user inputs empty fields
            array: newRecipeIngredients.push({ingredientName: inputIngredient.value, ingredientAmount: inputAmount.value});
            // obj: newRecipeIngredients.inputIngredient = inputAmount;
        };
        console.log(newRecipeIngredients);
         
        generateTable(newRecipeIngredients, ingredientsTable);

        inputIngredient.value = ""
        inputAmount.value = ""
    });
});

document.getElementById("create-recipe-form").addEventListener('submit', (evt) => {
    evt.preventDefault();
    // experiment with changing submit to button, 

    // grab all html fields
    // process empty strings on frontend to send back smaller object
    //const date = evt.target.elements.date.value;

    const recipe = {
        date: document.getElementById("date").value,
        instructions: document.getElementById("instructions").value,
        name: document.getElementById("name").value,
        observations: document.getElementById("observations").value,
        bakingTime: document.getElementById("baking-time").value,
        bakingTemp: document.getElementById("baking-temp").value,
        feeding: document.getElementById("feeding").checked,
        ingredients: newRecipeIngredients
    }

    console.log(recipe);

    fetch("/create-recipe", {
        method: "POST",
        body: JSON.stringify(recipe),
        headers: {
            'Content-Type': 'application/json'
          }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.assign("/user");
    })
    .catch((error) => {
        console.error('Error:', error)
    });
    
    // where to put flashed message if fetched route returns promise after redirect?
    
    // create json object from all fields and newRecipeIngredients
    // send complete json object to backend via ajax request or fetch
    // look up json.parse and json.stringify
    //

});




