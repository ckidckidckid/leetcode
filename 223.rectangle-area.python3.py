#
# [223] Rectangle Area
#
# https://leetcode.com/problems/rectangle-area/description/
#
# algorithms
# Medium (33.86%)
# Total Accepted:    71.8K
# Total Submissions: 212K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as
# shown in the figure.
#
#
#
# Example:
#
#
# Input: -3, 0, 3, 4, 0, -1, 9, 2
# Output: 45
#
#
# Note:
# Assume that the total area is never beyond the maximum possible value of int.
#
#
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        a1 = (C-A) * (D-B)
        a2 = (G-E) * (H-F)

        left = max(A,E)
        right = min(C,G)
        bottom = max(B,F)
        top = min(D,H)

        a3 = (right-left) * (top-bottom) if (right>left and top>bottom) else 0

        return a1+a2-a3
