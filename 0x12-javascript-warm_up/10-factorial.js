#!/usr/bin/node

function factorial (a) {
  if (isNaN(a) || a <= 1) {
    return (1);
  } else {
    return a * factorial(a - 1);
  }
}

// Display the results
const process = require('process');
const args = process.argv;
const input = parseInt(args[2]);
console.log(factorial(input));
