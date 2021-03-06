#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (44.55%)
# Total Accepted:    110.7K
# Total Submissions: 248.3K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
#
# Input: [1,3,4,2,2]
# Output: 2
#
#
# Example 2:
#
#
# Input: [3,1,3,4,2]
# Output: 3
#
# Note:
#
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
#
#
#
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ======================================================================
        # Trying an O(n) algorithm; Turns out it is the same as Linked List Cycle detection problem
        # ======================================================================
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

        # ======================================================================
        # Still O(nlog(n)) But trying a simplified approach
        # https://leetcode.com/problems/find-the-duplicate-number/discuss/72844/Two-Solutions-(with-explanation):-O(nlog(n))-and-O(n)-time-O(1)-space-without-changing-the-input-array
        # ======================================================================
        # s,e = 1,len(nums)-1
        # while s<e:
        #     m = s+(e-s)//2
        #     cnt=0
        #     for num in nums:
        #         if num<=m:
        #             cnt+=1
        #     if cnt>m:
        #         e=m
        #     else:
        #         s=m+1
        # return s

        # ======================================================================
        # O(nlog(n)) Solution; Accepted, but there exists a faster O(n) algorithm
        # ======================================================================
        # s,e=1,len(nums)-1
        # while s<=e:
        #     m = s + (e-s)//2
        #     sm=eq=lg=0
        #     for num in nums:
        #         if not s<=num<=e:
        #             continue
        #         if num==m:
        #             eq+=1
        #         elif num<m:
        #             sm+=1
        #         else:
        #             lg+=1
        #         if eq>1:
        #             return m
        #     if sm<lg:
        #         s=m+1
        #     else:
        #         e=m-1
        # return -1
