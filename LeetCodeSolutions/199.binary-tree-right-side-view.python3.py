#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (42.73%)
# Total Accepted:    110.2K
# Total Submissions: 257.5K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, level):
            table[level] = root.val
            max_depth[0] = max(max_depth[0], level)
            if root.left:
                inorder(root.left, level+1)
            if root.right:
                inorder(root.right, level+1)

        if not root:
            return []
        table = {}
        max_depth = [-1]
        inorder(root, 0)
        return [table[x] for x in range(max_depth[0]+1)]
