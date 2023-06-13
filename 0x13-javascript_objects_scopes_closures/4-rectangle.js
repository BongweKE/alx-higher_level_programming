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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    [this.height, this.width] = [this.height, this.width].map(i => i * 2);
  }
}

module.exports = Rectangle;
