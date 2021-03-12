"""
Generate Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

ex1:
input: nums = [1,2,3]
output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

ex2:
input: nums = [0,1]
output: [[0,1], [1,0]]
"""

# def gen_permutations(nums):


#Problem 2

def max_subset_sum_no_adjacent(array):

    memo = []
    i = 0
    for num in array:
        while i < len(array):
        sum_non_adjacent = num + array[i + 2]
        memo.append(sum_non_adjacent)
        i += 1
    return max(memo)


