#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (33.70%)
# Total Accepted:    124.1K
# Total Submissions: 368.3K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Single pass O(n) time; O(1) space solution
        dummy_small = ListNode(None)
        dummy_large = ListNode(None)
        s = dummy_small
        l = dummy_large
        while head is not None:
            oh = head
            head = head.next
            if oh.val < x:
                s.next = oh
                s = s.next
            else:
                l.next = oh
                l = l.next
            oh.next = None

        s.next = dummy_large.next
        return dummy_small.next
