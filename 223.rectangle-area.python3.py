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
        a1 = abs(C-A) * abs(D-B)
        a2 = abs(G-E) * abs(H-F)
        a3 = 0
        if ((A <= E <= C) or (E < A < G)) and ((B <= F <= D) or (F <= B <= H)):
            left = min(A,E)
            right = max(C,G)
            bottom = min(B,F)
            top = max(D,H)

            a3 = abs((right-left)-(C-A)-(G-E)) * abs((top-bottom)-(D-B)-(H-F))

        return a1+a2-a3
