#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const line = 'X'.repeat(this.width);
    let h = 0;
    while (h < this.height) {
      console.log(line);
      h += 1;
    }
  }
}

module.exports = Rectangle;
