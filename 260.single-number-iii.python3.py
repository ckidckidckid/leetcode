#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (53.48%)
# Total Accepted:    82.9K
# Total Submissions: 154.9K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
#
# Example:
#
#
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
#
# Note:
#
#
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
#
#
#
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ======================================================================
        # O(n) time, O(1) space; Got the idea from discussions
        # ======================================================================
        x = 0
        for num in nums:
            x ^= num
        bit_set = 0
        ans = [0,0]
        while x%2 == 0:
            x >>= 1
            bit_set += 1
        for num in nums:
            ans[(num >> bit_set) % 2] ^= num
        return ans
