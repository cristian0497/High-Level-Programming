#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const full = JSON.parse(body.body).results;
    let cant = 0;
    const val = 'https://swapi-api.hbtn.io/api/people/18/';
    for (let x = 0; x < full.length; x++) {
      if (full[x].characters.includes(val)) {
        cant += 1;
      }
    }
    console.log(cant);
  }
});
