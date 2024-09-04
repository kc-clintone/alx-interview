#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
if (!movieID) {
  console.error('Please provide a Movie ID as a positional argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making the API request:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  characterUrls.forEach(url => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error making the API request for character:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch character data: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

