#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function printCast () {
  const charURLs = await makeRequest(URL);
  for (const charURL of charURLs.characters) {
    await makeRequest(charURL)
      .then(
        (body) => {
          console.log(body.name);
        }, (error) => {
          console.log(error);
        });
  }
}

printCast();
