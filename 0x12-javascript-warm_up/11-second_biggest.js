#!/usr/bin/node
const Maj = [];
const len = process.argv.length - 2;
if (len < 2) {
  console.log('0');
} else {
  for (let x = 0; x < len; x++) {
    Maj[x] = process.argv[x + 2];
  }
  console.log(Maj.sort()[len - 2]);
}
