#!/usr/bin/node
const count = process.argv.length;

let _Var;
if (count === 2) {
  _Var = 'No argument';
} else if (count === 3) {
  _Var = 'Argument found';
} else {
  _Var = 'Arguments found';
}
console.log(_Var);