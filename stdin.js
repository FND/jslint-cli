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
