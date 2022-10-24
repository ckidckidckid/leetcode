#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (38.94%)
# Total Accepted:    126K
# Total Submissions: 323.4K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is
# 4. Note that there may be more than one LIS combination, it is only necessary
# for you to return the length.
#
#
# Your algorithm should run in O(n2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tails = []
        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)
