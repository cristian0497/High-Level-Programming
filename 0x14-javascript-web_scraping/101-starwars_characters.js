#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const values = JSON.parse(body.body).characters;
    for (let x = 0; x < values.length; x++) {
      request.get(values[x], function (error, characters) {
        if (error) {
          console.log(error);
        } else {
	  console.log(values[x])
          console.log(JSON.parse(characters.body).name);
        }
      });
    }
  }
});
