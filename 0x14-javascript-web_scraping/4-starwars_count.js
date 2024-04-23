#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    film.characters.forEach(character => {
      if (character.includes('/18/')) {
        count++;
      }
    });
  });

  console.log(count);
});
