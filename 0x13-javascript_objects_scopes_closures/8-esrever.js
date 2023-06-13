#!/usr/bin/node

exports.esrever = function (list) {
  const temp = [];
  let i = list.length - 1;

  while (i >= 0) {
    temp.push(list[i]);
    i -= 1;
  }
  return temp;
};
