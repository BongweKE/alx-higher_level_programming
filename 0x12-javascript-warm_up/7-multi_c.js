#!/usr/bin/node

const x = parseInt(process.argv[2]);
const argCount = process.argv.length - 2;

if ((argCount === 0) || !x) {
  /**
      * Check to see if there are no args
      * or the first argument can't be converted to an
      * integer
      */
  console.log('Missing number of occurrences');
} else {
  let i = 0;

  while (i < x) {
    console.log('C is fun');
    i += 1;
  }
}
