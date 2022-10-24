#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (31.23%)
# Total Accepted:    89.1K
# Total Submissions: 285.3K
# Testcase Example:  '[1,3,null,null,2]'
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Example 1:
#
#
# Input: [1,3,null,null,2]
#
# 1
# /
# 3
# \
# 2
#
# Output: [3,1,null,null,2]
#
# 3
# /
# 1
# \
# 2
#
#
# Example 2:
#
#
# Input: [3,1,4,null,null,2]
#
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
#
# Output: [2,1,4,null,null,3]
#
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
#
#
# Follow up:
#
#
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        def inorder_edit(node):
            if node.left:
                inorder_edit(node.left)
            node.val = ino[s[0]]
            s[0]+=1
            if node.right:
                inorder_edit(node.right)

        s = [0]
        ino = inorder(root)
        ino.sort()
        print(ino)
        inorder_edit(root)
