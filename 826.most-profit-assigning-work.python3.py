#
# [853] Most Profit Assigning Work
#
# https://leetcode.com/problems/most-profit-assigning-work/description/
#
# algorithms
# Medium (31.68%)
# Total Accepted:    2.1K
# Total Submissions: 6.7K
# Testcase Example:  '[2,4,6,8,10]\n[10,20,30,40,50]\n[4,5,6,7]'
#
# We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i]
# is the profit of the ith job. 
#
# Now we have some workers. worker[i] is the ability of the ith worker, which
# means that this worker can only complete a job with difficulty at most
# worker[i]. 
#
# Every worker can be assigned at most one job, but one job can be completed
# multiple times.
#
# For example, if 3 people attempt the same job that pays $1, then the total
# profit will be $3.  If a worker cannot complete any job, his profit is $0.
#
# What is the most profit we can make?
#
# Example 1:
#
#
# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker =
# [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get
# profit of [20,20,30,30] seperately.
#
# Notes:
#
#
# 1 <= difficulty.length = profit.length <= 10000
# 1 <= worker.length <= 10000
# difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
#
#
from bisect import bisect_right
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        dp = [(d,p) for d,p in zip(difficulty, profit)]
        dp.sort()
        max_seen = 0

        for i in range(len(dp)):
            difficulty[i] = dp[i][0]
            max_seen = max(max_seen, dp[i][1])
            dp[i] = (dp[i][0], max_seen)
        ans = 0
        for w in worker:
            e = bisect_right(difficulty, w)
            if e==0:
                continue
            if e == len(difficulty) or difficulty[e-1] <= w:
                e-=1
            ans += dp[e][1]
        return ans
