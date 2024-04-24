#!/usr/bin/node
const movieId = process.argv;
const request = require('request');

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const moviesCharacters = JSON.parse(body).characters;

  moviesCharacters.forEach((character) => {
    request(character, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
