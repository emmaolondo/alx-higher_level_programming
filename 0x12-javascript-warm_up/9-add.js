#!/usr/bin/node
// functions

const val = parseInt(process.argv[2]);
const v = parseInt(process.argv[3]);

function add (a, b) {
  return (a + b);
}
if (isNaN(val) || isNaN(v)) {
  console.log('NaN');
} else {
  console.log(add(val, v));
}
