#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap/description/
#
# algorithms
# Hard (30.18%)
# Total Accepted:    56.5K
# Total Submissions: 187.2K
# Testcase Example:  '[3,6,9,1]'
#
# Given an unsorted array, find the maximum difference between the successive
# elements in its sorted form.
#
# Return 0 if the array contains less than 2 elements.
#
# Example 1:
#
#
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
# (3,6) or (6,9) has the maximum difference 3.
#
# Example 2:
#
#
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
#
# Note:
#
#
# You may assume all elements in the array are non-negative integers and fit in
# the 32-bit signed integer range.
# Try to solve it in linear time/space.
#
#
#
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ======================================================================
        # Trying radix sort
        # ======================================================================
        n = len(nums)
        if n<2:
            return 0
        biggest = max(nums)
        pow = 1
        while pow <= biggest:
            bucket = [0]*10
            for num in nums:
                bucket[(num//pow)%10] += 1
            for i in range(1,10):
                bucket[i]+= bucket[i-1]
            rev = nums[::-1]
            for num in rev:
                digit = (num//pow)%10
                bucket[digit]-=1
                idx = bucket[digit]
                nums[idx] = num
            pow *= 10

        ans = 0
        for i in range(1,n):
            ans = max(ans, nums[i]-nums[i-1])
        return ans
        # ======================================================================
        # Count sort; times out
        # ======================================================================
        # if len(nums)<2:
        #     return 0
        # state = 0
        # smallest = float('inf')
        # for num in nums:
        #     smallest = min(smallest, num)
        #     state |= 1<<num
        # state = state>>(smallest+1)
        # ans = 0
        # count = 1
        # while state:
        #     if state & 1:
        #         ans = max(ans, count)
        #         count = 0
        #     count+=1
        #     state = state >> 1
        # return ans
