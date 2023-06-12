#!/usr/bin/node

const givenNum = parseInt(process.argv[2]);

function factorial (n) {
  if (n < 0) {
    return 'Undefined';
  } else if (!n) {
    // here, NaN and 0 are false
    // so !n covers both of them
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(givenNum));
