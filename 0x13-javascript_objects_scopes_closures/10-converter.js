#!/usr/bin/node

exports.converter = function (base) {
  // create a closure to hold the base
  return function (x) {
    // the closure will this part
    return x.toString(base);
  };
};
