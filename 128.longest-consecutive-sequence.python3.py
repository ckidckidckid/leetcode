#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (38.41%)
# Total Accepted:    142.4K
# Total Submissions: 370.7K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
#
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        ans = 0
        for num in nums:
            if num in table:
                continue
            elif num+1 not in table and num-1 not in table:
                table[num] = (num, 1)
            else:
                to_add = 0
                t=num+1
                while t in table:
                    val,count = table[t]
                    to_add += count
                    table[t] = (num, 0)
                    if val == t:
                        break
                    else:
                        t = val
                t=num-1
                while t in table:
                    val,count = table[t]
                    to_add += count
                    table[t] = (num, 0)
                    if val == t:
                        break
                    else:
                        t = val
                table[num] = (num, 1 + to_add)
            ans = max(ans, table[num][1])
        return ans
