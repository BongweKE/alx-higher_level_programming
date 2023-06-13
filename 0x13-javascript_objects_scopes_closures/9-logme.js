#!/usr/bin/node

exports.logMe = function (item) {
  if (globalThis.count !== undefined) {
    // console.log("Defined");
    globalThis.count += 1;
  } else {
    // console.log('undefined');
    globalThis.count = 0;
  }
  console.log(`${globalThis.count}: ${item}`);
};
