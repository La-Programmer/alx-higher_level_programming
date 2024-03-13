#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	let counter = 0;
	list.map(
		item => {
			if (item === searchElement) {
				counter++;
			}
		}
	)
	return counter;
}
