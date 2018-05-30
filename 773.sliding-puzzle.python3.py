#
# [787] Sliding Puzzle
#
# https://leetcode.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (47.26%)
# Total Accepted:    3.4K
# Total Submissions: 7.3K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
#
# A move consists of choosing 0 and a 4-directionally adjacent number and
# swapping it.
#
# The state of the board is solved if and only if the board is
# [[1,2,3],[4,5,0]].
#
# Given a puzzle board, return the least number of moves required so that the
# state of the board is solved. If it is impossible for the state of the board
# to be solved, return -1.
#
# Examples:
#
#
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
#
#
#
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
#
#
#
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
#
#
#
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
#
#
# Note:
#
#
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
#
#
from collections import deque


class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        def swap_tuple(tup, gap, dest):
            tmp = list(tup)
            tmp[gap], tmp[dest] = tmp[dest], tmp[gap]
            return tuple(tmp)

        switches = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (3, 1, 5), 5: (4, 2)}
        initial_state = tuple(board[0] + board[1])
        visited = {initial_state}
        if initial_state == (1, 2, 3, 4, 5, 0):
            return 0
        q = deque([(initial_state.index(0), initial_state, 0)])
        while q:
            gap, state, dist = q.popleft()
            next_states = [(x, swap_tuple(state, gap, x)) for x in switches[gap]]
            for next_gap, next_state in next_states:
                if next_state not in visited:
                    if next_state == (1, 2, 3, 4, 5, 0):
                        return dist + 1
                    visited.add(next_state)
                    q.append((next_gap, next_state, dist + 1))
        return -1
