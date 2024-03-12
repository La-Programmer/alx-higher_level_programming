#!/usr/bin/node

const { argv } = require('node:process');

function secondLargest (intArray) {
  let a = 0;
  let b = 0;

  for (let i = 0; i < intArray.length; i++) {
    if (a < intArray[i]) {
      a = intArray[i];
    }
  }
  for (let i = 0; i < intArray.length; i++) {
    if (b < intArray[i] && intArray[i] < a) {
      b = intArray[i];
    }
  }
  return b;
}

const intArray = argv.map((item) => Number(item));
if (intArray.length < 3) {
  console.log(0);
} else if (intArray.length === 3) {
  console.log(0);
} else {
  const result = secondLargest(intArray);
  console.log(result);
}
