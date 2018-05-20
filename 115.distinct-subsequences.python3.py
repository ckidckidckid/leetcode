#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (32.20%)
# Total Accepted:    83.7K
# Total Submissions: 259.9K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
# Example 2:
#
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
#
#
#
class Solution:

    # =====================================================
    # Iterative DP (bottom up) solution; Accepted; beats 81% :)
    # =====================================================
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        table = [[0]*(m+1) for _ in range(n)]
        table.append([1]*(m+1))
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                table[i][j] = table[i][j+1]
                if t[i] == s[j]:
                    table[i][j] += table[i+1][j+1]
        return table[0][0]


    # =====================================================
    # Recursive solution (top down) with memoization. times out :(
    # =====================================================
    # def numDistinct(self, s, t, table = {}):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: int
    #     """
    #     ans = 0
    #     key = (s,t)
    #     if key in table:
    #         return table[key]
    #     if s==t or len(t)==0:
    #         ans = 1
    #     elif len(s) < len(t):
    #         ans = 0
    #     else:
    #         ans += self.numDistinct(s[1:], t)
    #         if s[0] == t[0]:
    #             ans += self.numDistinct(s[1:], t[1:])
    #     table[key] = ans
    #     return ans
