#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# algorithms
# Medium (30.17%)
# Total Accepted:    104.4K
# Total Submissions: 346K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# There are N gas stations along a circular route, where the amount of gas at
# station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from station i to its next station (i+1). You begin the journey with
# an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit
# once in the clockwise direction, otherwise return -1.
#
# Note:
#
#
# If there exists a solution, it is guaranteed to be unique.
# Both input arrays are non-empty and have the same length.
# Each element in the input arrays is a non-negative integer.
#
#
# Example 1:
#
#
# Input:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
#
# Output: 3
#
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 +
# 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to
# station 3.
# Therefore, return 3 as the starting index.
#
#
# Example 2:
#
#
# Input:
# gas  = [2,3,4]
# cost = [3,4,3]
#
# Output: -1
#
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 =
# 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you
# start.
#
#
#
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # ==================================================================
        # O(n) solution;
        # After reading ideas from
        # https://leetcode.com/problems/gas-station/discuss/42568/Share-some-of-my-ideas.
        # ==================================================================
        n = len(gas)
        diff = 0
        for g,c in zip(gas, cost):
            diff += g-c
        if diff < 0:
            return -1
        ans = 0
        acc = gas[0]
        for i in range(0,n-1):
            if acc < cost[i]:
                ans = i+1
                acc = gas[i+1]
            else:
                acc += gas[i+1] - cost[i]
        return ans
        # ==================================================================
        # O(n^2) solution; times out
        # ==================================================================
        # n = len(gas)
        # for i in range(n):
        #     if cost[i] > gas[i]:
        #         continue
        #     g = gas[i]
        #     j=(i+1)%n
        #     prev=i
        #     while j!=i:
        #         g += gas[j] - cost[prev]
        #         if g < cost[j]:
        #             break
        #         prev = j
        #         j = (j+1)%n
        #     if j==i:
        #         return i
        # return -1
        #
