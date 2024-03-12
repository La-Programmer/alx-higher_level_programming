#!/usr/bin/node
const { argv } = require('node:process');

const myArg = argv[2];
const myInt = Math.floor(Number(myArg));
if (Number(myArg)) {
  console.log('My number: ' + myInt);
} else {
  console.log('Not a number');
}
