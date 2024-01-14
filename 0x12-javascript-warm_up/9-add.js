#!/usr/bin/node

function add (a, b) {
  const process = require('process');
  const args = process.argv;
  const arg2 = args[2];
  const arg3 = args[3];
  a = parseInt(arg2);
  b = parseInt(arg3);

  if (isNaN(a) || isNaN(b)) {
    return ('NaN');
  } else {
    return a + b;
  }
}

// Display the results
console.log(add());
