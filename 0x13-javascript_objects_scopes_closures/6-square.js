#!/usr/bin/node

// a class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const InitialSquare = require('./5-square');

class Square extends InitialSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
}

module.exports = Square;
