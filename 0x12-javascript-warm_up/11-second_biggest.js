#!/usr/bin/node

const listLen = process.argv.length - 2;
let output;
if (listLen < 2) {
  output = 0;
} else {
  const myList = process.argv.slice(2, listLen + 2).map(i => parseInt(i));
  myList.sort();

  output = myList[listLen - 2];
}
console.log(output);
