#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (38.39%)
# Total Accepted:    146.5K
# Total Submissions: 381.1K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
#
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        c = [1 for _ in range(rowIndex+1)]
        ci = 1
        while ci < rowIndex:
            ci+=1
            o = 1
            for i in range(1,ci):
                t = c[i]
                c[i] = o + c[i]
                o = t
        return c
