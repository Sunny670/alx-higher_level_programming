#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print () {
    let row = '';
    for (let a = 0; a < this.width; a++) {
      row += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
