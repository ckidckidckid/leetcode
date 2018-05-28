#
# [810] Valid Tic-Tac-Toe State
#
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/
#
# algorithms
# Medium (27.55%)
# Total Accepted:    3.9K
# Total Submissions: 14.1K
# Testcase Example:  '["O  ","   ","   "]'
#
# A Tic-Tac-Toe board is given as a string array board. Return True if and only
# if it is possible to reach this board position during the course of a valid
# tic-tac-toe game.
#
# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".
# The " " character represents an empty square.
#
# Here are the rules of Tic-Tac-Toe:
#
#
# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always
# places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled
# ones.
# The game ends when there are 3 of the same (non-empty) character filling any
# row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
#
#
#
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
#
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
#
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
#
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
#
#
# Note:
#
#
# board is a length-3 array of strings, where each string board[i] has length
# 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.
#
#
class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def check_win(c):
            if board[0][0] == c and board[0][1] == c and board[0][2] == c:
                return True
            elif board[1][0] == c and board[1][1] == c and board[1][2] == c:
                return True
            elif board[2][0] == c and board[2][1] == c and board[2][2] == c:
                return True
            elif board[0][0] == c and board[1][0] == c and board[2][0] == c:
                return True
            elif board[0][1] == c and board[1][1] == c and board[2][1] == c:
                return True
            elif board[0][2] == c and board[1][2] == c and board[2][2] == c:
                return True
            elif board[0][0] == c and board[1][1] == c and board[2][2] == c:
                return True
            elif board[0][2] == c and board[1][1] == c and board[2][0] == c:
                return True
            else:
                return False

        x_cnt = sum([row.count('X') for row in board])
        o_cnt = sum([row.count('O') for row in board])
        if not 0 <= x_cnt - o_cnt <= 1:
            return False
        x_win = check_win('X')
        o_win = check_win('O')
        if x_win and o_win:
            return False
        if x_win:
            return x_cnt == o_cnt + 1
        elif o_win:
            return x_cnt == o_cnt
        return True
