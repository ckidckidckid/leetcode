#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (41.14%)
# Total Accepted:    151.1K
# Total Submissions: 367.3K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#
#
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i,row in enumerate(grid):
            for j,c in enumerate(grid[i]):
                if i==0 and j==0:
                    pass
                elif i==0:
                    grid[i][j] = grid[i][j-1] + c
                elif j==0:
                    grid[i][j] = grid[i-1][j] + c
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + c
        return grid[-1][-1]
