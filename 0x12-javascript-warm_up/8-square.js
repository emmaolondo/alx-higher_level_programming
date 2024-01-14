#!/usr/bin/node

const process = require('process');
const args = process.argv;
const arg2 = args[2];
const size = parseInt(arg2);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
	  let row = '';
	  for (let j = 0; j < size; j++) {
		  row += 'X';
	  }
	  console.log(row);
  }
}
