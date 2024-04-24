#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const printCharacterName = (characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  };

  characters.forEach(printCharacterName);
});
