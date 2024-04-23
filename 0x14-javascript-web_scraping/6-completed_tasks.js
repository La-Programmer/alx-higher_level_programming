#!/usr/bin/node

const request = require('request');

const getCmdArgs = () => process.argv.slice(2);

const url = getCmdArgs()[0];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const result = {};
    const bodyJson = JSON.parse(body);
    let user = 0;
    for (let i = 0; i < bodyJson.length; i++) {
      if (user !== bodyJson[i].userId && bodyJson[i].completed === true) {
        console.log(`Is user: ${user} equal to apiUser: ${bodyJson[i].userId}`)
        user = bodyJson[i].userId;
        result[user] = 1;
        console.log(result);
      } else if (user === bodyJson[i].userId && bodyJson[i].completed === true) {
        console.log(`Is user: ${user} equal to apiUser: ${bodyJson[i].userId}`)
        result[user] += 1;
      }
    }
    console.log(result);
  }
});
