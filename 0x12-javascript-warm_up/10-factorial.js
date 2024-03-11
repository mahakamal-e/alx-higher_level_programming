#!/usr/bin/node

function factorial (numInput) {
  if (isNaN(numInput) || numInput === 0 || numInput === 1) {
    return (1);
  }
  return numInput * factorial(numInput - 1);
}

console.log(factorial(process.argv[2]));
