#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    let char;
    if (c) {
      char = c;
    } else {
      char = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let result = '';
      for (let i = 0; i < this.size; i++) {
        result += char;
      }
      console.log(result);
    }
  }
}

module.exports = Square;
