#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (44.14%)
# Total Accepted:    9.7K
# Total Submissions: 22.1K
# Testcase Example:  '[3,4,2]'
#
#
# Given an array nums of integers, you can perform operations on the array.
#
# In each operation, you pick any nums[i] and delete it to earn nums[i]
# points.  After, you must delete every element equal to nums[i] - 1 or nums[i]
# + 1.
#
# You start with 0 points.  Return the maximum number of points you can earn by
# applying such operations.
#
#
# Example 1:
#
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation:
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
#
#
#
# Example 2:
#
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation:
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
#
#
#
# Note:
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].
#
#
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(idx):
            if idx in cache:
                return cache[idx]
            elif idx<0:
                ans = 0
            elif idx==0:
                num, times = n_nums[0]
                ans = num*times
            else:
                curr_val, curr_cnt = n_nums[idx]
                next_val, next_cnt = n_nums[idx-1]
                if curr_val != next_val+1:
                    ans = curr_val*curr_cnt + helper(idx-1)
                else:
                    ans = max(curr_val*curr_cnt + helper(idx-2), helper(idx-1))
            cache[idx] = ans
            return ans

        ctr = Counter(nums)
        n_nums = []
        for k,v in ctr.items():
            n_nums.append((k,v))
        n_nums.sort()
        cache = {}
        return helper(len(n_nums)-1)
