#!/usr/bin/node

const fileS = require('fs');
const firstFile = fileS.readFileSync(process.argv[2], 'utf8');
const secondFile = fileS.readFileSync(process.argv[3], 'utf8');

fileS.writeFileSync(process.argv[4], firstFile + SecondFile);
