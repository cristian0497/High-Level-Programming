#!/usr/bin/node
const len = parseInt(process.argv[2]);
if (isNaN(len) === true) {
  console.log('Missing size');
} else if (len > 0) {
  for (let x = 0; x < len; x++) {
    console.log('X'.repeat(len));
  }
}
