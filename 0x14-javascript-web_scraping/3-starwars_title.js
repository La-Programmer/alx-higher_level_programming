#!/usr/bin/node

const request = require('request');

const getCmdArgs = () => process.argv.slice(2);

const id = getCmdArgs()[0];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(body.title);
  }
});
