#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const fs = require('fs');

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    fs.writeFile(args[3], body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
