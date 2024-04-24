#!/usr/bin/node

const movieId = process.argv;
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const movieData = JSON.parse(body);

  movieData.characters.forEach(characterUrl => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
