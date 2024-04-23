#!/usr/bin/node

const request = require('request');

const getCmdArgs = () => process.argv.slice(2);

const movieId = getCmdArgs()[0];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body);
    for (let i = 0; i < result.characters.length; i++) {
      const newUrl = result.characters[i];
      request(newUrl, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
});
