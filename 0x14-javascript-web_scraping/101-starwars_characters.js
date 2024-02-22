#!/usr/bin/node
const request = require('request');

const movie_id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode == 200) {
    const movieData = JSON.parse(body);
    const dd = movieData.characters;

    function printNames (index) {
      if (index < dd.length) {
        request.get(dd[index], function (error, response, body1) {
          if (error) {
            console.log(error);
            printNames(index + 1);
          } else if (response.statusCode === 200) {
            const moviedata1 = JSON.parse(body1);
            console.log(moviedata1.name);
            printNames(index + 1);
          } else {
					 console.log(`Error code: ${response.statusCode}`);
            printNames(index + 1);
          }
        });
      }
    }
    printNames(0);
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});
