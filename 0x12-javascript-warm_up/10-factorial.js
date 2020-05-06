#!/usr/bin/node
function factorial (value) {
  if (value === 0) {
    return 1;
  } else {
    return value * factorial(value - 1);
  }
}
const val = parseInt(process.argv[2]);
if (isNaN(val) === true) {
  console.log('1');
} else {
  console.log('%s', factorial(val));
}
