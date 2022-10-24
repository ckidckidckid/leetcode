#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (29.63%)
# Total Accepted:    167.8K
# Total Submissions: 566.4K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        n = len(nums)
        for i in range(n):
            reach = max(reach, i+nums[i])
            if i!=n-1 and nums[i]==0 and reach<i+1:
                return False
        return True
        # =============================================
        # Correct, but not Accepted: Times out
        # =============================================
        # if not nums or len(nums)<=1:
        #     return True
        # arr = [0 for _ in nums]
        # arr[0] = 1
        # curr_pos = [0]
        # new_pos = []
        # while len(curr_pos) > 0:
        #     for c in curr_pos:
        #         for jump in range(nums[c]-1,-1,-1):
        #             nv = c+jump+1
        #             if nv==len(nums)-1:
        #                 return True
        #             if not nv < len(nums) or arr[nv] == 1:
        #                 continue
        #             arr[nv] = 1
        #             new_pos.append(nv)
        #     curr_pos,new_pos=new_pos,[]
        # return False
