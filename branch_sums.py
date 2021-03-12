def branchSums(root):
    # Write your code here.
    sums = []
	calculateBranchSums(root, 0, sums)
	return sums

def calculateBranchSums(node, runningSum, sums):
	if node is None:
		return sums
	
	newRunningSum = runningSum + node.value
	
	calculateBranchSums(node.left, newRunningSum, sums)
	calculateBranchSums(node.right, newRunningSum, sums)
	
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return sums