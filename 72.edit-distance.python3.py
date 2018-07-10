#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (33.23%)
# Total Accepted:    123.3K
# Total Submissions: 370K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Algorithm from http://asr.cs.cmu.edu/spring2014/lectures/class4.DP.pdf

        m = len(word1)
        n = len(word2)
        table = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    table[i][j] = max(i, j)
                else:
                    table[i][j] = min(
                        table[i-1][j] + 1,
                        table[i][j-1] + 1,
                        table[i-1][j-1] + (1 if word1[i-1] != word2[j-1] else 0),
                    )
        return table[-1][-1]
