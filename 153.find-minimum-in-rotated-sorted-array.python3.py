#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (40.99%)
# Total Accepted:    197.9K
# Total Submissions: 482.5K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
#
#
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ======================================================================
        # Trying O(log(n))
        # ======================================================================
        if nums[0] < nums[-1]:
            return nums[0]
        n = len(nums)
        s,e=0,n-1
        while s <= e:
            m = s + (e-s)//2
            if (m==0 or nums[m-1] > nums[m]) and (m == n-1 or nums[m] < nums[m+1]):
                return nums[m]
            elif nums[m] <= nums[e]:
                e=m-1
            else:
                s=m+1
        # ======================================================================
        # O(n) gets accepted(cheeating); beats 10%
        # ======================================================================
        # return min(nums)
