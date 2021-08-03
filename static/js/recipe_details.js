"use strict";
console.log('JS IS WORKING')

const recipeId = window.location.pathname.slice(12);
const recipeIdJSON = {"recipe_id": recipeId};


// bakers percentage bar graph
const graphContainer = document.getElementById("graph"); //
const graphCanvas = document.getElementById("graph-canvas");

// once not hardcoded, fetch data from backend (how to pass as json without jquery?- notes are only jquery)
// or pass through flask as hidden html
const grams = [100, 80, 10, 2];
const names = ["flour", "water", "sourdough starter", "salt"];
const jsonAmounts = {"flour": 100, "water": 80, "sourdough starter": 10, "salt": 2}

// given recipe ID, get json amount data
const amountJson = [];
document.addEventListener("DOMContentLoaded", function() {
    fetch("/get-amounts", {
        method: "POST",
        body: JSON.stringify(recipeIdJSON),
        headers: {
            'Content-Type': 'application/json'  // could be application/formdata??
        }
    })
    .then(response => response.json()) // response into json
    .then(data => {console.log(data); return data})
    .then(data => {amountJson.push(data.ingredients)});
});

const testChart = new Chart(graphCanvas, {
        type: "bar",
        data: {
            labels: names,
            datasets: [{                                            // array of dataset objects
                // labels: ["hello", "goodbye", "hi", "bye"],       // labels on x axis
                data: grams,                                        // size of each bar
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                ],
                borderWidth: 1,
                hoverBorderWidth: 5
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: "Ingredients",
                        // color: 'rgba(255, 99, 132, 1)',
                        // align: "end"
                    },
                }],
                yAxes: [{
                    ticks: {
                    min: 0,
                    max: 120
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "Baker's Percentage"
                    },
                }]
            }
        }
    }
);


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

// format instructions with numbers, observations with dashes
// document.getElementById("instructions").value // get value of instructions
// split value at any digit space{d+}. --> add new line character
// document.getElementById("instructions").value = formattedStr; // reset value with formatted string 
