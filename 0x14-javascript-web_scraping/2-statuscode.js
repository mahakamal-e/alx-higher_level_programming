#!/usr/bin/node
const pathFile = process.argv[2];
const request = require('request');

request(pathFile, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
