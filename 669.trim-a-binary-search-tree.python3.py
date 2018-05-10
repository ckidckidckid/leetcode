#
# [669] Trim a Binary Search Tree
#
# https://leetcode.com/problems/trim-a-binary-search-tree/description/
#
# algorithms
# Easy (58.10%)
# Total Accepted:    31.9K
# Total Submissions: 54.8K
# Testcase Example:  '[1,0,2]\n1\n2'
#
#
# Given a binary search tree and the lowest and highest boundaries as L and R,
# trim the tree so that all its elements lies in [L, R] (R >= L). You might
# need to change the root of the tree, so the result should return the new root
# of the trimmed binary search tree.
#
#
# Example 1:
#
# Input:
# ⁠   1
# ⁠  / \
# ⁠ 0   2
#
# ⁠ L = 1
# ⁠ R = 2
#
# Output:
# ⁠   1
# ⁠     \
# ⁠      2
#
#
#
# Example 2:
#
# Input:
# ⁠   3
# ⁠  / \
# ⁠ 0   4
# ⁠  \
# ⁠   2
# ⁠  /
# ⁠ 1
#
# ⁠ L = 1
# ⁠ R = 3
#
# Output:
# ⁠     3
# ⁠    /
# ⁠  2
# ⁠ /
# ⁠1
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
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # Recursive Solution (72ms, 33%); from
        # https://leetcode.com/problems/trim-a-binary-search-tree/discuss/107000/Java-solution-6-liner

        # if root is None:
        #     return None
        # left_sub = self.trimBST(root.left, L, R)
        # right_sub = self.trimBST(root.right, L, R)
        # if root.val > R:
        #     return left_sub
        # elif root.val < L:
        #     return right_sub
        # root.left = left_sub
        # root.right = right_sub
        # return root

        # Iterative Solution; from
        # https://leetcode.com/problems/trim-a-binary-search-tree/discuss/107026/Java-solution-iteration-version

        while root is not None and not L <= root.val <= R:
            if root.val < L:
                root=root.right
            if root.val > R:
                root = root.left
        dummy = root
        while dummy is not None:
            while dummy.left is not None and dummy.left.val < L:
                dummy.left = dummy.left.right
            dummy = dummy.left

        dummy = root
        while dummy is not None:
            while dummy.right is not None and dummy.right.val > R:
                dummy.right = dummy.right.left
            dummy = dummy.right
        return root
