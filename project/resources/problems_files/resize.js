

/*
* Script to adjust elements bottom padding to make them appear same height.
* Requires:
* /common/scripts/portable/getComputedStyles.js
* /common/scripts/findPosition.js
* /common/scripts/portable/addEventListener.js
*/

// sort multidimensional array by 4th dimension
function sortBy4th(a,b)
{
	if (a[3]>b[3]) return -1;
	if (a[3]<b[3]) return 1;
	return 0;
}

function setMeasurements(elmStats)
{
	var largest = elmStats[0][3];
	for (var i=1; i<elmStats.length; i++) {// tweak elements except one furthest down page
		var difference = largest - elmStats[i][3];
		// test to see if it's possible to check what padding-bottom has already been set, then resize elements
		if (fGetComputedStyle(elmStats[i][0], 'padding-bottom') != false) {
			elmStats[i][0].style.paddingBottom = parseInt(fGetComputedStyle(elmStats[i][0], 'padding-bottom')) + difference + 'px';
		} else {
			elmStats[i][0].style.paddingBottom = difference + 'px';
		}
		elmStats[i][0].style.marginBottom = '0px';
	}
}

function getMeasurements(elmids)
{
	var elmStats = new Array();
	for (var i=0; i<elmids.length; i++) {// find element stats - position, height, bottom margin	
		var elm = document.getElementById(elmids[i]);
		var bottom = findPosition(elm)[1] + elm.offsetHeight;
		elmStats[i] = new Array(elm, findPosition(elm)[1], elm.offsetHeight, bottom, elmids[i]);
	}
	elmStats.sort(sortBy4th);// sort array by element with bottom margin furthest down page
	setMeasurements(elmStats);
}

function trigger()
{
	if (!document.getElementById || typeof document.body.offsetHeight == 'undefined') {//DOM feature sniffing
		return;
	}
	window.setTimeout('resize()', 100);// timeout to deal with IE JS minmax resizing - dirty hack
}


