#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (46.24%)
# Total Accepted:    55.8K
# Total Submissions: 120.7K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
#
# Example 1:
#
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# Example 2:
#
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#
#
import re
class Solution:
    def apply_op(self, x1, x2, op):
        ans = 0
        if op=='+':
            ans = x1 + x2
        elif op=='*':
            ans = x1 * x2
        elif op=='-':
            ans = x1 - x2
        return ans

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        ans = []
        for i in range(len(input)):
            if input[i] in '+-*':
                p1 = self.diffWaysToCompute(input[:i])
                p2 = self.diffWaysToCompute(input[i+1:])
                for l in p1:
                    for r in p2:
                        ans.append(self.apply_op(l, r, input[i]))
        return ans
