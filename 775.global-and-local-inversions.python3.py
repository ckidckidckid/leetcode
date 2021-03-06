#
# [790] Global and Local Inversions
#
# https://leetcode.com/problems/global-and-local-inversions/description/
#
# algorithms
# Medium (33.05%)
# Total Accepted:    5.8K
# Total Submissions: 17.6K
# Testcase Example:  '[0]'
#
# We have some permutation A of [0, 1, ..., N - 1], where N is the length of
# A.
#
# The number of (global) inversions is the number of i < j with 0 <= i < j < N
# and A[i] > A[j].
#
# The number of local inversions is the number of i with 0 <= i < N and A[i] >
# A[i+1].
#
# Return true if and only if the number of global inversions is equal to the
# number of local inversions.
#
# Example 1:
#
#
# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.
#
#
# Example 2:
#
#
# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.
#
#
# Note:
#
#
# A will be a permutation of [0, 1, ..., A.length - 1].
# A will have length in range [1, 5000].
# The time limit for this problem has been reduced.
#
#
from bisect import bisect_left, insort
class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Idea : to check if local inversions can keep up with global inversion
        # Extremely fast solution at
        # https://leetcode.com/problems/global-and-local-inversions/discuss/113651/Python-easy-understanding-solution!
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        n = len(A)
        for i in range(n):
            if abs(i-A[i]) > 1:
                return False
        return True

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Generalized solution; O(n) time https://leetcode.com/problems/global-and-local-inversions/discuss/113661/Generalize-to-any-integer-array-(not-necessarily-a-0-greaterN-permutation)
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # n = len(A)
        # if n <= 1:
        #     return True
        # i=1
        # while i < n:
        #     if A[i-1] > A[i]:
        #         A[i-1], A[i] = A[i], A[i-1]
        #         i+=1
        #     i+=1
        # for i in range(1,n):
        #     if A[i] < A[i-1]:
        #         return False
        # return True

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # O(nlogn) solution
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # n = len(A)
        # A.append(n)
        # li = gi = 0
        # seen = [n]
        # for i in range(n-1,-1,-1):
        #     li += A[i] > A[i+1]
        #     gi += bisect_left(seen, A[i])
        #     insort(seen, A[i])
        # return li == gi
