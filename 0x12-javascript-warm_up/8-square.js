#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (!size) {
  /**
      * Given that NaN is false and !false is true
      * this will captute the situation where
      * size is not input or it is input as a string, etc
      */
  console.log('Missing size');
} else {
  // we have size as an actionable integer
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i += 1;
  }
}
