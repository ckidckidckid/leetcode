#
# [306] Additive Number
#
# https://leetcode.com/problems/additive-number/description/
#
# algorithms
# Medium (27.81%)
# Total Accepted:    32.8K
# Total Submissions: 117.7K
# Testcase Example:  '"112358"'
#
# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for
# the first two numbers, each subsequent number in the sequence must be the sum
# of the preceding two.
#
# Given a string containing only digits '0'-'9', write a function to determine
# if it's an additive number.
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence
# 1, 2, 03 or 1, 02, 3 is invalid.
#
# Example 1:
#
#
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5,
# 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#
#
# Example 2:
#
#
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199
#
# Follow up:
# How would you handle overflow for very large input integers?
#
class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def helper(n1, n2, s, valid):
            if n1 is not None and n2 is not None and s == '':
                return valid
            ans = False
            for i in range(len(s)):
                tn = int(s[:i+1])
                if tn > 0 and s[0] == '0':
                    break
                if n1 is None and n2 is None:
                    ans = ans or helper(None, tn, s[i+1:], False)
                    if ans:
                        break
                elif n1 is None and n2 is not None:
                    ans = ans or helper(n2, tn, s[i+1:], False)
                    if ans:
                        break
                else:
                    ans = ans or (n1 + n2 == tn and helper(n2, tn, s[i+1:], True))
                    if ans:
                        break
            return ans

        return helper(None, None, num, False)
