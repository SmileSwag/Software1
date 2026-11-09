const n1=parseInt(prompt("Enter the first number:"));
const n2=parseInt(prompt("Enter the second number:"));
const n3=parseInt(prompt("Enter the third number:"));

document.querySelector("#target").innerHTML=`
sum:${n1 +n2 +n3};
product:${n1*n2*n3};
average:${(n1+n2+n3)/3};
`;