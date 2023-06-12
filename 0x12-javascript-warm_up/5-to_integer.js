#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));

let _Var;
if (isNaN(num)) {
  _Var = 'Not a number';
} else {
  _Var = `My number: ${num}`;
}
console.log(_Var);
