#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (26.85%)
# Total Accepted:    141.1K
# Total Submissions: 525.1K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ======================================================================
        # Trying improved O(n) solution|O(1) space;
        # ======================================================================

        pos = neg = 1
        ans = -float('inf')
        for i,n in enumerate(nums):
            if n<0:
                pos,neg=neg,pos
            pos = max(pos*n, n)
            neg = min(neg*n, n)
            ans = max(ans, pos)
        return ans

        # ======================================================================
        # Trying O(n) solution|O(n) space; Accepted, but beats only 11%
        # ======================================================================
        # n = len(nums)
        # if n < 1:
        #     return 0
        # pos = [0]*n
        # neg = [0]*n
        # ans = nums[0]
        # pos[0] = nums[0] if nums[0] >= 0 else 1
        # neg[0] = nums[0] if nums[0] < 0 else 1
        # for i in range(1,n):
        #     if nums[i] >= 0:
        #         pos[i] = max(pos[i-1]*nums[i], nums[i])
        #         neg[i] = min(neg[i-1]*nums[i], nums[i])
        #     else:
        #         pos[i] = max(neg[i-1]*nums[i], nums[i])
        #         neg[i] = min(pos[i-1]*nums[i], nums[i])
        #     ans = max(ans, pos[i])
        # return ans

        # ======================================================================
        # Trying O(n^2) solution; still times out
        # ======================================================================
        # n = len(nums)
        # ans = -float('inf')
        # for i in range(n):
        #     p = 1
        #     for j in range(i,n):
        #         p*=nums[j]
        #         ans = max(ans, p)
        # return ans

        # ======================================================================
        # O(n^3) solution; Times out
        # ======================================================================
        # n = len(nums)
        # ans = -float('inf')
        # for i in range(n):
        #     for j in range(i,n):
        #         p=1
        #         for k in range(i,j+1):
        #             p*=nums[k]
        #         ans = max(ans, p)
        # return ans
