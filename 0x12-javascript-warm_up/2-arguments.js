#!/usr/bin/node
// const { argv } = require('node:process');

// const numberArgv = argv.length - 2;

if (process.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
