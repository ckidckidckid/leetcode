#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.24%)
# Total Accepted:    136.7K
# Total Submissions: 424.1K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
#
#
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not any(obstacleGrid):
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        table = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                elif i==0 and j==0:
                    table[i][j] = 1
                elif i==0:
                    table[i][j] = table[i][j-1]
                elif j==0:
                    table[i][j] = table[i-1][j]
                else:
                    table[i][j] = table[i-1][j] + table[i][j-1]
        return table[-1][-1]
