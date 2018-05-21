#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (23.61%)
# Total Accepted:    94.7K
# Total Submissions: 400.4K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
#
# Example 1:
#
#
# Input: [10,2]
# Output: "210"
#
# Example 2:
#
#
# Input: [3,30,34,5,9]
# Output: "9534330"
#
#
# Note: The result may be very large, so you need to return a string instead of
# an integer.
#
#
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not any(nums): return '0'
        transformed, len_table = [], {}
        for i,num in enumerate(nums):
            s = str(num)
            len_table[i] = len(s)
            s =  s + s[0] + s[::-1]
            transformed.append((s, i))
        transformed.sort(reverse=True)
        return ''.join([s[:len_table[idx]] for (s,idx) in transformed])
