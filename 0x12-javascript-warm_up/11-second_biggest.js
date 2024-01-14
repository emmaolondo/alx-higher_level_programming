#!/usr/bin/node

/*
 * Print the second largest number
 */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).map(Number);// convert args to numbers
  // sort in descending order
  const sorted = list.sort((a, b) => b - a);
  console.log(sorted[1]);
}
