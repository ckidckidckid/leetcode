#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.09%)
# Total Accepted:    35.5K
# Total Submissions: 118K
# Testcase Example:  '3'
#
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 231).
#
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
#
#
#
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
#
#
#
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # =====================================================================
        # Trying Faster Solution
        # https://leetcode.com/problems/nth-digit/discuss/88369/0ms-C++-Solution-with-Detail-Explanation
        # =====================================================================
        digits = 1
        base = 9
        while n > base*digits:
            n -= base*digits
            digits += 1
            base *= 10

        idx = n%digits
        if idx == 0:
            idx = digits
        num = 1
        for i in range(1, digits):
            num *= 10
        num += (n//digits) -1 if idx == digits else (n//digits)

        for i in range(idx, digits):
            num //=10
        return num%10

        # =====================================================================
        # Times out; O(n) solution
        # =====================================================================
        # s = '0'
        # i = 1
        # while len(s) < n+1:
        #     s += str(i)
        #     i+=1
        # return int(s[n])
