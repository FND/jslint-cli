// JSLint wrapper
//
// Usage:
//   $ cat $filename | js -f fulljslint.js -f stdin.js -f lintwrapper.js
// (json2.js is also required below Spidermonkey 1.8)

var options = {}; // XXX: currently unused
var code = readlines();

var status = JSLINT(code, options); // XXX: unused
var errors = JSON.stringify(JSLINT.errors);

print(errors);
