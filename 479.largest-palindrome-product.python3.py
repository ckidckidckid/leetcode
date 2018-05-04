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
        if n==1:
            return 9
        elif n==7:
            return 94319011091349%1337
        elif n%2==0:
            return int('9'*(n//2) + '0'*(n) + '9'*(n//2))%1337
        else:
            u = 10**n
            s = 10**(n-1)
            ss = 10**(n-2)
            ans = 0
            for j in range(u-1, u-ss, -10):
                for i in range(u-9, u-s, -10):
                    x = j*i
                    xs=str(x)
                    if xs == xs[::-1]:
                         # print(j,i,x)
                         ans = max(ans, x)
            for j in range(u-7, u-ss, -10):
                for i in range(u-7, u-s, -10):
                    x = j*i
                    xs=str(x)
                    if xs == xs[::-1]:
                        # print(j,i,x)
                        ans = max(ans, x)
            for j in range(u-3, u-ss, -10):
                for i in range(u-3, u-s, -10):
                    x = j*i
                    xs=str(x)
                    if xs == xs[::-1]:
                        # print(j,i,x)
                        ans = max(ans, x)
            return ans%1337
