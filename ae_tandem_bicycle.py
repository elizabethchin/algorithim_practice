def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.

# """
# red shirts
# blue shirts
# if fastest = true return max speed else return min speed
# """
	speed = 0
	if fastest == False:
		redShirtSpeeds.sort(reverse=True)
		blueShirtSpeeds.sort(reverse=True)
		for i in range(len(redShirtSpeeds)):
			redShirtSpeed = redShirtSpeeds[i]
			blueShirtSpeed = blueShirtSpeeds[i]
			speed += max(redShirtSpeed, blueShirtSpeed)
		return speed
	
	else:
		redShirtSpeeds.sort()
		blueShirtSpeeds.sort(reverse=True)
		for i in range(len(redShirtSpeeds)):
			redShirtSpeed = redShirtSpeeds[i]
			blueShirtSpeed = blueShirtSpeeds[i]
			speed += max(redShirtSpeed, blueShirtSpeed)
			
		return speed
		
		