#!/usr/bin/node
const { argv } = require('node:process');

let myArg = argv[2];
let myInt = Math.floor(Number(myArg));
if (Number(myArg)) {
  console.log('My number: ' + myInt);
} else {
  console.log('Not a number');
}
