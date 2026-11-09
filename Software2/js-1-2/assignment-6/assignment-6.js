const target = document.querySelector("#target");
const shouldcalc = confirm("Should i calculate sqr root?");

if (shouldcalc) {
    const input = prompt("enter number");
    const number = parseFloat(input);


    if (number < 0) {
        target.innerHTML = "The square root of a negative number is not defined";
}
    else {
        const SqrRoot = Math.sqrt(number);
        target.innerHTML = `The sqr root of a ${number} is ${SqrRoot}.`;
}

}
else {
    target.innerHTML = "the square root is not calculated.";
}