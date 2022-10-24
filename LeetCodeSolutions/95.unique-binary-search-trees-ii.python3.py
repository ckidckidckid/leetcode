#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (32.40%)
# Total Accepted:    102.4K
# Total Submissions: 316K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import lru_cache
class Solution:
    @lru_cache(maxsize = 10000)
    def helper(self, n, s=1):
        ans = []
        if n<s:
            return [None]
        elif n==s:
            ans.append(TreeNode(n))
        else:
            for val in range(s,n+1):
                left_childs = self.helper(val-1,s)
                right_childs = self.helper(n, val+1)
                for l in left_childs:
                    for r in right_childs:
                        root = TreeNode(val)
                        root.left = l
                        root.right = r
                        ans.append(root)
        return ans

    def generateTrees(self, n, s=1):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        else:
            return self.helper(n,1)
