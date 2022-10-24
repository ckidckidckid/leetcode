#
# [796] Reaching Points
#
# https://leetcode.com/problems/reaching-points/description/
#
# algorithms
# Hard (23.40%)
# Total Accepted:    3.1K
# Total Submissions: 13.2K
# Testcase Example:  '9\n5\n12\n8'
#
# A move consists of taking a point (x, y) and transforming it to either (x,
# x+y) or (x+y, y).
#
# Given a starting point (sx, sy) and a target point (tx, ty), return True if
# and only if a sequence of moves exists to transform the point (sx, sy) to
# (tx, ty). Otherwise, return False.
#
#
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
#
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True
#
#
#
# Note:
#
#
# sx, sy, tx, ty will all be integers in the range [1, 10^9].
#
#
class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Solution using modulus
        # https://leetcode.com/problems/reaching-points/discuss/114856/Easy-and-Concise-2-line-SolutionPythonC++Java
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        while tx > sx and ty > sy:
            tx, ty = tx%ty, ty%tx
        return (sx == tx and (ty-sy)%sx == 0) or (sy == ty and (tx-sx)%sy == 0)

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Recursive Solution O(tx*tx); Reaches Max recursion Depth
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # def helper(x, y):
        #     k = (x,y)
        #     if k in cache:
        #         return cache[k]
        #     if x==tx and y==ty:
        #         ans = True
        #     elif x > tx or y > ty:
        #         ans = False
        #     else:
        #         ans = helper(x+y, y) or helper(x, y+x)
        #     cache[k] = ans
        #     return ans
        # cache = {}
        # return helper(sx, sy)
