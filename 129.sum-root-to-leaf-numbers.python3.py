#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (38.05%)
# Total Accepted:    137.3K
# Total Submissions: 360.6K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
# Example 2:
#
#
# Input: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root, acc=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Recursive easy solutions; accpeteds
        # if root is None:
        #     return 0
        # acc = acc*10 + root.val
        # if root.left is None and root.right is None:
        #     return acc
        # else:
        #     return self.sumNumbers(root.left, acc) + self.sumNumbers(root.right, acc)

        # Trying iterative solution 
        dummy = TreeNode(0)
        dummy.right = root
        st = [] # stack
        st.append((dummy,0))
        ans = 0
        while st:
            node, acc = st.pop()
            acc = acc*10 + node.val
            if node.right is None and node.left is None:
                ans += acc
            else:
                if node.right:
                    st.append((node.right, acc))
                if node.left:
                    st.append((node.left, acc))
        return ans
