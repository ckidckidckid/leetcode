#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (51.31%)
# Total Accepted:    7.7K
# Total Submissions: 15K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to
# make two strings equal.
#
# Example 1:
#
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
#
#
#
# Example 2:
#
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e]
# to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
#
#
#
# Note:
# 0 < s1.length, s2.length .
# All elements of each string will have an ASCII value in [97, 122].
#
#
class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1,l2 = len(s1),len(s2)
        table = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i==0 and j==0:
                    continue
                elif i==0:
                    table[i][j] = table[i][j-1] + ord(s2[j-1])
                elif j==0:
                    table[i][j] = table[i-1][j] + ord(s1[i-1])
                else:
                    if s1[i-1] == s2[j-1]:
                        table[i][j] = table[i-1][j-1]
                    else:
                        table[i][j] = min(
                            table[i-1][j] + ord(s1[i-1]),
                            table[i][j-1] + ord(s2[j-1]),
                            table[i-1][j-1] + ord(s1[i-1]) + ord(s2[j-1])
                        )
        return table[l1][l2]
