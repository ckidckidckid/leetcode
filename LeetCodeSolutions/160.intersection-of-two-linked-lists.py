#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (30.87%)
# Total Accepted:    190.1K
# Total Submissions: 616.1K
# Testcase Example:  'No intersection: []\n[]'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
#
# For example, the following two linked lists:
#
# A:          a1 → a2
# ⁠                  ↘
# ⁠                    c1 → c2 → c3
# ⁠                  ↗
# B:     b1 → b2 → b3
#
# begin to intersect at node c1.
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
#
#
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hA = headA
        hB = headB
        a = b = 0
        if hA is None or hB is None:
            return None
        while hA.next is not None and hB.next is not None:
            hA = hA.next
            hB = hB.next
        if hA.next is None:
            while hB.next is not None:
                b+=1
                hB = hB.next
        elif hB.next is None:
            while hA.next is not None:
                a+=1
                hA = hA.next
        if hA is not hB:
            return None
        while a > 0:
            a -= 1
            headA = headA.next
        while b > 0:
            b -= 1
            headB = headB.next
        while headA is not None:
            if headA is headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
