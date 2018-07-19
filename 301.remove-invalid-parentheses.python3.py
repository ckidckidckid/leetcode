#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (36.12%)
# Total Accepted:    75K
# Total Submissions: 207.7K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and
# ).
#
# Example 1:
#
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
#
#
# Example 2:
#
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
#
#
# Example 3:
#
#
# Input: ")("
# Output: [""]
#
#
#
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Very simple solution from
        # https://leetcode.com/problems/remove-invalid-parentheses/discuss/75032/Share-my-Java-BFS-solution
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        def isValid(ss):
            cnt = 0
            for c in ss:
                if c=='(':cnt+=1
                if c==')':cnt-=1
                if cnt<0:
                    return False
            return cnt==0

        q = deque([s])
        visited = {s}
        ans = []
        found = False

        while q:
            ss = q.popleft()
            if isValid(ss):
                ans.append(ss)
                found = True
            if not found:
                for i in range(len(ss)):
                    if ss[i] not in {'(', ')'}:
                        continue
                    ns = ss[:i] + ss[i+1:]
                    if ns not in visited:
                        visited.add(ns)
                        q.append(ns)
        return ans
