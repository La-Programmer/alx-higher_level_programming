#!/usr/bin/node
const { argv } = require('node:process');

function add(a, b) {
  return a + b;
}

let a = Math.floor(Number(argv[2]));
let b = Math.floor(Number(argv[3]));
if (a && b) {
  console.log(add(a, b));
} else {
  console.log(NaN);
}
