#
# [744] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (35.35%)
# Total Accepted:    7.9K
# Total Submissions: 22.4K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
#
# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K.  How long will it take for all
# nodes to receive the signal?  If it is impossible, return -1.
#
#
# Note:
#
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1  and 1 .
#
#
#
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        distance = [float('inf')]*(N+1)
        distance[0] = -1
        distance[K] = 0
        graph = defaultdict(dict)
        for t in times:
            graph[t[0]][t[1]] = t[2]
        q = [(0,K)]
        visited = set()
        while q:
            dist, node = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            for child, child_dist in graph[node].items():
                if child not in visited:
                    distance[child] = min(distance[child], child_dist+dist)
                    heapq.heappush(q, (distance[child], child))
        return max(distance) if max(distance) < float('inf') else -1
