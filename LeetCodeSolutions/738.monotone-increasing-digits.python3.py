#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (40.97%)
# Total Accepted:    5.9K
# Total Submissions: 14.5K
# Testcase Example:  '10'
#
#
# Given a non-negative integer N, find the largest number that is less than or
# equal to N with monotone increasing digits.
#
# (Recall that an integer has monotone increasing digits if and only if each
# pair of adjacent digits x and y satisfy x .)
#
#
# Example 1:
#
# Input: N = 10
# Output: 9
#
#
#
# Example 2:
#
# Input: N = 1234
# Output: 1234
#
#
#
# Example 3:
#
# Input: N = 332
# Output: 299
#
#
#
# Note:
# N is an integer in the range [0, 10^9].
#
#
class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def fill(st, en):
            for i in range(st, en+1):
                rev[i]=9

        rev = [int(x) for x in str(N)[::-1]]
        i=0
        j=1
        while j<len(rev):
           if rev[j]<=rev[j-1]:
               j+=1
               continue
           else:
               while j<len(rev)-1 and rev[j]==rev[j+1]:
                   j+=1
               fill(i,j-1)
               rev[j]-=1
               i=j
               j+=1
        return int(''.join(str(x) for x in rev[::-1]))
