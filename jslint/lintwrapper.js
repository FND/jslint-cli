// JSLint wrapper
//
// Usage:
//   $ cat $filename | js -f fulljslint.js -f json2.js -f lintwrapper.js

// lint code from stdin
function lint(options) { // XXX: options currently unused
	var code = readlines();
	var status = JSLINT(code, options); // XXX: status unused
	return JSON.stringify(JSLINT.errors);
}

// inspired by http://whereisandy.com/code/jslint/
function readlines() {
	var EOFCount = 10; // number of blank lines indicating EOF
	var lines = [];
	var blankcount = 0;
	while(blankcount < EOFCount) {
 		var line = readline();
		blankcount = line === "" ? blankcount + 1 : 0;
		lines.push(line);
	}
	lines.splice(lines.length - EOFCount, EOFCount);
	return lines;
}

print(lint());
