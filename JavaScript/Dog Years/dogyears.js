//Your Name in lowercase only
const myName = "Meow".toLowerCase();

//Your Age
const myAge = 33;

//Early Years
let earlyYears = 2;
earlyYears *= 10.5;

//Later Years
let laterYears = myAge - 2;
// Number of dog years accounted by your later days
laterYears *= 4; 

//My Age in Dog Years
let myAgeInDogYears = earlyYears + laterYears;

//Print the results
console.log(`My Name is: ${myName}`);
console.log(`My Age is: ${myAge}`);
console.log(`My Early Years are: ${earlyYears}`);
console.log(`My Later Years are: ${laterYears}`);
console.log(`My Age in Dog Years are: ${myAgeInDogYears}`);

//Final result in summary
console.log(`My name is ${myName}. I am ${myAge} years old in human years which is myAgeInDogYears years old in dog years.`);