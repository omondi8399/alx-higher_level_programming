#!/usr/bin/node

const argument = process.argv;
const number = parseInt(argument[2]);

if (isNaN(number) || number === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
