const name = prompt("Enter name")
const housenumber = Math.floor(Math.random() * 4) + 1;

if (housenumber === 1) {
    house = "Gryffindor";
} else if (housenumber === 2) {
    house = "Slytherin";
}
else if (housenumber === 3) {
    house = "Hufflepuff";
}
else {
    house = "Ravenclaw"
}

document.querySelector("#target").innerHTML = `${name}, you are ${house}.`;