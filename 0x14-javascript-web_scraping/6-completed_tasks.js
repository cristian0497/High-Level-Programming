#!/usr/bin/node
const request = require('request');
const Dic = {};
request.get(process.argv[2], function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const values = JSON.parse(body.body);
    for (let x = 0; x < values.length; x++) {
      if (Dic[values[x].userId] === undefined) {
        Dic[values[x].userId] = 0;
      } else {
        if (values[x].completed === true) {
          Dic[values[x].userId] += 1;
        }
      }
    }
    console.log(Dic);
  }
});
