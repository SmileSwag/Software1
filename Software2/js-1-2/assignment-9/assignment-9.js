const number = parseInt(prompt("Enter a integer"));
const target = document.querySelector("#target");

if (number <= 1) {
    target.innerHTML = `${number} is not a prime number`
}
    else {
    let isPrime = true;

    for (let i = 2; i < number; i++) {
        if (number % i === 0){
            isPrime = false;
            break;
        }
    }

    if (isPrime) {
    target.innerHTML= `${number} is a prime number.`;
    }   
    else{
    target.innerHTML = ` ${number} is not a prime number.`
    }
}