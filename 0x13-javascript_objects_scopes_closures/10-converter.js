#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    const result = num.toString(base);
    return result;
  };
};
