#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (46.54%)
# Total Accepted:    57.5K
# Total Submissions: 123.5K
# Testcase Example:  '2'
#
#
# Given a positive integer n, break it into the sum of at least two positive
# integers and maximize the product of those integers. Return the maximum
# product you can get.
#
#
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 =
# 3 + 3 + 4).
#
#
#
# Note: You may assume that n is not less than 2 and not larger than 58.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Using Solution 2 from
        # https://www.programcreek.com/2015/04/leetcode-integer-break-java/
        if n < 4:
            table = [0,0,1,2]
            return table[n]
        elif (n-4)%3 == 0:
            return (3**((n-4)//3))*4
        else:
            fac = n//3
            rem = n%3
            return (3**(fac))*(rem if rem != 0 else 1)
