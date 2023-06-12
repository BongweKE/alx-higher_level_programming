#!/usr/bin/node
const argCount = process.argv.length - 2;

function add (a, b) {
  return a + b;
}

if (argCount < 2) {
  /**
      * missing arguments usually
      * evaluate to undefined which is different from
      * NaN and 9 + undefined = 9undefined
      */
  console.log(NaN);
} else {
  const myVals = process.argv.slice(2, 4);
  const [a, b] = myVals.map(i => parseInt(i));
  console.log(add(a, b));
}
