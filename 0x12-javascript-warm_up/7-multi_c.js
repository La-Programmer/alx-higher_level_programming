#!/usr/bin/node
const { argv } = require('node:process');

let myArg = argv[2];
let myInt = Math.floor(Number(myArg));
if (Number(myArg)) {
  for (let counter = 0; counter < myInt; counter++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
