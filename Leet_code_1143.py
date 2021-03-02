#brute force

# class Solution:
#     def lcs(self, text1: str, text2: str) -> int:
#         return self.lcs_recursive(text1, text2, 0, 0)

#     def lcs_recursive(self, text1, text2. i, j):
#         if i == len(text1) or j == len(text2):
#             return 0
#         if text1[i] == text2[j]:
#             return 1 + self.lcs_recursive(text1, text2, i + 1, j+ 1)

#         return max(self.lcs_recursive(text1, text2, i + 1, j),
#                 self.lcs_recursive(text1, text2, i, j + 1))

# top-down dynamic programming with memoization

# class Solution:
#     def lcs(self, text1: str, text2: str) -> int:
#         memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
#         return self.lcs_recursive(memo, text1, text2, 0, 0)

#     def lcs_recursive(self, memo, text1, text2, i, j):
#         if i == len(text1) or j == len(text2):
#             return 0
#         if memo[i][j] == -1:
#             if text1[i] == text2[j]:
#                 memo[i][j] = 1 + self.lcs_recursive(memo, text1, text2, i + 1, j + 1)
#             else:
#                 memo[i][j] = max(self.lcs_recursive(memo, text1, text2, i + 1, j), 
#                             self.lcs_recursive(memo, text1, text2, i, j + 1))
#         return memo[i][j]

#bottom-up dynamic programming with tabulation
# memo = []
# if text1[i] == text2[j]:
#     memo[i][j] = 1 + memo[i - 1][j - 1]
# else:
#     memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

class Solution:
    def lcs(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        max_length = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

            max_length = max(max_length, memo[i][j])
        return max_length



