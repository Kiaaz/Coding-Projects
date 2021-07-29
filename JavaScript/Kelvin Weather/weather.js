//Today's forecast in Kelvin
const kelvin = 293;

//Convert to Celcius
const celcius = kelvin - 273;

//Convert to Fahrenheit 
const fahrenheit = Math.floor(celcius * (9/5) + 32);

//Convert to Newton 
const newton = Math.floor(celcius * (3/100));

//Print the results
console.log(`Today's forecast in Kelvin is: ${kelvin}`);
console.log(`Today's forecast in Celcius is: ${celcius}`);
console.log(`Today's forecast in Fahreinheit is: ${fahrenheit}`);
console.log(`Today's forecast in Newton is: ${newton}`);
