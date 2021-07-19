console.log('JS IS WORKING')

const addIngredients = document.getElementById("add-ingredients");
const ingredientInput = document.getElementById("ingredients-input");
const ingredientsTable = document.getElementById("ingredients-table");
const formSubmit = document.getElementById("create-recipe-form");
let dbIngredients = [];

// build list on front end with tuples of ingredent and amount --> pass to backend on submit
// eg [{ingredientName: "flour", ingredientAmount: '100'}, {ingredientName: "water", ingredientAmount: '100'}]
let newRecipeIngredients = [];

// frontload all ingredients from database
// jquery's document.ready loads as page loads (up to 100 ingredients, don't worry about it, 500- 1000 ill take time, dont front load over 10,000)
// vanilla equivalent is: 
document.addEventListener("DOMContentLoaded", function() {
    fetch('/get-ingredients')
    .then((res) => res.json())  // result into json
    .then((data) => {console.log(data); return data})
    .then((data) => dbIngredients = data.ingredients)   // data is {ingredients; ingredients}
});
console.log(dbIngredients, "are ingredients from DB")

// create function to autofill input box from frontloaded ingredients

// generate a html table row with a given objects data
const generateRow = (obj) => {
    return '<tr><td>' + obj.ingredientName + '</td><td>' + obj.ingredientAmount + '</td></tr>'
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

    // add a single ingredient 
    const pushIngredient = document.getElementById("push-ingredient")
    pushIngredient.addEventListener('click', () => {
        const inputIngredient = document.getElementById("ingredient-name");
        const inputAmount = document.getElementById("ingredient-amount");
        newRecipeIngredients.push({ingredientName: inputIngredient.value, ingredientAmount: inputAmount.value});
        console.log(newRecipeIngredients);
         
        const allRows = newRecipeIngredients.map(generateRow);
        const allRowsStr = allRows.join("");
        const headers = '<tr id="headers"><th>Ingredient</th><th>Amount</th></tr>'

        ingredientsTable.innerHTML = headers + allRowsStr

        inputIngredient.value = ""
        inputAmount.value = ""

        // create functions to break this up
    });
});

formSubmit.addEventListener('submit', () => {
    // send newRecipeIngredients array to backend
    // needs to be json?

});



