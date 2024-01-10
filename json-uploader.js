const fs = require('fs');
const axios = require('axios');

const url = 'http://10.10.110.38:8080/patenty-utrativshie-silu/Patents.json';
const filePath = './Patents.json';

async function updateJsonFile() {
  try {
    const jsonData = fs.readFileSync(filePath, 'utf8');
    console.log('JSON file content:', jsonData);
    const response = await axios.post(url, jsonData, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    console.log('JSON file updated successfully!', response);
  } catch (error) {
    console.error('Error updating JSON file on server:', error);
  }
}

updateJsonFile();