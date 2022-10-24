#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (20.40%)
# Total Accepted:    172.8K
# Total Submissions: 846.6K
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
#
#
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=50000)
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        if not s or len(s) == 0:
            ans = 0
        elif len(s) == 1 and (0 < int(s) <= 9):
            ans = 1
        elif s[0] != '0':
            ans += (self.numDecodings(s[1:]) if 0 < int(s[:1]) <= 9 else 0)
            if (0 < int(s[:2]) <= 26):
                ans += (self.numDecodings(s[2:]) if len(s) > 2 else 1)
        return ans
