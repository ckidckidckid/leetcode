#
# [793] Swap Adjacent in LR String
#
# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (28.69%)
# Total Accepted:    4.1K
# Total Submissions: 14.3K
# Testcase Example:  '"X"\n"L"'
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a
# move consists of either replacing one occurrence of "XL" with "LX", or
# replacing one occurrence of "RX" with "XR". Given the starting string start
# and the ending string end, return True if and only if there exists a sequence
# of moves to transform one string to the other.
#
# Example:
#
#
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#
#
# Note:
#
#
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.
#
#
class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Coutning Method O(n) time; O(1) space
        # Idea from https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/113788/Simple-Python-(1-Scan-O(1)-space)
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        rc = lc = 0
        if len(start) != len(end) or start.replace('X', '') != end.replace('X', ''):
            return False

        for c1, c2 in zip(start, end):
            if c1=='R': rc+=1
            elif c1=='L': lc+=1
            if c2=='R': rc-=1
            elif c2=='L': lc-=1
            if rc<0 or lc>0:
                return False
        return True

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # BFS Solution ; Times out
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # def transforms(s, src, dest):
        #     ans = []
        #     splits = s.split(src)
        #     n = len(splits)
        #     for i in range(1, n):
        #         head = src.join(splits[:i])
        #         tail = src.join(splits[i:])
        #         ans.append(head + dest + tail)
        #     return ans
        #
        # def bfs(s):
        #     children = transforms(s, 'XL', 'LX') + transforms(s, 'RX', 'XR')
        #     for child in children:
        #         if child not in visited:
        #             visited.add(child)
        #             if child == end:
        #                 return True
        #             if bfs(child):
        #                 return True
        #     return False
        #
        # if len(start) != len(end):
        #     return False
        # if start==end:
        #     return True
        # visited = {set}
        # return bfs(start)
