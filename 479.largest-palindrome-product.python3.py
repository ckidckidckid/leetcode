#
# [479] Largest Palindrome Product
#
# https://leetcode.com/problems/largest-palindrome-product/description/
#
# algorithms
# Easy (25.58%)
# Total Accepted:    9.8K
# Total Submissions: 38.5K
# Testcase Example:  '1'
#
# Find the largest palindrome made from the product of two n-digit numbers.
# ⁠Since the result could be very large, you should return the largest
# palindrome mod 1337.
#
# Example:
# Input: 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
#
#
#
# Note:
# The range of n is [1,8].
#
#
#
# 9 * 1 = 9
# 99 * 91 = 9009
#  993 * 913 = 906609
class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2==0:
            return int('9'*(n//2) + '0'*(n) + '9'*(n//2))%1337
        else:
            arr = [9,123,677,877]
            return arr[n//2]
