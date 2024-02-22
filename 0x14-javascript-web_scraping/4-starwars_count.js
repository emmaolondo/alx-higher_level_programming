#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const characterId = 18;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieData = JSON.parse(body).results;
    const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;
    const withWedges = movieData.filter(film => film.characters.includes(characterUrl));
    console.log(withWedges.length);
  }
});
