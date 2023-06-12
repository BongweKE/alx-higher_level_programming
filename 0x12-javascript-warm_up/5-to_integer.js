#!/usr/bin/node
const valChecked = process.argv[2];
const numVal = parseInt(valChecked);
let output;

if (numVal) {
  // Numbers are true
  output = `My number: ${numVal}`;
} else {
  /**
      * parseInt("String") = NaN which is false
      * Therefore here we have No numbers
      *
      */
  output = 'Not a number';
}

console.log(output);
