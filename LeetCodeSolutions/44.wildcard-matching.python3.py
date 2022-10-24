#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (21.11%)
# Total Accepted:    125.6K
# Total Submissions: 595.1K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
#
# Example 3:
#
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
#
#
# Example 4:
#
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
#
#
# Example 5:
#
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
#
#
#
class Solution:

    # =========================================================================
    # Trying O(sp) solution
    # Based on https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution
    # Not sure of complexity
    # =========================================================================
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n=len(s),len(p)
        i = j = 0
        s_to_match = star_pos_in_p = -1
        while i<m:
            if j<n and (p[j] == '?' or p[j] == s[i]):
                i+=1
                j+=1
            elif j<n and p[j] == '*':
                star_pos_in_p = j
                s_to_match = i
                j+=1
            elif star_pos_in_p >= 0:
                j = star_pos_in_p + 1
                i = s_to_match + 1
                s_to_match += 1
            else:
                return False
        while j<n and p[j] == '*':
            j += 1
        return j==n

    # =========================================================================
    # Correct, but times out ; O(sp^2)
    # =========================================================================
    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     j=0
    #     ans = None
    #     for i in range(len(p)):
    #         if p[i] == '*':
    #             flag = False
    #             for k in range(len(s),j-1,-1):
    #                 submatch = self.isMatch(s[k:], p[i+1:])
    #                 if submatch:
    #                     flag = ans = True
    #                     break
    #             if flag:
    #                 break
    #         if j==len(s):
    #             ans = False
    #             break
    #         elif p[i] == '?' or p[i] == s[j]:
    #             j+=1
    #         else:
    #             ans = False
    #             break
    #     if ans is None:
    #         ans = j==len(s)
    #     return ans
