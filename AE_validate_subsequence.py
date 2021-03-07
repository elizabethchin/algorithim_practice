"""
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers[1,3,4] for a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single nuymber in ana array and the array inself are both valid subsequences of the array.

example:

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
> true

"""

def isValidSubsequence(array, sequence):
    # Write your code here.
	
	arrIdx = 0
	seqIdx = 0
	
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
	
		arrIdx += 1
	
	return seqIdx == len(sequence)

def isValidSubsequence(array, sequence):
    # Write your code here.
    
	i = 0
	
	for num in array:
		if i == len(sequence):
			return True
		if num == sequence[i]:
			i += 1
	return i == len(sequence)