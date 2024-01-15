#!/usr/bin/node

// Write a class Rectangle that defines a rectangle:

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print (c = 'x') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }

  // fuction that exchange the width and the heght
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // function that double the instances
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
