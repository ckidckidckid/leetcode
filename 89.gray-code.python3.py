#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (42.58%)
# Total Accepted:    107.4K
# Total Submissions: 252.3K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
#
# Note:
# For a given n, a gray code sequence is not uniquely defined.
#
# For example, [0,2,3,1] is also a valid gray code sequence according to the
# above definition.
#
# For now, the judge is able to judge based on one instance of gray code
# sequence. Sorry about that.
#
#
import math
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        other = lambda x : '1' if x=='0' else '0'

        change_bit = [0]
        max_bit = 1
        while int(math.log(len(change_bit)+1, 2)) < n:
            change_bit.extend([max_bit] + change_bit)
            max_bit+=1
        ans = ['{:032b}'.format(0)]
        for c in change_bit:
            prev = ans[-1]
            ans.append(prev[:31-c] + other(prev[31-c]) + prev[32-c:])
        return [int(x,2) for x in ans]
