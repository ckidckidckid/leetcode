#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (37.26%)
# Total Accepted:    68.3K
# Total Submissions: 183.2K
# Testcase Example:  '[[]]'
#
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
#
#
#
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
#
#
#
#
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
#
#
#
#
# Write a function to compute the next state (after one update) of the board
# given its current state.
#
#
# Follow up:
#
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        m = len(board)
        n = len(board[0])

        # In place modification by keeping track of only top row and left value

        top_row = [0 for _ in range(n)]
        for i in range(m):
            left_val = 0
            temp = board[i][:]
            for j in range(n):
                temp_left = board[i][j]

                left_pop = left_val
                right_pop = (board[i][j+1] if j<n-1 else 0)
                top_pop = sum(top_row[max(0, j-1):min(n, j+2)])
                bottom_pop = sum(board[i+1][max(0, j-1):min(n, j+2)]) if i<m-1 else 0

                neighbor_pop = left_pop + right_pop + top_pop + bottom_pop

                if board[i][j] == 0:
                    if neighbor_pop == 3:
                        board[i][j] = 1
                else:
                    if not 2 <= neighbor_pop <= 3:
                        board[i][j] = 0
                left_val = temp_left
            top_row = temp

# Interesting approach to solve inplace by saving the information in two least significant bits discussion at
# https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
# KEEP IN MIND THAT INT CAN HOLD 64 bit of INFO

# Discussions on follow ups
# https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution
# https://leetcode.com/problems/game-of-life/discuss/73241/What-does-the-follow-up-mean-by-%22encroaches-the-border-of-the-array%22

# For 2nd folow up, we cannot compute `m` and `n` and the board will be represented as set of live co-ordinates i.e
# live = {(0,0), {1,1}, ..}
