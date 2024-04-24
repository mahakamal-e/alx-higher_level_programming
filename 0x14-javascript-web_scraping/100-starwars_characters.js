#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(url, (error, response, body) => {
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
