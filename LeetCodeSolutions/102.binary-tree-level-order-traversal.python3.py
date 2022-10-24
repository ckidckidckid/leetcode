#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (42.91%)
# Total Accepted:    241.7K
# Total Submissions: 562.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque()
        if root:
            q.append((root, 0))
        table = {}
        max_level = -1
        while q:
            node,level = q.popleft()
            if level not in table:
                table[level] = []
            table[level].append((node.val))
            max_level = max(max_level, level)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))

        return [table[level] for level in range(max_level+1)]
