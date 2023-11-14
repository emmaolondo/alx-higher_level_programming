#!/usr/bin/node
//  a script that prints square

const arg = process.argv[2];
const argint = parseInt(arg);
let s = '';
if (arg === undefined || isNaN(argint)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argint; i++) {
    s += '* ';
  }
  for (let j = 0; j < argint; j++) {
    console.log(s);
  }
}
