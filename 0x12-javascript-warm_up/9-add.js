#!/usr/bin/node

const process = require('process');
const args = process.argv;
const arg2 = args[2];
const arg3 = args[3];
const number = parseInt(arg2);
const num = parseInt(arg3);

if (isNaN(number) || isNaN(num)) {
  console.log('NaN');
} else {
	console.log(number + num);
}
