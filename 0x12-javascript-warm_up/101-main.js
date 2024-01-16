#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(7, function () {
  console.log('C is fun');
});
