const dice = parseInt(prompt("Enter number of dice"));

let sum = 0;

for (let i = 0; i < dice; i++) {
    const roll = Math.floor(Math.random() * 6) + 1;
    sum += roll;
}

console.log(`Sum of ${dice} dice rolls: ${sum}`);