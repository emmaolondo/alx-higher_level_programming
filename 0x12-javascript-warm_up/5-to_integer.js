#!/usr/bin/node

const process = require('process');
const args = process.argv;
const arg2 = args[2];
const number = parseInt(arg2);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(number);
}
