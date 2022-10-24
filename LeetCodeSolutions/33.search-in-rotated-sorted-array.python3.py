#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (31.92%)
# Total Accepted:    257.9K
# Total Submissions: 807.8K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
#
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Idea similar to solution in
        # https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14601/Java-intuitive-closest-to-unflavored-binary-search
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: # mid is larger than target
                # hi=mid-1 ====> Normal binary search
                if nums[lo] <= nums[mid] and nums[lo] > target: # left half is monotonic, yet the target is not in the left half
                    lo = mid+1
                else: # left is not monotonic OR target is the the left half, continue as regular binary search
                    hi = mid-1
            else: # complementary case
                if nums[hi] >= nums[mid] and target > nums[hi]:
                    hi = mid-1
                else:
                    lo = mid+1
        return -1
