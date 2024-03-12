#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let i = 0; i < this.width; i++) {
        result += 'X';
      }
      console.log(result);
    }
  }
}

module.exports = Rectangle;
