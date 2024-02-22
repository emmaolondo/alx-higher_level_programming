#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const character_id = 18;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body).results;
    const characterUrl = `https://swapi-api.alx-tools.com/api/people/${character_id}/`;
    const withWedges = movieData.filter(film => film.characters.includes(characterUrl));
    console.log(movieData.length);
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});
