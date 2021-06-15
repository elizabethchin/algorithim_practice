def nonConstructibleChange(coins):
    # Write your code here.
    
	sorted_coins = sorted(coins)
	
	current_change = 0
	
	for coin in sorted_coins:
		
		if coin > current_change + 1:
			return current_change + 1
		
		else:
			current_change += coin
			
	return current_change + 1


coins = ""
print(nonConstructibleChange(coins))