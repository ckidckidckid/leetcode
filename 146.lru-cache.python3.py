#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Hard (20.09%)
# Total Accepted:    176.4K
# Total Submissions: 876.6K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
#
#
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
#
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#
#
class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def print_fwd(self):
        n = self.head
        while n:
            print(n.val, '==>', end='')
            n = n.next
        print('None')

    def print_bkd(self):
        n = self.tail
        while n:
            print(n.val, '==>', end='')
            n = n.prev
        print('None')

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity+2
        self.size = 2
        self.table = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("get", key, '~~>', end='')
        if key not in self.table:
            return -1
        node = self.table[key]
        t_prev = node.prev
        t_next = node.next
        t_prev.next = node.next
        t_next.prev = node.prev

        oh = self.head.next
        node.prev = self.head
        node.next = oh
        oh.prev = node
        self.head.next = node

        # print(node.val)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print("put", key, value)
        # self.print_bkd()
        # self.print_fwd()
        node = Node(key, value)
        if key in self.table:
            e_node = self.table[key]
            # print("override ", e_node.val)
            t_prev = e_node.prev
            t_next = e_node.next
            t_prev.next = e_node.next
            t_next.prev = e_node.prev
            # e_node.next.prev, e_node.prev.next = e_node.prev, e_node.next
            self.size -= 1
        self.table[key] = node

        oh = self.head.next
        node.prev = self.head
        node.next = oh
        self.head.next = node
        oh.prev = node

        self.size += 1
        if self.size > self.capacity:
            to_del_node = self.tail.prev
            # print("eviction ", to_del_node.val, to_del_node.next.val, to_del_node.prev.val)
            t_prev = to_del_node.prev
            t_next = to_del_node.next
            t_prev.next = to_del_node.next
            t_next.prev = to_del_node.prev
            # print("--", self.tail.prev.val)
            del self.table[to_del_node.key]
            self.size-=1





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
