#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (36.82%)
# Total Accepted:    178.9K
# Total Submissions: 485.2K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
#
#
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(x,y):
            grid[x][y] = 'x'
            if x>0 and grid[x-1][y] == '1':
                dfs(x-1, y)
            if y>0 and grid[x][y-1] == '1':
                dfs(x,y-1)
            if x<m-1 and grid[x+1][y] == '1':
                dfs(x+1,y)
            if y<n-1 and grid[x][y+1] == '1':
                dfs(x,y+1)

        if not any(grid):
            return 0
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i,j)
        return ans
