

/*
* 
* Requires:
* /common/scripts/toCamelCase.js
* 
* get computed style for an element - call like so:
* getComputedStyle(elementObjectReference, 'CSSStyleProperty')
* eg: getComputedStyle(document.getElementById('test'), 'background-color')
* 
* Be careful - this can return unexpected data - FPUs, colours as RGB, keywords in one browser, integers in another (MacIE handily returns boolean false for zero values such as "0px") - make sure you check what you get back, it won't necessarily be in the format it's written in the CSS. Also note that it might not return shorthand values - instead of querying for 'padding', you may have to query for 'padding-top' *and* 'padding-right' *and* 'padding-bottom' and etc etc...
*/

function fGetComputedStyle(oElm, sProperty) {	
	if (oElm.currentStyle) {
		// IE =<6 method
		// replaces previous nasty: return eval('oElm.currentStyle.' + toCamelCase(sProperty));
		return oElm.currentStyle[toCamelCase(sProperty)];
	} else if (document.defaultView && document.defaultView.getComputedStyle) {
		// Mozilla/W3C DOM method
		return document.defaultView.getComputedStyle(oElm, '').getPropertyValue(sProperty);
	} else {
		// neither IE =<6 method or Mozilla/W3C DOM method used
		return false;
	}
}
