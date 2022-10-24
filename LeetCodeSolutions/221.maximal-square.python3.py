#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (30.45%)
# Total Accepted:    88.2K
# Total Submissions: 289.6K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#
#
#
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not any(matrix):
            return 0
        m,n = len(matrix), len(matrix[0])
        size = [[0 for _ in range(n)] for _ in range(m)]
        ans = -1
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    size[i][j] = int(matrix[i][j])
                else:
                    if int(matrix[i][j]) == 1:
                        size[i][j] = min(size[i-1][j], size[i][j-1], size[i-1][j-1]) + 1
                    else:
                        size[i][j] = 0
                ans = max(ans, size[i][j]*size[i][j])
        return ans
