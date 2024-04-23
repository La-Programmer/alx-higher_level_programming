#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const getCmdArgs = () => process.argv.slice(2);

const url = getCmdArgs()[0];
const filePath = getCmdArgs()[1];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
