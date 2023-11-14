#!/usr/bin/node
// create an add function

function add (a, b) {
//  return a + b;
// let a = process.argv[2];
// let b = process.argv[3];
  return a + b;
}
const f = process.argv[2];
const s = process.argv[3];

console.log(add(parseInt(f), parseInt(s)));
