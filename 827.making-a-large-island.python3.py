class Solution:
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def fill(x, y, c):
            if x<0 or x>=m or y<0 or y>=n or grid[x][y] != 1:
                return 0
            ans = 1
            grid[x][y] = c
            ans += fill(x+1, y, c)
            ans += fill(x-1, y, c)
            ans += fill(x, y+1, c)
            ans += fill(x, y-1, c)
            return ans

        m = len(grid)
        n = len(grid[0])
        table = {0:0}
        c = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    table[c] = fill(i,j,c)
                    c+=1
        ans = -float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ta = 1
                    seen = set()
                    if i>0 and grid[i-1][j] not in seen:
                        ta += table[grid[i-1][j]]
                        seen.add(grid[i-1][j])
                    if i<m-1 and grid[i+1][j] not in seen:
                        ta += table[grid[i+1][j]]
                        seen.add(grid[i+1][j])
                    if j>0 and grid[i][j-1] not in seen:
                        ta += table[grid[i][j-1]]
                        seen.add(grid[i][j-1])
                    if j<n-1 and grid[i][j+1] not in seen:
                        ta += table[grid[i][j+1]]
                        seen.add(grid[i][j+1])
                    ans = max(ans, ta)

        return ans if ans != -float('inf') else m*n

        # Naive implementation O(m*n*m*n) solution
        # def find_size(g, x, y):
        #     if x<0 or x>=m or y<0 or y>=n or g[x][y] == 0:
        #         return 0
        #     ans = 1
        #     g[x][y] = 0
        #     ans += find_size(g, x+1, y)
        #     ans += find_size(g, x-1, y)
        #     ans += find_size(g, x, y+1)
        #     ans += find_size(g, x, y-1)
        #     return ans
        #
        # m = len(grid)
        # n = len(grid[0])
        # ans = -float('inf')
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 0:
        #             grid[i][j] = 1
        #             ans = max(ans, find_size([row[:] for row in grid], i, j))
        #             grid[i][j] = 0
        # return ans if ans != -float('inf') else m*n
