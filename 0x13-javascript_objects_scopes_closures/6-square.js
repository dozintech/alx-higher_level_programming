#!/usr/bin/node
const Square0 = require('./5-square');
class Square extends Square0 {
  charPrint (c) {
    let mark = c;
    let row = '';
    if (c === undefined) {
      mark = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      row += mark;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
