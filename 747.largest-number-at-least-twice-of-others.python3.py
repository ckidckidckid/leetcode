#
# [748] Largest Number At Least Twice of Others
#
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
#
# algorithms
# Easy (41.46%)
# Total Accepted:    18.8K
# Total Submissions: 45.4K
# Testcase Example:  '[0,0,0,1]'
#
# In a given integer array nums, there is always exactly one largest element.
#
# Find whether the largest element in the array is at least twice as much as
# every other number in the array.
#
# If it is, return the index of the largest element, otherwise return -1.
#
# Example 1:
#
#
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the
# array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return
# 1.
#
#
#
#
# Example 2:
#
#
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return
# -1.
#
#
#
#
# Note:
#
#
# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].
#
#
#
#
#
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx,m = -1,-float('inf')
        for i,n in enumerate(nums):
            if n > m:
                idx,m = i,n
        for n in nums:
            if n != m and m < 2*n:
                return -1
        return idx
