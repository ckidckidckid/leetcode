#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.80%)
# Total Accepted:    157K
# Total Submissions: 608.4K
# Testcase Example:  '{}'
#
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
#
#
# Return a deep copy of the list.
#
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        root = RandomListNode(head.label)
        visited = {head : root}
        while head:
            cp = visited[head]
            if head.next:
                if head.next not in visited:
                    new_next_node = RandomListNode(head.next.label)
                    visited[head.next] = new_next_node
                cp.next = visited[head.next]
            if head.random:
                if head.random not in visited:
                    new_random_node = RandomListNode(head.random.label)
                    visited[head.random] = new_random_node
                cp.random = visited[head.random]
            head = head.next
        return root
