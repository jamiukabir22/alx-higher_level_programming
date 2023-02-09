#!/usr/bin/node

const sf = require('fs');

sf.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
	if (err){
		console.log(err);
	}
});
