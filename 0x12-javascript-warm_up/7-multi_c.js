#!/usr/bin/node

const process = require('process');
const args = process.argv;
const arg2 = args[2];
const number = parseInt(arg2);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < number) {
    console.log('C is fun');
    i++;
  }
}
