#!/usr/bin/node

let _Var;
if (typeof process.argv[2] === 'undefined') {
  _Var = 'No argument';
} else {
  _Var = process.argv[2];
}
console.log(_Var);
