#!/usr/bin/node

const request = require('request');

const getCmdArgs = () => process.argv.slice(2);

const url = getCmdArgs()[0];

request(url, (err, res, body) => {
  if (err) {
    console.log();
  }
  console.log(`code: ${res.statusCode}`);
});
