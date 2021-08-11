"use strict";
console.log('JS IS WORKING')

 // create functions to break this up further?

const addIngredients = document.getElementById("add-ingredients");
const ingredientInput = document.getElementById("ingredients-input");
const ingredientsTable = document.getElementById("ingredients-table");


// inputted ingr/amounts for html display and pass to backend as json on submit
// array: [{ingredientName: "flour", ingredientAmount: '100'}, {ingredientName: "water", ingredientAmount: '100'}]
// dict: {"flour": 10, "water": 10, "love": 10}

const newRecipeIngredients = [];

// collections for frontloaded ingredients data (array for display, set for lookup)
const dbIngredients = [];
const dbIngredientsSet = new Set();
const makeSet = (arr) => {
    for (const item of arr) {
        dbIngredientsSet.add(item);
     };
};

// frontload all ingredients from database (array for display, set for lookup)
// jquery's document.ready loads as page loads (up to 100 ingredients, don't worry about it, 500- 1000 ill take time, dont front load over 10,000)
// vanilla equivalent is: 
document.addEventListener("DOMContentLoaded", function() {
    fetch('/get-ingredients')
    .then((res) => res.json())  // response into json
    .then((data) => {console.log(data); return data})
    .then((data) => {dbIngredients.push(data.ingredients); return makeSet(data.ingredients)})   // data is {ingredients; ingredients}
    .then((data) => console.log(dbIngredientsSet + " has been created"))
});

// generate a html table row with a given objects data
const generateRow = (obj) => {
    return '<tr><td>' + obj.ingredientName + '</td><td>' + obj.ingredientAmount + '</td></tr>'
};

// render all inputted ingr/amounts in html display 
const generateTable = (obj, elem) => {
    const allRows = obj.map(generateRow);
    const allRowsStr = allRows.join("");
    const headers = '<thead><tr><th scope="col">Ingredient</th><th scope="col">Amount in Grams</th></tr></thead>'

    elem.innerHTML = headers + allRowsStr
};

// suggestions box pop up
const suggestionsEl = document.querySelector('[data-bs-toggle="popover"]');
const suggestionsPopover = new bootstrap.Popover(suggestionsEl)

// begin adding ingredients (box to add pops up)
addIngredients.addEventListener('click', () => {
    // when Add Ingredients clicked, creates new input box and Add button (could use document.createElement)
    ingredientInput.innerHTML = '<div class="row"> <span class="col-4 mb-3">' + 
        '<label for="ingredient-name" class="form-label">Ingredient Name</label>' +
        '<input type="text" id="ingredient-name" class="form-control" list="ingrResults">' +
        '<datalist id="ingrResults"></datalist>' +
        '</span> <span class="col-4 mb-3">' +
        '<label for="ingredient-amount" class="form-label">Amount in Grams</label>' +
        '<input type="number" id="ingredient-amount" class="form-control">' +
        '</span> <span class="col-1 mb-3">' +
        '<button type="button" id="push-ingredient" class="form-control btn-secondary">Add</button>'
        '</span> <div>';

    addIngredients.style.display = "none";

    // listen for whenever user inputs new character, compare substring to ingredients, return list
    document.getElementById("ingredient-name").addEventListener('input', (evt) => {       // input, change, keypress
        // get string input at every keystroke, convert to lowercase
        const currentInput = document.getElementById("ingredient-name").value.toLowerCase();
        //convert currentInput to regex for max search results
        const regexInput = new RegExp(".*" + currentInput + ".*", "g")
        // make list of ingredients that have a substring match for regexInput
        const searchResult = [];
        for (const ingredient of dbIngredients[0]) {
            const result = ingredient.match(regexInput); // match, includes, filter, indexof(.includes) --> if boolean true, capture index of list
            if (result !== null)
                searchResult.push(result[0]);        
        };
  
        // /////////////
        // // if user has inputted search char, display resulting list
        // const searchDisplay = document.getElementById("ingredients-search"); // div
        // searchDisplay.style.display = "";
        // // if user deletes input, display is hidden
        // if(dbIngredients[0].length === searchResult.length)
        //     searchDisplay.style.display = "none";
        // /////////////

        // generate html option for each ingredient in search result
        const makeOptionItem = (ingredient) => {
            return ('<option value="' + ingredient + '">');
        };

        // generate string of html options of all ingr results
        const makeAllOptions = (ingredients) => {
            let listOptions = "";
            for (const ingredient of ingredients) {
                const option = makeOptionItem(ingredient);
                listOptions = listOptions + option;
            }
            return listOptions;
        };

        console.log(makeAllOptions(searchResult));
        document.getElementById("ingrResults").innerHTML = makeAllOptions(searchResult);
        console.log("...")
       
        // /////////////////////////////////
        // // generate html list of ingredients from search result
        // const makeListItem = (ingredient, index) => {
        //     return ("<li id='result" + index + "' value='" + ingredient + "'>" + ingredient + "</li>")
            
        // };

        // // generate html string of all ingr results as list items
        // const makeHtmlList = (ingredients) => {
        //     let listItems = "";
        //     for (const index in ingredients) {
        //         const listIngredient = makeListItem(ingredients[index], index);
        //         listItems = listItems + listIngredient;
        //     };
        //     return listItems;
        // };

        // document.getElementById("search-list").innerHTML = makeHtmlList(searchResult);
        // /////////////////////

    });

    // if element is clicked on, set value to input box 
    document.getElementById("search-list").addEventListener('click', (evt) => {
        const clickedIngr = evt.target.getAttribute("value");
        document.getElementById("ingredient-name").value = clickedIngr;

    });

    // add a single ingredient to array 
    const pushIngredient = document.getElementById("push-ingredient")
    pushIngredient.addEventListener('click', () => {
        const inputIngredient = document.getElementById("ingredient-name");
        const inputAmount = document.getElementById("ingredient-amount");
        if ((inputIngredient.value !== "") && (inputAmount.value !== "")) {     // handle case where user inputs empty fields
            array: newRecipeIngredients.push({ingredientName: inputIngredient.value, ingredientAmount: inputAmount.value});
            // obj: newRecipeIngredients.inputIngredient = inputAmount;
        }; 
         
        generateTable(newRecipeIngredients, ingredientsTable);

        inputIngredient.value = ""
        inputAmount.value = ""
        document.getElementById("ingredients-search").style.display = "none";
    });
});


document.getElementById("create-recipe-form").addEventListener('submit', (evt) => {
    evt.preventDefault();
    // experiment with changing submit to button, 

    // grab all html field

    // element.files --> array to access index[0]
    // const picture = makeImageObject(img);
    // console.log(picture);
    // console.log(typeof picture);
    let formDataRecipe = new FormData();
        formDataRecipe.append("date", document.getElementById("date").value)
        formDataRecipe.append("instructions", document.getElementById("instructions").value)
        formDataRecipe.append("name", document.getElementById("name").value)
        formDataRecipe.append("observations", document.getElementById("observations").value)
        formDataRecipe.append("bakingTime", document.getElementById("baking-time").value)
        formDataRecipe.append("bakingTemp", document.getElementById("baking-temp").value)
        formDataRecipe.append("feeding", document.getElementById("feeding").checked)
        formDataRecipe.append("img", document.getElementById("img").files[0])
        formDataRecipe.append("ingredients", JSON.stringify(newRecipeIngredients))

    // rejected syntax: const date = evt.target.elements.date.value;

    console.log(formDataRecipe);

    fetch("/create-recipe", {
        method: "POST",
        body: formDataRecipe,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.assign("/user");
    })
    .catch((error) => {
        console.error('Error:', error)
    });
    
    // create json object from all fields and newRecipeIngredients
    // send complete json object to backend via ajax request or fetch
    // look up json.parse and json.stringify
    //

});




