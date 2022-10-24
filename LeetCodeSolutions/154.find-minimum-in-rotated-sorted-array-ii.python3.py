#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (37.94%)
# Total Accepted:    97.4K
# Total Submissions: 256.6K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# The array may contain duplicates.
#
# Example 1:
#
#
# Input: [1,3,5]
# Output: 1
#
# Example 2:
#
#
# Input: [2,2,2,0,1]
# Output: 0
#
# Note:
#
#
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
#
#
#
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # =======================================================
        # Apparently O(log(n)) is impossible for repeated elements
        # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48849/Stop-wasting-your-time.-It-most-likely-has-to-be-O(n).
        # =======================================================
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
