#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (41.47%)
# Total Accepted:    144K
# Total Submissions: 347K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
#
# Example:
#
#
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#
#
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(s,e,k):
            ans = []
            if k==0 or e-s+1<k:
                return [ans]
            elif e-s+1==k:
                ans = [list(range(s,e+1))]
            else:
                for sub in helper(s+1, e, k-1):
                    ans.append([s] + sub)
                for sub in helper(s+1, e, k):
                    ans.append(sub)
            return ans
        return helper(1,n,k)
