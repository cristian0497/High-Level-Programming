#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let x = 0; x < this.size; x++) {
      console.log((c || 'X').repeat(parseInt(this.size)));
    }
  }
}
module.exports = Square;
