#!/usr/bin/node

const request = require('request');

const getCmdArgs = () => process.argv.slice(2);

const url = getCmdArgs()[0];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body);
    const movieList = result.results;
    console.log(movieList)
    let count = 0;
    for (let i = 0; i < movieList.length; i++) {
      for (let j = 0; i < movieList[i].characters.length; j++) {
        console.log(movieList[i].characters[j]);
        if (movieList[i].characters[j].includes('18')) {
          count++;
          break;
        }
      }
    }
    return count;
  }
});
