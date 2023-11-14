#!/usr/bin/node
// a script that prints My number  if the first argument can be converted to an integer

const number = process.argv[2];

console.log(parseInt(number));
