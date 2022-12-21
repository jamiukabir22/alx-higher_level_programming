#!/usr/bin/node
const args = process.argv;
if (isNaN(Number(args[2]))) {
	console.log('Missing number of occurances');
} else {
	for (let h = 0; h < NUmber(args[2]); h++) {
		console.log('C is fun');
	}
}
