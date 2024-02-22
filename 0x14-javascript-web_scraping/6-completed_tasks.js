#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const i in tasks) {
      if (tasks[i].completed === true) {
        if (completed[tasks[i].userId] === undefined) {
          completed[tasks[i].userId] = 1;
        } else {
          completed[tasks[i].userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});
