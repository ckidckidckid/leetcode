#
# [688] Knight Probability in Chessboard
#
# https://leetcode.com/problems/knight-probability-in-chessboard/description/
#
# algorithms
# Medium (40.25%)
# Total Accepted:    7.7K
# Total Submissions: 19K
# Testcase Example:  '3\n2\n0\n0'
#
#
# On an NxN chessboard, a knight starts at the r-th row and c-th column and
# attempts to make exactly K moves.  The rows and columns are 0 indexed, so the
# top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
#
#
#
# A chess knight has 8 possible moves it can make, as illustrated below.  Each
# move is two squares in a cardinal direction, then one square in an orthogonal
# direction.
#
#
#
#
#
# Each time the knight is to move, it chooses one of eight possible moves
# uniformly at random (even if the piece would go off the chessboard) and moves
# there.
#
#
#
# The knight continues moving until it has made exactly K moves or has moved
# off the chessboard.  Return the probability that the knight remains on the
# board after it has stopped moving.
#
#
# Example:
#
# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight
# on the board.
# From each of those positions, there are also two moves that will keep the
# knight on the board.
# The total probability the knight stays on the board is 0.0625.
#
#
#
# Note:
# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.
#
#
class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        def helper(x,y,moves):
            ans = 0
            key = (x,y,moves)
            if key in cache:
                return cache[key]
            if moves>=K:
                ans = 1
            else:
                for nx,ny in [(x+2,y+1), (x+2,y-1), (x+1,y-2), (x-1,y-2), (x-2,y-1), (x-2,y+1), (x-1, y+2), (x+1, y+2)]:
                    if nx>=0 and nx<N and ny>=0 and ny<N:
                        ans += 0.125 * helper(nx,ny,moves+1)
            cache[key] = ans
            return ans

        cache = {}
        if not (r>=0 and r<N and c>=0 and c<N):
            ans = 0
        else:
            ans = helper(r,c,0)
        return ans


        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Without Memoization; Times out
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # def helper(x,y,moves):
        #     if moves>=K:
        #         return
        #     else:
        #         for nx,ny in [(x+2,y+1), (x+2,y-1), (x+1,y-2), (x-1,y-2), (x-2,y-1), (x-2,y+1), (x-1, y+2), (x+1, y+2)]:
        #             if nx>=0 and nx<N and ny>=0 and ny<N:
        #                 helper(nx,ny,moves+1)
        #             else:
        #                 ans[0] -= (1/8**(moves+1))
        #
        # ans = [1]
        # cache = {}
        # if not (r>=0 and r<N and c>=0 and c<N):
        #     ans[0] = 0
        # else:
        #     helper(r,c,0)
        # return ans[0]
