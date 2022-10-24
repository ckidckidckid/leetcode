#
# [803] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (29.68%)
# Total Accepted:    5.7K
# Total Submissions: 19K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each fight starts from city u and
# arrives at v with a price w.
#
# Now given all the cities and fights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
#
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
#
#
# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
#
# Note:
#
#
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
#
#
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # def helper(src, dest, rem, seen, acc=0):
        #     if src == dest:
        #         return acc
        #     ans = float('inf')
        #     if rem == 0:
        #         return ans
        #     seen.add(src)
        #     for n in graph[src]:
        #         if n not in seen and acc+graph[src][n] < ans:
        #             sh = helper(n, dest, rem-1, seen, acc + graph[src][n])
        #             ans = min(ans, sh)
        #     seen.remove(src)
        #     return ans
        #
        #
        # graph = [{} for _ in range(n)]
        # for flight in flights:
        #     graph[flight[0]][flight[1]] = flight[2]
        # ans = helper(src, dst, K+1, seen=set())
        # return ans if ans < float('inf') else -1

        #  # TODO: Read Bellman Ford down below

        dp = [[float('inf') for _ in range(n)] for _ in range(K+2)]
        dp[0][src] = 0;
        for i in range(1,K+2):
            dp[i][src] = 0;
            for flight in flights:
                s = flight[0]
                d = flight[1]
                p = flight[2]
                dp[i][d] = min(dp[i][d], dp[i-1][s] + p);
        return dp[K + 1][dst] if dp[K + 1][dst] < float('inf') else -1
