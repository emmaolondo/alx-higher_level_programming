#!/usr/bin/node
// functions

// const {argv} = require('node:process');
const val = parseInt(process.argv[2]);
// const v = parseInt(process.argv[3])

function factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
if (isNaN(val)) {
  console.log(1);
} else {
  console.log(factorial(val));
}
