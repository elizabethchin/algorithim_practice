# LeetCode 516
# Given a string s, find the longest palindromic subsequence’s length in s. You may assume that the maximum length of s is 1000

# class Solution
#     def longestPalindromeSubseq(self, s: str) -> int:
#         return self.longestPalindromeSubseq_recursive(s, 0, len(s) -1)

#     #"pointer" from left has passed right
#     def longestPalindromeSubseq_recursive(self, s, start, end):
#         if start > end:
#             return 0

#         #every sequence with one element is a palindrome of length 1
#         if start == end:
#             return 1

#         # case 1: elements at the beginning and the end are the same
#         if s[start] == s[end]:
#             return 2 + self.longestPalindromeSubseq_recursive(s, start + 1, end - 1)

#         #case 2: skip one element either from the beginning or the end
#         subseq1 = self.longestPalindromeSubseq_recursive(s, start + 1, end)
#         subseq2 = self.longestPalindromeSubseq_recursive(s, start, end - 1)

#     return max(subseq1, subseq2)

# O(2^n) time bc making 2 recursive calls in the same function
# O(n) space bc recursion stack

#use memoization to store subsequences
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo =[[-1 for _ n in range(len(s))] for _ in range(len(s))]
