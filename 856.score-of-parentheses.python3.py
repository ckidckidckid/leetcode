#
# [886] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (55.58%)
# Total Accepted:    3.7K
# Total Submissions: 6.6K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:
#
#
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
#
#
#
#
#
# Example 1:
#
#
# Input: "()"
# Output: 1
#
#
#
# Example 2:
#
#
# Input: "(())"
# Output: 2
#
#
#
# Example 3:
#
#
# Input: "()()"
# Output: 2
#
#
#
# Example 4:
#
#
# Input: "(()(()))"
# Output: 6
#
#
#
#
# Note:
#
#
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
#
#
#
#
#
#
class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
        #  Accepted, but not effecient
        #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

        # f,s,t = 0,1,2
        # S = list(S)
        # while len(S) > 1:
        #     if S[f] == '(' and S[s] == ')':
        #         S = S[:f]  + [1] + S[s+1:]
        #         f,s,t = 0,1,2
        #     elif type(S[f]) == int and type(S[s]) == int:
        #         S = S[:f]  + [S[f] + S[s]] + S[s+1:]
        #         f,s,t = 0,1,2
        #     elif S[f] == '(' and type(S[s]) == int and S[t] == ')':
        #         S = S[:f]  + [S[s]*2] + S[t+1:]
        #         f,s,t = 0,1,2
        #     else:
        #         f+=1
        #         s+=1
        #         t+=1
        # return S[0] if len(S) > 0 else 0

        #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
        # Props to approach 2 in
        # https://leetcode.com/problems/score-of-parentheses/discuss/141777/C++JavaPython-Concise-O(1)-Space
        # OR
        # https://leetcode.com/problems/score-of-parentheses/discuss/141848/C++-O(1)spaceO(n)time.
        #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
        layers = 0
        ans = 0
        for i in range(len(S)):
            if S[i] == '(':
                if S[i+1] == ')':
                    ans += 1<<layers
                layers+=1
            else:
                layers-=1
        return ans
