#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.65%)
# Total Accepted:    120.6K
# Total Submissions: 369.3K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true,
# otherwise return false.
#
# Example 1:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
# Follow up:
#
#
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
#
#
#
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        if n==0:
            return False
        e = n-1
        for i in range(1,n):
            if nums[i] < nums[(i-1)%n]:
                e = i-1
                break
        if nums[0] <= target <= nums[e]:
            st=0
            en=e
        else:
            st=e+1
            en=n-1
        while en>=st:
            mid = (st + (en - st)//2)
            print(st, en, mid)
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                en = mid-1
            else:
                st = st+1
        return False
