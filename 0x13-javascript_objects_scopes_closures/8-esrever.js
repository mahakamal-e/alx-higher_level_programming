#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const length = list.length;
  for (let i = length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList);
};
