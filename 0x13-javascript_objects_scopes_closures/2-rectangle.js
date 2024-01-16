#!/usr/bin/node

// Write a class Rectangle that defines a rectangle:

module.exports = class Rectangle {
  constructor (w, h) {
    if ((typeof h === 'number') && (typeof w === 'number') && (h > 0) && (w > 0)) {
      this.height = h;
      this.width = w;
    }
  }
};
