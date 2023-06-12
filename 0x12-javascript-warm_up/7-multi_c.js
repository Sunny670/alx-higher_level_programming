#!/usr/bin/node
const z = Math.floor(Number(process.argv[2]));
if (isNaN(z)) {
  console.log('Missing number of occurrences');
} else {
  for (let y = 0; y < z; y++) {
    console.log('C is fun');
  }
}