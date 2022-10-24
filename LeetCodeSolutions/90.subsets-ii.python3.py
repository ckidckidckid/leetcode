#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (38.54%)
# Total Accepted:    147.4K
# Total Submissions: 382.5K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#
class Solution:
    def subsetsWithDup(self, nums, ordered = False, seen=None):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # BackTracking Idea from
        # https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
        def backtrack(tmp, s):
            ll.append(tmp[:])
            for i in range(s,len(nums)):
                if i>s and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(tmp, i+1)
                tmp.pop()

        nums.sort()
        ll = []
        backtrack([],0)
        return ll
