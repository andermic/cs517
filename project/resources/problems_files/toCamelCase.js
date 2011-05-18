/*
* convert string to CamelCase
*/
function toCamelCase(s) {
	// exp: 1 or more non-word characters followed by a word character
	var exp = /\W+(\w)/;
	for(; exp.test(s); s = s.replace(exp, RegExp.$1.toUpperCase()) );
	return s;
}