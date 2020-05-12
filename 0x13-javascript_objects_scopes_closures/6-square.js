#!/usr/bin/node
const newSquare = require('./5-square');

class Square extends newSquare {
  charPrint (c) {
    for (let x = 0; x < this.width; x++) {
      console.log((c || 'X').repeat(parseInt(this.width)));
    }
  }
}

module.exports = Square;
