#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv.slice(2)[0], 'utf8', function(err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
