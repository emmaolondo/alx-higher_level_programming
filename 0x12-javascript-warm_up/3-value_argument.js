#!/usr/bin/node

const { argv } = require('node:process');

// print first argument in the console
const firstArgv = argv[2];

if (firstArgv === undefined) {
  console.log('No argument');
} else {
  console.log(firstArgv);
}
