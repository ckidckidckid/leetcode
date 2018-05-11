#
# [747] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (43.28%)
# Total Accepted:    24.8K
# Total Submissions: 57.2K
# Testcase Example:  '[0,0,0,0]'
#
#
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
# indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to
# find minimum cost to reach the top of the floor, and you can either start
# from the step with index 0, or the step with index 1.
#
#
# Example 1:
#
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the
# top.
#
#
#
# Example 2:
#
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping
# cost[3].
#
#
#
# Note:
#
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].
#
#
#
class Solution:
    def helper(self, cost, table=None):
        if len(cost) in table:
            return table[len(cost)]
        ans = 0
        if 0 < len(cost) <= 2:
            ans = cost[0]
        else:
            ans = cost[0] + \
                    min(self.helper(cost[1:], table),
                        self.helper(cost[2:], table)
                    )
        table[len(cost)] = ans
        return ans

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # ========================================
        # Recursive; Accepted but very very slow
        # ========================================
        # if cost is None or len(cost) <= 2:
        #     return 0
        # table = {}
        # return min(self.helper(cost, table), self.helper(cost[1:], table))

        # ========================================
        # Attempting bottom up apprach; much faster
        # ========================================
        n = len(cost)
        p,c = 0,0
        for i in range(2,n+1):
            t = c
            c = min(cost[i-1]+c, cost[i-2] + p)
            p = t
        return c
