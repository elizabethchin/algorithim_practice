

def sortedSquaredArray(array):
    # Write your code here.
    squares = []
	
	for num in array:
		squares.append(num*num)
	return sorted(squares)

#this is the brute force approach O(nlogn) time | O(n) space

def sortedSquaredArray(array):
    # Write your code here.
    
	
	length = len(array)
	squares = [0] * length
	left_index = 0
	right_index = len(array) - 1
	
	for i in reversed(range(len(array))):
	
		if abs(array[left_index]) > abs(array[right_index]):
			squares[i] = (array[left_index])**2
			left_index += 1
		else: #don't use elif gives error
			# abs(array[left_index]) < abs(array[right_index])
			squares[i] = (array[right_index])**2
			right_index -= 1
	return squares

# optimal O(n) time and space