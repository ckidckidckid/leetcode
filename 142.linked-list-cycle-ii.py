#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (30.52%)
# Total Accepted:    148.6K
# Total Submissions: 487.1K
# Testcase Example:  '[]\nno cycle'
#
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
#
#
#
# Note: Do not modify the linked list.
#
#
# Follow up:
# Can you solve it without using extra space?
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                break
        if not fast or not fast.next:
            return None
        fast = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
