#!/usr/bin/node
// Write a script that prints x times “C is fun”
const val = parseInt(process.argv[2]);

if (isNaN(val)) {
  console.log('Missing Size');
} else {
  let i = 0;

  while (i < val) {
    let row = '';
    let j = 0;
    while (j < val) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
}
