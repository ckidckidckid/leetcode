#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (32.93%)
# Total Accepted:    104.8K
# Total Submissions: 317.9K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
#
# Example 1:
#
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
#
#
# Example 2:
#
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
#
#
#
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if len(nums) == 0:
            return ans
        s = None
        prev = None
        for n in nums:
            if s is None:
                s = prev = n
            elif n == prev + 1:
                prev = n
            else:
                ans.append((str(s) + '->' + str(prev)) if s != prev else str(prev))
                s = prev = n
        ans.append((str(s) + '->' + str(nums[-1])) if s != nums[-1] else str(nums[-1]))
        return ans
