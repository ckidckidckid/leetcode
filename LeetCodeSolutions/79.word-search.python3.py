#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (28.23%)
# Total Accepted:    178.8K
# Total Submissions: 633.2K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
# Example:
#
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
#
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(word, i, j):

            ans = False
            if len(word) == 0:
                ans = True
            elif board[i][j] != word[0]:
                ans = False
            else:
                neighbors = []
                visited[i][j] = True
                if i!=0 and not visited[i-1][j]:
                    neighbors.append([i-1, j])
                if j!=0 and not visited[i][j-1]:
                    neighbors.append([i, j-1])
                if i<(len(board)-1) and not visited[i+1][j]:
                    neighbors.append([i+1, j])
                if j<(len(board[0])-1) and not visited[i][j+1]:
                    neighbors.append([i, j+1])
                # print(i,j,'==>',neighbors)
                ans = len(neighbors) == 0 and len(word) == 1
                for n in neighbors:
                    ans = ans or dfs(word[1:], n[0], n[1])
                    if ans:
                        break
                visited[i][j] = False
            # print(word,i,j, ans)
            return ans

        if not any(board) or not any(word):
            return False
        ans = False
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i,row in enumerate(board):
            for j,c in enumerate(row):
                    ans = ans or dfs(word, i, j)
                    if ans:
                        break
        return ans
