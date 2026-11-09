const year = prompt("Enter a year")
const isyear = parseInt(year)

if ((isyear % 4 === 0 && isyear % 100 !== 0) || isyear % 400 === 0) {
    anwser = `${isyear} is a leap year.`;
} else {
    anwser = `${isyear} is not a leap year.`;
}

document.querySelector("#target").innerHTML = answer;