#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (34.02%)
# Total Accepted:    120.2K
# Total Submissions: 353.2K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list using insertion sort.
#
#
#
#
#
# A graphical example of insertion sort. The partial sorted list (black)
# initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list
#
#
#
#
#
# Algorithm of Insertion Sort:
#
#
# Insertion sort iterates, consuming one input element each repetition, and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it
# there.
# It repeats until no input elements remain.
#
#
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def printll(node):
            while node:
                print("{}==>".format(node.val), end='')
                node=node.next
            print("null")

        dummy = ListNode(-float('inf'))
        to_process = head
        while to_process:
            v = to_process.val
            next_to_process = to_process.next
            to_process.next = None
            ptr = dummy
            # printll(dummy)
            # printll(to_process)
            while ptr.next is not None:
                if v < ptr.next.val:
                    tmp = ptr.next
                    ptr.next = to_process
                    to_process.next = tmp
                    break
                ptr = ptr.next
            else:
                ptr.next = to_process
            to_process = next_to_process
        return dummy.next
