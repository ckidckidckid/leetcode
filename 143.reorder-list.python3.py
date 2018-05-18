#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (26.97%)
# Total Accepted:    112.9K
# Total Submissions: 418.1K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
# Example 1:
#
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
#
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        def printll(node):
            while node:
                print("{}-->".format(node.val), end='')
                node=node.next
            print("null")
        def reverse(node):
            if node is None:
                return None
            if node.next is None:
                return node
            n1 = node.next
            node.next = None
            ans = reverse(n1)
            n1.next = node
            return ans
        if not head:
            return head
        n = 1
        th = head
        while th:
            n+=1
            th = th.next
        l1 = th = head

        n = n//2 + int(n%2)
        for i in range(n-1):
            th = th.next
        l2 = th.next
        th.next = None
        l2 = reverse(l2)
        ptr = l1
        printll(l1)
        printll(l2)
        while l2:
            l1 = l1.next
            ptr.next = l2
            l2 = l2.next
            ptr = ptr.next
            ptr.next = l1
            ptr = ptr.next
