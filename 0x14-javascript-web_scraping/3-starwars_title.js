#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body.body).title);
  }
});
