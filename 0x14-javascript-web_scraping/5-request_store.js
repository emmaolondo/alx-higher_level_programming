#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
