#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((item, counter) => {
  const newItem = item * counter;
  counter++;
  return newItem;
});
console.log(list);
console.log(newList);
