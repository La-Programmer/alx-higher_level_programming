#!/usr/bin/node

const { argv } = require('node:process');

const fs = require('fs');

let file1Data;
let file2Data;

try {
	file1Data = fs.readFileSync(argv[2], 'utf8');
} catch (err) {
	console.log(err);
}

try {
	file2Data = fs.readFileSync(argv[3], 'utf8');
} catch (err) {
	console.log(err);
}

if (file1Data.length != 0) {
	file1Data += '\n';
	fs.writeFile(argv[4], file1Data, err => {
		if (err) {
			console.error('Error writing to file: ', err);
		}
	});

}
if (file2Data.length != 0) {
	file2Data += '\n';
	fs.appendFile(argv[4], file2Data, err => {
		if (err) {
			console.error('Error writing to file: ', err);
		}
	});
}
