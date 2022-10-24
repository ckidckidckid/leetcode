#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (43.74%)
# Total Accepted:    132.1K
# Total Submissions: 301.7K
# Testcase Example:  '[]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h)
# memory, where h is the height of the tree.
#
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.st = []
        while root:
            self.st.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.st) > 0

    def next(self):
        """
        :rtype: int
        """
        n = self.st.pop()
        nr = n.right
        while nr:
            self.st.append(nr)
            nr = nr.left
        return n.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
