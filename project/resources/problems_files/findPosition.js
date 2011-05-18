function findPosition(elm)
{
	if(elm.offsetParent) {
		for(var left = 0, top = 0; elm.offsetParent; elm = elm.offsetParent) {
			left += elm.offsetLeft;
			top += elm.offsetTop;
		}
		return[left, top];
	} else {
		return[elm.x, elm.y];
	}
}