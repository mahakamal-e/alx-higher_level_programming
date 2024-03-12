#!/usr/bin/node

const list = require('./100-data').list;
const mapList = list.map((val, idx) => val * idx);
console.log(list);
console.log(mapList);
