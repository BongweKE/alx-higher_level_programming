#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let [i, count] = [0, 0];
  const max = list.length;

  while (i < max) {
    if (list[i] === searchElement) {
      count += 1;
    }
    i += 1;
  }

  return count;
};
