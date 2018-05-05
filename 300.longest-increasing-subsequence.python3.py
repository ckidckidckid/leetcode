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
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return 1
        arr = [1 for i in range(n)]
        ans = 1
        for i in range(1,n):
            lm = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    lm = max(lm, arr[j]+1)
            arr[i] = lm
            ans = max(ans, lm)
        print(arr)
        return ans
