#!/usr/bin/node

exports.converter = function (base) {
  function convertor (n) {
    return n.toString(base);
  }
  return convertor;
};
