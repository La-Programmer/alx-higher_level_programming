#!/usr/bin/node

const { argv } = require('node:process');

const fs = require('fs');

let file1Data;
let file2Data;

try {
  file1Data = fs.readFileSync(argv[2], 'utf8');
  file2Data = fs.readFileSync(argv[3], 'utf8');
} catch (err) {
  console.error(err);
}

file1Data += '\n';
file2Data += '\n';
fs.writeFile(argv[4], file1Data, err => {
  if (err) {
    console.error('Error writing to file: ', err);
  }
});

fs.appendFile(argv[4], file2Data, err => {
  if (err) {
    console.error('Error writing to file: ', err);
  }
});
