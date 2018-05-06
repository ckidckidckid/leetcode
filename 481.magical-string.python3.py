#
# [481] Magical String
#
# https://leetcode.com/problems/magical-string/description/
#
# algorithms
# Medium (45.81%)
# Total Accepted:    13.8K
# Total Submissions: 30.2K
# Testcase Example:  '1'
#
#
# A magical string S consists of only '1' and '2' and obeys the following
# rules:
#
#
# The string S is magical because concatenating the number of contiguous
# occurrences of characters '1' and '2' generates the string S itself.
#
#
#
# The first few elements of string S is the following:
# S = "1221121221221121122……"
#
#
#
# If we group the consecutive '1's and '2's in S, it will be:
#
#
# 1   22  11  2  1  22  1  22  11  2  11  22 ......
#
#
# and the occurrences of '1's or '2's in each group are:
#
#
# 1   2       2    1   1    2     1    2     2    1    2    2 ......
#
#
#
# You can see that the occurrence sequence above is the S itself.
#
#
#
# Given an integer N as input, return the number of '1's in the first N number
# in the magical string S.
#
#
# Note:
# N will not exceed 100,000.
#
#
#
# Example 1:
#
# Input: 6
# Output: 3
# Explanation: The first 6 elements of magical string S is "12211" and it
# contains three 1's, so return 3.
#
#
#
class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        def other(x):
            if x==1:
                return 2
            else:
                return 1

        if n == 0:
            return 0
        if n == 1:
            return 1
        s = [-1 for _ in range(n)]
        s[0] = 1
        count = 1
        rc = 1
        ptr = 0
        for i in range(1,n):
            if s[ptr] == rc:
                s[i] = other(s[i-1])
                ptr += 1
                rc = 1
            else:
                s[i] = s[i-1]
                rc += 1
        return s.count(1)
