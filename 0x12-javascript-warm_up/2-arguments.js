#!/usr/bin/node

const argNum = process.argv.length;

if (argNum === 2) {
  console.log('No argument');
} else if (argNum === 3) {
  console.log('Argument found');
} else if (argNum === 4) {
  console.log('Arguments found');
}
