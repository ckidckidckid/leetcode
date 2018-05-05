#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (47.35%)
# Total Accepted:    89.2K
# Total Submissions: 188.3K
# Testcase Example:  '3\n7'
#
#
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
#
# Note:
#
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#
#
# Example 2:
#
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
#
#
#
#
class Solution:
    def combinationSum3(self, k, n, start = 1, table={}):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if (k,n,start) in table:
            return table[(k,n,start)]
        if n == start and k==1:
            ans = [[start]]
        elif n < start or k<=0:
            ans = []
        else:
            ans = []
            sr1 = self.combinationSum3(k-1, n-start, start+1) if start < 9 else []
            for s in sr1:
                # if len(s) > 0:
                ans.append([start] + s)
            sr2 = self.combinationSum3(k, n, start+1) if start < 9 else []
            ans += sr2
        # print("k={},n={},start={},ans={}".format(k,n,start, ans))
        table[(k,n,start)] = ans
        return ans
