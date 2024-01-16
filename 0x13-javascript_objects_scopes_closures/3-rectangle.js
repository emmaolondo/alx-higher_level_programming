#!/usr/bin/node

// Write a class Rectangle that defines a rectangle:

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0 && w !== h) {
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
};
