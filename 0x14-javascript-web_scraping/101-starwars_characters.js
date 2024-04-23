#!/usr/bin/node

const request = require('request');
const Promise = require('bluebird');

const getCmdArgs = () => process.argv.slice(2);

const movieId = getCmdArgs()[0];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body);
    console.log(result.characters);
    // for (let i = 0; i < result.characters.length; i++) {
    //   const newUrl = result.characters[i];
    //   console.log(newUrl);
    //   request(newUrl, (err, res, body) => {
    //     if (err) {
    //       console.log(err);
    //     } else {
    //       const character = JSON.parse(body);
    //       console.log(`Character name: ${character.name}  character ID: ${character.url}`);
    //     }
    //   });
    // }
    const characterPromises = result.characters.map(newUrl => {
      return new Promise((resolve, reject) => {
        request(newUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            const character = JSON.parse(body);
            resolve(`Name: ${character.name}  ID: ${character.url}`);
          }
        });
      });
    });
    Promise.all(characterPromises)
      .then(characters => {
        characters.forEach(character => console.log(character));
      })
      .catch(error => console.error(error));
  }
});
