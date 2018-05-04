#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (39.85%)
# Total Accepted:    194.5K
# Total Submissions: 487.9K
# Testcase Example:  '[2,1]\nnode with value 2\nnode with value 1'
#
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
#
#
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of
# itself).”
#
#
#
# ⁠       _______6______
# ⁠      /              \
# ⁠   ___2__          ___8__
# ⁠  /      \        /      \
# ⁠  0      _4       7       9
# ⁠        /  \
# ⁠        3   5
#
#
#
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
# example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
# itself according to the LCA definition.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x, l=None, r=None):
#         self.val = x
#         self.left = l
#         self.right = r

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if p is None or p is None:
            return root
        if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
            return root
        if (root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

# if __name__ == '__main__':
#     s = Solution()
#     root = TreeNode(3 ,TreeNode(1, None, 2), TreeNode(4))
#     p = TreeNode(2)
#     q = TreeNode(4)
#     s.lowestCommonAncestor(root, p, q)
