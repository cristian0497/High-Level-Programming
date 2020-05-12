#!/usr/bin/node
const fs = require('fs');
try {
  const info = fs.readFileSync(process.argv[2], 'utf-8');
  console.log(info);
} catch (error) {
  console.error(error);
}
