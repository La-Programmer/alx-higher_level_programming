#!/usr/bin/node
const { argv } = require('node:process');

const myArg = argv[2];
const myInt = Math.floor(Number(myArg));
if (Number(myArg)) {
  for (let counter = 0; counter < myInt; counter++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
