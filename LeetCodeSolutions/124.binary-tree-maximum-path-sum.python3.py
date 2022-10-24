#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (27.28%)
# Total Accepted:    128.8K
# Total Submissions: 471.7K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
#
# Example 1:
#
#
# Input: [1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# Output: 6
#
#
# Example 2:
#
#
# Input: [-10,9,20,null,null,15,7]
#
# -10
# / \
# 9  20
# /  \
# 15   7
#
# Output: 42
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Recursive solution with Memoization
        # each node returns 2 values via helper ==> (best_path_with_root_begin, best_path_without_root_begin)
        MIN = -float('inf')
        def helper(node):
            if node in table:
                return table[node]
            if not node:
                return (MIN, MIN)
            elif not node.left and not node.right:
                ans = (node.val, MIN)
            else:
                lsub_r, lsub_ur = helper(node.left)
                rsub_r, rsub_ur = helper(node.right)
                best_r = max(node.val, node.val+lsub_r, node.val+rsub_r)
                best_ur = max(lsub_r, lsub_ur, rsub_r, rsub_ur, lsub_r + rsub_r + node.val)
                ans = (best_r, best_ur)
            table[node] = ans
            return ans
        table = {}
        return max(helper(root))
