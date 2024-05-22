#!/usr/bin/node

const fs = require('fs');
// Import built-in Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Use fs.readFile() to read contents of the file specified as a command-line argument
  // 'utf8' specifies encoding of the file being read

  if (error) {
    // If an error occurs during the file read operation, 'error' parameter will contain an error object.
    console.error('Error reading the file:', error);

  } else {
    // If file is read successfully, the 'content' parameter will contain contents of the file as a string.
    console.log(content);
  }
});
