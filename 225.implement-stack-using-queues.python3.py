#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (34.44%)
# Total Accepted:    94.5K
# Total Submissions: 274.1K
# Testcase Example:  '["MyStack","empty"]\n[[],[]]'
#
#
# Implement the following operations of a stack using queues.
#
#
# push(x) -- Push element x onto stack.
#
#
# pop() -- Removes the element on top of the stack.
#
#
# top() -- Get the top element.
#
#
# empty() -- Return whether the stack is empty.
#
#
# Notes:
#
# You must use only standard operations of a queue -- which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may
# simulate a queue by using a list or deque (double-ended queue), as long as
# you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top
# operations will be called on an empty stack).
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# all test cases.
#
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._t = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._t.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._t.pop()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._t[-1]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._t) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
