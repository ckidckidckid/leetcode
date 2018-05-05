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
    def helper(self, k, n, start=1, seen=set()):
        if start>9: return None

        if k==0:
            if n==0: return []
            else: return None
        if k==1:
            if n>=start and n<10:  return [[n]]
            else: return None
        res = []

        for i in range(start, 10):
            if i>n: break
            if i in seen: continue
            seen.add(i)
            subress = self.helper(k-1, n-i, i+1, seen)
            seen.remove(i)
            if subress is None or len(subress) == 0:
                continue
            for subres in subress:
                t = [i] + subres
                res.append(t)
        return res

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.helper(k, n)
