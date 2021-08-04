"use strict";
console.log('JS IS WORKING')

const recipeId = window.location.pathname.slice(12);
const recipeIdJSON = {"recipe_id": recipeId};


// bakers percentage bar graph
const graphContainer = document.getElementById("graph"); //
const graphCanvas = document.getElementById("graph-canvas");

// set colors for bar graph
const backgroundColors = [
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
];
const borderColors = [
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
];

// given recipe ID, get json amount data
const amountJson = [];
const amountNames = [];
// const amountPercentages = [];

document.addEventListener("DOMContentLoaded", function() {
    fetch("/get-amounts", {
        method: "POST",
        body: JSON.stringify(recipeIdJSON),
        headers: {
            'Content-Type': 'application/json'  // could be application/formdata??
        }
    })
    .then(response => response.json()) // response into json
    // .then(data => {console.log(data); return data})
    .then(data => {
        for (const amount of data.data) {
            amountJson.push({x: amount.ingredient_name, y: amount.amount});
            amountNames.push(amount.ingredient_name);
            // amountPercentages.push(amount.amount);
        };
    })
    .then(data => {console.log(amountJson); console.log(amountNames); // create new array of objects for array
    const testChart = new Chart(graphCanvas, {
        type: "bar",
        data: {
            labels: amountNames, //amountJson, // how to access name of each object??
            datasets: [{                                            // array of dataset objects
                label: "hello",       // labels on x axis
                data: amountJson,                                        // size of each bar
                backgroundColor: backgroundColors,
                borderColor: borderColors,
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
    
    });
});



// format instructions with numbers, observations with dashes
// document.getElementById("instructions").value // get value of instructions
// split value at any digit space{d+}. --> add new line character
// document.getElementById("instructions").value = formattedStr; // reset value with formatted string 
