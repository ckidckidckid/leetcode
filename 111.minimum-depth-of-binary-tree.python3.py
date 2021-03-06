#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (33.64%)
# Total Accepted:    216.1K
# Total Submissions: 642.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its minimum depth = 2.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS Solution; Faster because if one branch of tree is very deep, we need not visit there
        from collections import deque
        if not root:
            return 0
        q = deque()
        q.append((root,1))
        while q:
            node,level = q.popleft()
            if not any((node.left, node.right)):
                return level
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))

        # ========================================
        # Original simple recursive DFS solution;
        # ========================================
        if root is None:
            return 0
        elif all((root.left, root.right)):
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
