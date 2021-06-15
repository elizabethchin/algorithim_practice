def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
	#sort in place/mutate input array so not using extra space therfore O(1) 
	#space ask intervieer if you can do this
	#this sorts in descending order
    redShirtHeights.sort(reverse=True) 
	blueShirtHeights.sort(reverse=True)
	
	shirtColorInFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
	for idx in range(len(redShirtHeights)):
		redShirtHeight = redShirtHeights[idx]
		blueShirtHeight = blueShirtHeights[idx]
		
		if shirtColorInFirstRow == "RED":
			if redShirtHeight >= blueShirtHeight:
				return False
		
		else:
			if blueShirtHeight >= redShirtHeight:
				return False
			
	return True