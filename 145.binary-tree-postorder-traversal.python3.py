#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (42.64%)
# Total Accepted:    181.9K
# Total Submissions: 426.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [3,2,1]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        st = []
        ans = []
        st.append(root)
        while st:
            n = st.pop()
            if not n.left and not n.right:
                ans.append(n.val)
            else:
                r = n.right
                l = n.left
                n.right = n.left = None
                st.append(n)
                if r:
                    st.append(r)
                if l:
                    st.append(l)
        return ans
