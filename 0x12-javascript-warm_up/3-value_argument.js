#!/usr/bin/node
const { argv } = require('node:process');

// print first argument in the console
const firstArgv = argv[2];
const noArgv = argv[1];
if (firstArgv) {
  console.log(firstArgv);
} else if (noArgv) {
  console.log('no Argument');
}
