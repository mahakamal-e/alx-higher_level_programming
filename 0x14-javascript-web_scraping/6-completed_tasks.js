#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const tasks = JSON.parse(body);

  const completedTasksByUser = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId]++;
      } else {
        completedTasksByUser[task.userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});
