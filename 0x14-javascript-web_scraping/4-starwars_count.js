#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body);
    const movieList = result.results;
    let count = 0;
    for (let i = 0; i < movieList.length; i++) {
      for (let j = 0; i < movieList[i].characters.length; j++) {
        if (movieList[i].characters[j].includes('18')) {
          count++;
          break;
        }
      }
    }
    return count;
  }
});
