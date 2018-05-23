#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (26.09%)
# Total Accepted:    117.3K
# Total Submissions: 449.6K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Note:
#
# You can assume that you can always reach the last index.
#
from collections import deque

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        steps = 0
        q = deque()
        q.append((0,0))
        for i in range(n):
            reach,steps = q[0]
            if i+nums[i] > q[-1][0]:
                q.append((i+nums[i], steps+1))
            if reach == i:
                q.popleft()
        return steps
