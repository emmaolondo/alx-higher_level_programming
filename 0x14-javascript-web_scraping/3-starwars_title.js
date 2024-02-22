#!/usr/bin/node
const request = require('request');

const movie_id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request.get(url, function(error, response, body){
	if (error) {
		console.log(error);
	} else if (response.statusCode == 200) {
		const movieData = JSON.parse(body);
		console.log(movieData.title);
	} else {
		console.log(`Error code: ${response.statusCode}`);
	}
});
