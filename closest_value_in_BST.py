def findClosestValueInBst(tree, target):
    # Write your code here.
    
	current_node = tree
	closest = float("inf")
	
	while current_node is not None:
		if abs(target - closest) > abs(current_node.value - target):
			closest = current_node.value
		elif target < current_node.value:
			current_node = current_node.left
		else: #target > current_node.value:
			current_node = current_node.right
	return closest

#avg O(logn) worst O(n) time