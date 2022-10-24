#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (42.49%)
# Total Accepted:    18.4K
# Total Submissions: 43.3K
# Testcase Example:  '"ABAB"\n2'
#
# Given a string that consists of only uppercase English letters, you can
# replace any letter in the string with another letter at most k times. Find
# the length of a longest substring containing all repeating letters you can
# get after performing the above operations.
#
# Note:
# Both the string's length and k will not exceed 104.
#
#
#
# Example 1:
#
# Input:
# s = "ABAB", k = 2
#
# Output:
# 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
#
#
#
#
# Example 2:
#
# Input:
# s = "AABABBA", k = 1
#
# Output:
# 4
#
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#
#
#
class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        table = {}
        result = max_c  = i = 0
        for j in range(len(s)):
            table[s[j]] = table.get(s[j], 0) + 1
            max_c = max(max_c, table[s[j]])
            if j-i+1-max_c > k:
                table[s[i]] -= 1
                i+=1
            result = max(result, j-i+1)
        return result
