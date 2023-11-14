#!/usr/bin/node
// a script that prints My number  if the first argument can be converted to an integer

const number = process.argv[2];
const arg = parseInt(number);

if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
