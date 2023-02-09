#!/usr/bin/node

const requst = require('request');

const options = {
	url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
	headera: {
		'User-Agent': 'request'
	}
};

function callback (error, response, body) {
	if (!error && response.status.code == 200) {
		const info = JSON.parse(body);
		console.log(info.title);
	}
}

request(options, callback);
