#!/usr/bin/node

const process = require('process');
const args = process.argv;
const arg2 = args[2];

if (arg2 === undefined) {
  console.log('No argument');
} else {
  console.log(arg2);
}
