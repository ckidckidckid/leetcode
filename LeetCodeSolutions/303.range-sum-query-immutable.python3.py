#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (32.49%)
# Total Accepted:    95.5K
# Total Submissions: 293.9K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
#
#
# Note:
#
# You may assume that the array does not change.
# There are many calls to sumRange function.
#
#
#
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cum_sum = [0]*len(nums)
        for i,val in enumerate(nums):
            self.cum_sum[i] = val + (self.cum_sum[i-1] if i>0 else 0)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cum_sum[j]- (self.cum_sum[i-1] if i > 0 else 0)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
