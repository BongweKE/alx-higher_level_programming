#!/usr/bin/node

// use unpacking and destructing to create two variables
const [a, b] = [process.argv[2], process.argv[3]];

// use the backticked string for interpolation
const sentence = `${a} is ${b}`;
console.log(sentence);
