#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.width; i++) {
      let result = '';
      for (let j = 0; j < this.width; j++) {
        result += char;
      }
      console.log(result);
    }
  }
}

module.exports = Square;
