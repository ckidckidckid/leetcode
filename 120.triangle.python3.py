#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (35.18%)
# Total Accepted:    134.1K
# Total Submissions: 381.1K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#
from functools import lru_cache
class Solution:
    @lru_cache(maxsize = 10000)
    def rowmin(self, level, idx):
        if level >= self.n:
            return 0
        elif level == self.n-1:
            return self.triangle[level][idx]
        else:
            return self.triangle[level][idx] + min(
                self.rowmin(level+1, idx),self.rowmin(level+1, idx+1)
            )

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # ============================
        # Top down DP; original idea + accepted
        # ============================
        # self.triangle = triangle
        # self.n = len(triangle)
        # return self.rowmin(0,0)

        # ============================
        # Bottom up DP ; explained at
        # https://leetcode.com/problems/triangle/discuss/38730/DP-Solution-for-Triangle
        # ============================

        min_path = triangle[-1][:]
        n = len(triangle)
        for level in range(n-2,-1,-1):
            for idx in range(0, level+1):
                min_path[idx] = triangle[level][idx] + min(
                    min_path[idx],min_path[idx+1],
                )
        return min_path[0]
