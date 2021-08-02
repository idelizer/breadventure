"use strict";
console.log('JS IS WORKING')

// format instructions with numbers, observations with dashes
// document.getElementById("instructions").value // get value of instructions
// split value at any digit space{d+}. --> add new line character
// document.getElementById("instructions").value = formattedStr; // reset value with formatted string 

// bakers percentage bar graph

// console.log(recipe.name.value)

const recipeId = window.location.pathname.slice(12);
const recipeIdJSON = {"recipe_id": recipeId};

// delete recipe
document.getElementById("delete").addEventListener('click', (evt) => {
    console.log("button works")
    window.confirm("are you sure?")

    fetch("/delete-recipe", {
        method: "POST",
        body: JSON.stringify(recipeIdJSON),
        headers: {
            'Content-Type': 'application/json'  // could be application/formdata??
        }
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
        window.location.assign("/user")
    });
});
