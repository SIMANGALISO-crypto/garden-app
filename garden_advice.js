// garden_advice.js

// Function to get gardening advice based on season and plant type
function getGardeningAdvice(season, plantType) {
    const adviceData = {
        summer: {
            general: "Water your plants regularly and provide some shade.",
            flower: "Use fertiliser to encourage blooms.",
            vegetable: "Keep an eye out for pests!",
        },
        winter: {
            general: "Protect your plants from frost with covers.",
            flower: "Keep flowers indoors if possible.",
            vegetable: "Use mulch to protect root vegetables.",
        },
        default: {
            general: "No advice for this season.",
            default: "No advice for this type of plant."
        }
    };

    let advice = "";

    const seasonAdvice = adviceData[season] || adviceData.default;
    advice += (seasonAdvice.general || adviceData.default.general) + "\n";

    if (plantType in seasonAdvice) {
        advice += seasonAdvice[plantType];
    } else {
        advice += adviceData.default.default;
    }

    return advice;
}

// Prompt the user for input (browser only)
let season = prompt("Enter the season (e.g., summer, winter):").toLowerCase();
let plantType = prompt("Enter the plant type (e.g., flower, vegetable):").toLowerCase();

// Get and display the advice
let gardeningAdvice = getGardeningAdvice(season, plantType);
console.log(gardeningAdvice);
