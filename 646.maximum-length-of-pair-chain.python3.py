#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (47.27%)
# Total Accepted:    19.2K
# Total Submissions: 40.6K
# Testcase Example:  '[[1,2], [2,3], [3,4]]'
#
#
# You are given n pairs of numbers. In every pair, the first number is always
# smaller than the second number.
#
#
#
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b
# < c. Chain of pairs can be formed in this fashion.
#
#
#
# Given a set of pairs, find the length longest chain which can be formed. You
# needn't use up all the given pairs. You can select pairs in any order.
#
#
#
# Example 1:
#
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
#
#
#
# Note:
#
# The number of given pairs will be in the range [1, 1000].
#
#
#
from bisect import bisect_left

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # Idea similar to Longest Increasing Subsequence solution.
        # O(nlog(n)) time and O(n) space
        # https://github.com/ckidckidckid/leetcode/blob/master/300.longest-increasing-subsequence.python3.py
        ################################################################################

        # tails = []
        # pairs.sort()
        # for pair in pairs:
        #     idx = bisect_left(tails, pair[0])
        #     if idx >= len(tails):
        #         tails.append(pair[1])
        #     if pair[1] < tails[idx]:
        #         tails[idx] = pair[1]
        # return len(tails)

        # Greedy Solution; Faster ; O(nlog(n)) time though, but O(1) space
        # https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/105607/4-Liner-Python-Greedy

        pairs.sort(key = lambda x : x[1])
        cur, res = float('-inf'), 0
        for pair in pairs:
            if pair[0] > cur:
                cur, res = pair[1], res+1
        return res
