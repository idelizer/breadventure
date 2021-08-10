"use strict";
console.log('JS IS WORKING')

const recipeId = window.location.pathname.slice(12);
const recipeIdJSON = {"recipe_id": recipeId};


// bakers percentage bar graph
const graphContainer = document.getElementById("graph"); //
const graphCanvas = document.getElementById("graph-canvas");

// set colors for bar graph
const backgroundColors = [
    'rgba(182, 99, 169, .8)',
    'rgba(233, 168, 109, .8)',
    'rgba(132, 188, 167, .8)',
    'rgba(217, 105, 99, .8)',
    'rgba(137, 122, 201, .8)',
    'rgba(231, 198, 110, .8)',
    'rgba(185, 129, 159, .8)',
    'rgba(170, 188, 126, .8)',
    'rgba(217, 118, 89, .8)',
    'rgba(146, 111, 178, .8)',
];
const borderColors = [
    'rgba(182, 99, 169, 1)',
    'rgba(233, 168, 109, 1)',
    'rgba(132, 188, 167, 1)',
    'rgba(217, 105, 99, 1)',
    'rgba(137, 122, 201, 1)',
    'rgba(231, 198, 110, 1)',
    'rgba(185, 129, 159, 1)',
    'rgba(170, 188, 126, 1)',
    'rgba(217, 118, 89, 1)',
    'rgba(146, 111, 178, 1)',
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
    .then(data => {console.log(data); return data})
    .then(data => {
        for (const amount of data.data) {
            amountJson.push({x: amount.ingredient_name, y: amount.amount});
            amountNames.push(amount.ingredient_name);
            // amountPercentages.push(amount.amount);
        };
        return data})
    .then(data => {
        if (data.data.length !== 0) {

            const testChart = new Chart(graphCanvas, {
                type: "bar",
                data: {
                    labels: amountNames, 
                    datasets: [{                                    // array of dataset objects
                        label: "Baker's Percentage",               // labels on x axis
                        data: amountJson,                           // size of each bar
                        backgroundColor: backgroundColors,
                        borderColor: borderColors,
                        borderWidth: 3,
                        hoverBorderWidth: 5
                    }]
                },
                options: {
                    scales: {
                        xAxes: [{
                            scaleLabel: {
                                display: true,
                                labelString: "Ingredients",
                                fontSize: 22,
                                fontColor: 'rgba(255, 255, 255, 1)',
                            },
                            ticks: {
                                fontSize: 18,
                                fontColor: 'rgba(255, 255, 255, 1)'
                            }
                        }],
                        yAxes: [{
                            ticks: {
                                min: 0,
                                max: 120,
                                fontSize: 18,
                                fontColor: 'rgba(255, 255, 255, 1)'
                            },
                            scaleLabel: {
                                display: true,
                                labelString: "Baker's Percentage",
                                fontSize: 22,
                                fontColor: 'rgba(255, 255, 255, 1)'
                            },
                        }],
                    }   
                }
            }
        );
    };  
    

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
