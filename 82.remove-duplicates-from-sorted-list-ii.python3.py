#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (30.09%)
# Total Accepted:    135.4K
# Total Submissions: 449.8K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = sentinel = ListNode(None)
        sentinel.next = head

        while head and head.next:
            if head.val != head.next.val:
                prev = head
            else:
                while head.next and head.val == head.next.val:
                    head=head.next
                prev.next = head.next
            head = head.next

        return sentinel.next
