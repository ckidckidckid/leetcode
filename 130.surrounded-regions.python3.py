#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (19.78%)
# Total Accepted:    102.6K
# Total Submissions: 518.5K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
#
#
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def neigbors(i,j, m, n):
            res = []
            if i>0:
                res.append((i-1,j))
            if i<m-1:
                res.append((i+1,j))
            if j>0:
                res.append((i,j-1))
            if j<n-1:
                res.append((i,j+1))
            return res


        def dfs(i,j, m, n, visited):
            visited[i][j] = 1
            board[i][j] = '-'
            for i_n,j_n in neigbors(i,j,m,n):
                if visited[i_n][j_n] == 0 and board[i_n][j_n] == 'O':
                    dfs(i_n,j_n,m,n,visited)

        m = len(board)
        if m==0:
            return
        n = len(board[0])
        if n==0:
            return
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j,m,n,visited)
            if board[m-1][j] == 'O':
                dfs(m-1,j,m,n,visited)

        for i in range(1,m-1):
            if board[i][0] == 'O':
                dfs(i,0,m,n,visited)
            if board[i][n-1] == 'O':
                dfs(i,n-1,m,n,visited)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'
