#!/usr/bin/node
// count args without default one
const argsNo = process.argv.length - 2;

let reply;

if (argsNo === 0) {
  reply = 'No argument';
} else {
  reply = process.argv[2];
}

console.log(reply);
