#!/usr/bin/node
//  a script that prints x times “C is fun”

const arg = process.argv[2];
const argint = parseInt(arg);

if (arg === undefined || isNaN(argint)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argint; i++) {
    console.log('C is fun');
  }
}
