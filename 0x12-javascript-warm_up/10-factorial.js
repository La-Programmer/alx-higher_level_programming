#!/usr/bin/node

const { argv } = require('node:process');

function factorial (num) {
  if (num <= 1 || !num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const myInt = Math.floor(Number(argv[2]));
const result = factorial(myInt);
console.log(result);
