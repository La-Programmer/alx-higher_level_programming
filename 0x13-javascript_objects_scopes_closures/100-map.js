#!/usr/bin/node

const list = require('./100-data').list;

let counter = 0;
const newList = list.map((item, counter) => {
	let newItem = item * counter;
	counter++;
	return newItem;
});
console.log(list);
console.log(newList);
