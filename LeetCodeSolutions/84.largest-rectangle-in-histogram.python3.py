#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (27.79%)
# Total Accepted:    119.6K
# Total Submissions: 430.4K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
#
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
#
#
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#
#
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # =====================================================================
        # Trying O(n) solution;
        # https://www.youtube.com/watch?v=VNbkzsnllsU&t=1s
        # =====================================================================
        n = len(heights)
        st = []
        ans = 0
        for idx, h in enumerate(heights):
            pos = idx
            while st and st[-1][0] > h:
                val, pos = st.pop()
                ans = max(ans, (idx-pos)*val)
            st.append((h, pos))
        while st:
            val, pos = st.pop()
            ans = max(ans, (n-pos)*val)
        return ans

        # =====================================================================
        # Trivial O(n^2) solution; Obviously times out
        # =====================================================================

        # n = len(heights)
        # ans = 0
        # for i in range(n):
        #     mh = heights[i]
        #     for j in range(i, n):
        #         mh = min(mh, heights[j])
        #         ans = max(ans, (j-i+1)*mh)
        # return ans
