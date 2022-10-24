#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (35.40%)
# Total Accepted:    106.1K
# Total Submissions: 299.8K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# Example: 
#
#
# You may serialize the following tree:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
#
# as "[1,2,3,null,null,4,5]"
#
#
# Clarification: Just the same as how LeetCode OJ serializes a binary tree. You
# do not necessarily need to follow this format, so please be creative and come
# up with different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node is None:
                arr.append(None)
            else:
                arr.append(node.val)
                preorder(node.left)
                preorder(node.right)

        arr = []
        preorder(root)
        str_arr = [str(x) if x is not None else '$' for x in arr]
        serial = ','.join(str_arr)
        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        str_arr = data.split(',')
        arr = [int(x) if x != '$' else None for x in str_arr]
        dummy = TreeNode(-1)
        st = deque([dummy])
        prev_None = True
        for val in arr:
            node = TreeNode(val)
            if prev_None:
                parent = st.pop()
                parent.right = node if val is not None else None
            else:
                parent = st[-1]
                parent.left = node if val is not None else None

            if val is not None:
                st.append(node)
                prev_None = False
            else:
                prev_None = True
        return dummy.right


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
