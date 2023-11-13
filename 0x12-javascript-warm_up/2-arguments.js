#!/usr/bin/node
const { argv } = require('node:process');

const numberArgv = argv.length - 2;

if (numberArgv === 1) {
  console.log('Argument found');
} else if (numberArgv > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
