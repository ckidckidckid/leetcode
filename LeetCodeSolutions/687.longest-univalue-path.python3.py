#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (32.84%)
# Total Accepted:    27K
# Total Submissions: 82.2K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of
# edges between them.
#
#
# Example 1:
#
#
#
#
# Input:
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
#
#
# Output:
#
# 2
#
#
#
#
# Example 2:
#
#
#
#
# Input:
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
#
#
# Output:
#
# 2
#
#
#
# Note:
# The given binary tree has not more than 10000 nodes.  The height of the tree
# is not more than 1000.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node.left is None and node.right is None:
                return (1,1)
            else:
                l_max, l_ext = helper(node.left) if node.left is not None else (0,0)
                r_max, r_ext = helper(node.right) if node.right is not None else (0,0)
                l_ext = l_ext if node.left is not None and node.left.val == node.val else 0
                r_ext = r_ext if node.right is not None and node.right.val == node.val else 0

                ext_ans = 1 + max(l_ext, r_ext)
                c_thru = 1 + l_ext +r_ext

                ans = max(l_max, r_max, ext_ans, c_thru)
                return (ans, ext_ans)

        if root is None:
            ans = 1
        else:
            ans,_ = helper(root)
        return ans-1
