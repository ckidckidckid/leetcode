#
# [811] Number of Subarrays with Bounded Maximum
#
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (41.34%)
# Total Accepted:    4.5K
# Total Submissions: 10.9K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# We are given an array A of positive integers, and two positive integers L and
# R (L <= R).
#
# Return the number of (contiguous, non-empty) subarrays such that the value of
# the maximum array element in that subarray is at least L and at most R.
#
#
# Example :
# Input:
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2,
# 1], [3].
#
#
# Note:
#
#
# L, R  and A[i] will be an integer in the range [0, 10^9].
# The length of A will be in the range of [1, 50000].
#
#
#
class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # O(n) time ; O(1) space solution
        # https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/117599/Ridiculously-Simple-O(n)O(1)-Java-Solution-based-on-State-Machine
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        ans = 0
        viable = False
        lastViable = -1
        lastBigger = -1
        for i,n in enumerate(A):
            if n > R:
                viable = False
                lastBigger = i
                continue
            if L <= n <= R:
                viable = True
                lastViable = i
            if viable:
                ans += lastViable-lastBigger

        return ans


        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # O(n^2) solution; TLE
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # n = len(A)
        # ans = 0
        # for i in range(n):
        #     m = 0
        #     for j in range(i,n):
        #         m = max(m, A[j])
        #         if L <= m <= R:
        #             ans += 1
        # return ans
