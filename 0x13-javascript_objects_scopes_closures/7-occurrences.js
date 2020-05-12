#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      ocurrences += 1;
    }
  }
  return ocurrences;
};
