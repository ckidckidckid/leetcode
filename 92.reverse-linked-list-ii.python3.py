#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (31.48%)
# Total Accepted:    138.7K
# Total Submissions: 440.7K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
def printn(node):
    print("---------")
    while node is not None:
        print(node.val)
        node = node.next
        
class Solution:
    def reverse(self, head):
        if head is None:
            return (None, None)
        if head.next is None:
            return (head, head)
        n = head.next
        head.next = None
        nh,nt = self.reverse(n)
        nt.next = head
        return (nh, head)
        
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        p1 = dummy
        curr = dummy

        for _ in range(m):
            p1 = curr
            curr = curr.next
        
        p2=curr
        for j in range(n-m+1):
            p2=curr
            curr=curr.next

        # printn(dummy)
        s = p1.next
        
        p1.next = None
        p2.next = None
        # printn(dummy)

        h, t = self.reverse(s)
        # printn(h)
        p1.next = h
        t.next = curr 
        return dummy.next
