#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18';
if (process.argv[2] === 'https://swapi-api.hbtn.io/api/films') {
  request.get(url, function (error, body) {
    if (error) {
      console.log(error);
    } else {
      const full = JSON.parse(body.body);
      console.log("" + full.films.length);
    }
  });
}
