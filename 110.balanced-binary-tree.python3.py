#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (38.51%)
# Total Accepted:    225.4K
# Total Submissions: 585.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# Return false.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self, node):
        if node == None:
            return 0
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return abs(self.depth(root.left)-self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


        # def depth(node):
        #     if node is None:
        #         return {'l':0,'r':0}
        #     else:
        #         return {'l' : max(depth(node.left)['l'], depth(node.left)['r'])+1, 'r' :max(depth(node.right)['l'], depth(node.right)['r'])+1}
        #
        # def helper(node):
        #     h = id(node)
        #     o = None
        #     if h in table:
        #         o = table[h]
        #     else:
        #         o = depth(node)
        #         table[h] = o
        #     return abs(o['l'] - o['r']) <= 1 and ( node is None or (helper(node.left) and helper(node.right)))
        # table = {}
        # return helper(root)
