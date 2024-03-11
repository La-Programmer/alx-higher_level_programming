#!/usr/bin/node
const { argv } = require('node:process');

let first = argv[2];
let second = argv[3];

console.log(first + ' is ' + second);
