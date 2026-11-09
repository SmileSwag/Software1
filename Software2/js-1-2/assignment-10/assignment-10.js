const diceCount = parseInt(prompt("Enter number of dice:"));
const targetSum = parseInt(prompt("Enter the sum of interest:"));

const target = document.querySelector("#target");

const totalrounds = 10000;
let count = 0;

for (let i = 0; i < totalrounds; i++) {
    let currentsum = 0;

    for (let j = 0; j < diceCount; j++) {
        const roll = Math.floor(Math.random() *6) + 1;
        currentsum += roll;
    }
    if (currentsum === targetSum) {
        count++;
    }
}

const probability = ((count / totalrounds) * 100).toFixed(2);

target.innerHTML = `Probability to get sum ${targetSum} with ${diceCount} dice is ${probability}%`;