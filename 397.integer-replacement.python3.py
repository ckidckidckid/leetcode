#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (30.51%)
# Total Accepted:    29.3K
# Total Submissions: 95.9K
# Testcase Example:  '8'
#
# 
# Given a positive integer n and you can do operations as follow:
# 
# 
# 
# 
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# 
# 
# 
# 
# What is the minimum number of replacements needed for n to become 1?
# 
# 
# 
# 
# Example 1:
# 
# Input:
# 8
# 
# Output:
# 3
# 
# Explanation:
# 8 -> 4 -> 2 -> 1
# 
# 
# 
# Example 2:
# 
# Input:
# 7
# 
# Output:
# 4
# 
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
# 
# 
#
class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, count=0):
            # if n in table:
                # return table[n]
            if n==1:
                ans = count
            elif n%2 == 0:
                ans = helper(n/2, count+1)
            else:
                ans = min(helper(n-1, count+1), helper(n+1, count+1))
            # table[n] = ans
            return ans
        table = {}
        return helper(n)
