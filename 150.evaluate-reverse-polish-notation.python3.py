# coding: utf-8

#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (28.55%)
# Total Accepted:    115.3K
# Total Submissions: 404K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
#
# Note:
#
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
#
#
# Example 1:
#
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
#
# Example 2:
#
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
#
# Example 3:
#
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def apply_op(o1, o2, op):
            if op == '+':
                return o1+o2
            if op == '-':
                return o1-o2
            if op == '*':
                return o1*o2
            if op == '/':
                ans=1
                if o1<0:
                    ans=-1
                    o1=-o1
                if o2<0:
                    ans*=-1
                    o2=-o2
                return ans * (o1//o2)

        st = []
        for x in tokens:
            if x in {'+', '-', '*', '/'}:
                op2 = st.pop()
                op1 = st.pop()
                res = apply_op(op1, op2, x)
                st.append(res)
            else:
                st.append(int(x))
        return st.pop()
