#!/usr/bin/node

const fs = require('fs');
const getCmdArgs = () => process.argv.slice(2);

const filePath = getCmdArgs()[1];
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
