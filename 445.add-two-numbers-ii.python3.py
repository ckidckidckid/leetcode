#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (46.27%)
# Total Accepted:    49.5K
# Total Submissions: 106.9K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def str_to_list(s,h=None,t=None):
            if len(s) == 0:
                return h
            else:
                if h is None:
                    h = t = ListNode(int(s[0]))
                else:
                    t.next = ListNode(int(s[0]))
                    t = t.next
                return str_to_list(s[1:], h, t)

        def list_to_int(node, acc=0):
            if node is None:
                return acc
            else:
                return list_to_int(node.next, acc*10+node.val)
                
        n1 = list_to_int(l1)
        n2 = list_to_int(l2)
        n = n1+n2

        return str_to_list(str(n))
