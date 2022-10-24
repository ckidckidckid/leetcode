#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (37.85%)
# Total Accepted:    112.4K
# Total Submissions: 297K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
#
from collections import deque
class Solution:
    table = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # =====================================================================
        # O(n) Static DP solution
        # =====================================================================
        m = len(self.table)
        for i in range(m,n+1):
            j=1
            self.table.append(float('inf'))
            while j*j <= i:
                self.table[i] = min(self.table[i], self.table[i - j*j]+1)
                j+=1
        return self.table[n]

        # =====================================================================
        # O(n) DP solution
        # =====================================================================
        # table = [float('inf')]*(n+1)
        # table[0] = 0
        # for i in range(1,n+1):
        #     j=1
        #     while j*j <= i:
        #         table[i] = min(table[i], table[i - j*j]+1)
        #         j+=1
        # return table[n]

        # =====================================================================
        # O(n) BFS solution; Times out
        # =====================================================================

        # squares = [i*i for i in range(1,100000)]
        # squares_st = set(squares)
        # if n in squares_st:
        #     return 1
        # q = deque()
        # q.append((n,1))
        # visited = {n}
        # while q:
        #     val,steps = q.popleft()
        #     for sq in squares:
        #         if val-sq<0:
        #             break
        #         if val-sq in squares_st:
        #             return steps+1
        #         if val-sq not in visited:
        #             q.append((val-sq, steps+1))
        #             visited.add(val-sq)
        # return -1
