#!/usr/bin/node
const { argv } = require('node:process');

const myArg = argv[2];
const myInt = Math.floor(Number(myArg));
if (Number(myArg)) {
  for (let counter = 0; counter < myInt; counter++) {
    let output = '';
    for (let counter2 = 0; counter2 < myInt; counter2++) {
      output += 'X';
    }
    console.log(output);
  }
} else {
  console.log('Missing size');
}
