#!/usr/bin/node

/*
 * Pintr the second largest number
 */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[3]);
}
