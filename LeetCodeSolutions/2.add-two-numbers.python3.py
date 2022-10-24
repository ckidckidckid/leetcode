#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (28.68%)
# Total Accepted:    487.5K
# Total Submissions: 1.7M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
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
        carry = 0
        res = p = ListNode(0)
        while l1 is not None or l2 is not None:
            p.next = ListNode(0)
            s = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry
            p.next.val = s%10
            carry = s//10
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
            p=p.next
        if carry:
            p.next = ListNode(0)
            p.next.val = carry
        return res.next
