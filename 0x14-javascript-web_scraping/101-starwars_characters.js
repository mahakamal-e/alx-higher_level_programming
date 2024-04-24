#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const movieCharacters = JSON.parse(body).characters;

    const promises = movieCharacters.map((character) => {
      return new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) reject(error);
          else resolve(JSON.parse(body).name.toUpperCase());
        });
      });
    });

    Promise.all(promises).then((characterNames) => {
      characterNames.forEach((characterName) => {{
        console.log(characterName);
      });
    });
  }
});
