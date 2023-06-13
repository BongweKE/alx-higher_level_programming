#!/usr/bin/node

const Square0 = require('./5-square.js');

class Square extends Square0 {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c !== undefined) {
      const line = c.repeat(this.size);

      let i = 0;
      while (i < this.size) {
        console.log(line);
        i += 1;
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
