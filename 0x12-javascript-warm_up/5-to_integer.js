#!/usr/bin/node
// concatination
const { argv } = require('node:process');
const v = parseInt(argv[2]);

if (isNaN(v)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + v);
}
