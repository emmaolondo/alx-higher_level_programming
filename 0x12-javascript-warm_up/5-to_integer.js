#!/usr/bin/node
// a script that prints My number  if the first argument can be converted to an integer

const number = process.argv[2];
const parse_int = parseInt(number);

if (isNaN(parse_int)) {
  console.log("Not a number");
} else {
  console.log("My number: " + parse_int);
}
