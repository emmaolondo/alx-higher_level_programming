#!/usr/bin/node
// Write a script that prints x times “C is fun”
const val = parseInt(process.argv[2]);

if (isNaN(val)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;

  while (i < val) {
    console.log('C is fun');
    i++;
  }
}
