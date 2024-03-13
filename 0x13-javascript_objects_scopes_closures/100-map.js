#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map(item => {
  return item * list.indexOf(item);
});
console.log(list);
console.log(newList);
