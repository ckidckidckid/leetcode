#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (37.00%)
# Total Accepted:    139K
# Total Submissions: 375.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque()
        if root:
            q.append((root, 0))
        ans = []
        max_level = -1
        even = True
        while q:
            if even:
                node,level = q.popleft()
                children = [node.right, node.left]
            else:
                node,level = q.pop()
                children = [node.left, node.right]

            if level>max_level:
                max_level=level
                ans.append([])
                ans[level] = []
                if even:
                    q.appendleft((node, level))
                else:
                    q.append((node,level))
                even = not even
                continue

            ans[level].append((node.val))
            for child in children:
                if child:
                    if even:
                        q.append((child, level+1))
                    else:
                        q.appendleft((child, level+1))

        return ans
