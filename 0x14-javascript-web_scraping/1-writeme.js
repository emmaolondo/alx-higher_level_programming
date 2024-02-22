#!/usr/bin/node
// A script that writes a string to a file
const fs = require('fs');
file = process.argv[2];
string = process.argv[3]
fs.writeFile(file, string, error => {
	if (error) console.log(error);
});
