#!/usr/bin/node
// Create a count without the defaults
const argNo = process.argv.length - 2;

let reply;

if (argNo === 0) {
  reply = 'No argument';
} else if (argNo === 1) {
  reply = 'Argument found';
} else {
  reply = 'Arguments found';
}
console.log(reply);
