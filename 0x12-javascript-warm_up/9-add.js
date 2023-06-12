#!/usr/bin/node
function add (x, z) {
  return x + z;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
