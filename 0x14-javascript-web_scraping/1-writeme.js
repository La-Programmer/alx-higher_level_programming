#!/usr/bin/node

const getCmdArgs = () => process.argv.slice(2);
const fs = require('fs');

const argsList = getCmdArgs();
const filePath = argsList[0];
const stringToWrite = argsList[1];

fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
