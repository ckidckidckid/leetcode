#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (33.45%)
# Total Accepted:    76.1K
# Total Submissions: 227.4K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
#
# Note:  
#
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
#
#
#
from bisect import insort
from collections import deque
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # ======================================================================
        # Trying faster solution; O(nlog(n)) solution
        # ======================================================================

        seen = {1}
        ugly = deque([1])
        count = 0
        while True:
            num = ugly.popleft()
            count += 1
            if count == n:
                return num
            for val in (num*2, num*3, num*5):
                if val not in seen:
                    seen.add(val)
                    insort(ugly, val)

        # ======================================================================
        # O(n^2) solution; Times out
        # ======================================================================
        # def is_ugly(num):
        #     while num%5 == 0: num //=5
        #     while num%3 == 0: num //=3
        #     while num%2 == 0: num //=2
        #     return num==1
        #
        # num = 1
        # count = 1
        # while True:
        #     if count == n:
        #         return num
        #     num+=1
        #     if is_ugly(num):
        #         count+=1
