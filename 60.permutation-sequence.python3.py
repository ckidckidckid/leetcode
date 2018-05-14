#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (29.69%)
# Total Accepted:    103.3K
# Total Submissions: 347.8K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# Given n and k, return the kth permutation sequence.
#
# Note:
#
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
#
#
# Example 1:
#
#
# Input: n = 3, k = 3
# Output: "213"
#
#
# Example 2:
#
#
# Input: n = 4, k = 9
# Output: "2314"
#
#
#
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        f_table = [1,1,2,6,24,120,720,5040,40320,362880, 3628800]
        table = [x for x in range(1,n+1)]
        ans = ''
        while table:
            n = len(table)
            idx = (k-1)//f_table[n-1]
            val = table.pop(idx)
            ans += str(val)
            k=((k-1)%f_table[n-1]) + 1
        return ans
