#!/usr/bin/node

function closure (item) {
  let counter = 0;

  function inner (item) {
    console.log(`${counter}: ${item}`);
    counter++;
    return counter;
  }
  return inner;
}

exports.logMe = closure();
