#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (40.20%)
# Total Accepted:    47.2K
# Total Submissions: 117.3K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
#
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
#
#
# Example 1:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
#
# Given tree t:
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
# Return true, because t has the same structure and node values with a subtree
# of s.
#
#
# Example 2:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
#
# Given tree t:
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
# Return false.
#
#
class Solution:
    def is_exact_match(self,s,t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.is_exact_match(s.left, t.left) and self.is_exact_match(s.right, t.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.is_exact_match(s, t) or (s != None and (self.isSubtree(s.left, t) or self.isSubtree(s.right, t)))
