#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (41.67%)
# Total Accepted:    161.4K
# Total Submissions: 387.1K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(node, acc):
            acc.append(str(node.val))
            if node.left is None and node.right is None:
                ans.append('->'.join(acc))
            if node.left:
                helper(node.left, acc)
            if node.right:
                helper(node.right, acc)
            acc.pop()

        ans = []
        if not root:
            return ans
        helper(root, [])
        return ans
