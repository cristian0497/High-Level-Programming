#!/usr/bin/node
const len = parseInt(process.argv[2]);
if (isNaN(len) === true) {
  console.log('Missing number of occurrences');
} else if (len > 0) {
  for (let x = 0; x < len; x++) {
    console.log('C is fun');
  }
}
