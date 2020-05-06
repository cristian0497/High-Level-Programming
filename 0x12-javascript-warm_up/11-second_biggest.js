#!/usr/bin/node
const Maj = [];
const len = process.argv.length - 2;
if (len < 2) {
  console.log('0');
} else {
  for (let x = 0; x < len; x++) {
    Maj[x] = parseInt(process.argv[x + 2]);
  }
  console.log('%s', Maj.sort()[len - 2]);
}
