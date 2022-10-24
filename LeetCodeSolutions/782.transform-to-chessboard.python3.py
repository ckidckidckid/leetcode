#
# [798] Transform to Chessboard
#
# https://leetcode.com/problems/transform-to-chessboard/description/
#
# algorithms
# Hard (37.16%)
# Total Accepted:    1.5K
# Total Submissions: 4K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]'
#
# An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows
# with each other, or any 2 columns with each other.
#
# What is the minimum number of moves to transform the board into a
# "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If
# the task is impossible, return -1.
#
#
# Examples:
# Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# Output: 2
# Explanation:
# One potential sequence of moves is shown below, from left to right:
#
# 0110     1010     1010
# 0110 --> 1010 --> 0101
# 1001     0101     1010
# 1001     0101     0101
#
# The first move swaps the first and second column.
# The second move swaps the second and third row.
#
#
# Input: board = [[0, 1], [1, 0]]
# Output: 0
# Explanation:
# Also note that the board with 0 in the top left corner,
# 01
# 10
#
# is also a valid chessboard.
#
# Input: board = [[1, 0], [1, 0]]
# Output: -1
# Explanation:
# No matter what sequence of moves you make, you cannot end with a valid
# chessboard.
#
#
# Note:
#
#
# board will have the same number of rows and columns, a number in the range
# [2, 30].
# board[i][j] will be only 0s or 1s.
#
#
#
class Solution:
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # O(n^2) solutions; Idea from https://leetcode.com/problems/transform-to-chessboard/discuss/132113/Java-Clear-Code-with-Detailed-Explanations
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        n = len(board)
        if n == 0:
            return 0
        m = len(board[0])
        if n != m:
            return -1
        else:
            m = n
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[0][j] ^ board[i][j] ^ board[i][0] == 1:
                    return -1
        rowOneCount = colOneCount = rowToMove = colToMove = 0
        for i in range(n):
            if board[0][i] == 1:
                rowOneCount += 1
            if board[i][0] == 1:
                colOneCount += 1
            if board[0][i] == i%2:
                colToMove += 1
            if board[i][0] == i%2:
                rowToMove += 1
        if not (n//2 <= rowOneCount <= (n+1)//2) or not (n//2 <= colOneCount <= (n+1)//2):
            return -1
        if n%2 == 0:
            rowToMove = min(rowToMove, n - rowToMove)
            colToMove = min(colToMove, n - colToMove)
        else:
            if rowToMove % 2 == 1:
                rowToMove = n - rowToMove
            if colToMove % 2 == 1:
                colToMove = n - colToMove
        return (rowToMove + colToMove)//2
