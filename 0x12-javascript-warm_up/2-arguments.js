#!/usr/bin/node
const { argv } = require('node:process');

const numberArgv = argv.length - 2;

if (numberArgv === 0) {
  console.log('No argument');
} else if (numberArgv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
