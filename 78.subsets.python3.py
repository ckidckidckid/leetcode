#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (45.25%)
# Total Accepted:    237.2K
# Total Submissions: 524.1K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # BackTracking Idea from
        # https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
        def backtrack(tmp, s):
            ll.append(tmp[:])
            for i in range(s,len(nums)):
                tmp.append(nums[i])
                backtrack(tmp, i+1)
                tmp.pop()

        nums.sort()
        ll = []
        backtrack([],0)
        return ll
