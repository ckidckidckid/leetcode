#
# [757] Pyramid Transition Matrix
#
# https://leetcode.com/problems/pyramid-transition-matrix/description/
#
# algorithms
# Medium (46.02%)
# Total Accepted:    4.8K
# Total Submissions: 10.5K
# Testcase Example:  '"ABC"\n["ABD","BCE","DEF","FFF"]'
#
#
# We are stacking blocks to form a pyramid.  Each block has a color which is a
# one letter string, like `'Z'`.
#
# For every block of color `C` we place not in the bottom row, we are placing
# it on top of a left block of color `A` and right block of color `B`.  We are
# allowed to place the block there only if `(A, B, C)` is an allowed triple.
#
# We start with a bottom row of bottom, represented as a single string.  We
# also start with a list of allowed triples allowed.  Each allowed triple is
# represented as a string of length 3.
#
# Return true if we can build the pyramid all the way to the top, otherwise
# false.
#
#
# Example 1:
#
# Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
# ⁠   A
# ⁠  / \
# ⁠ D   E
# ⁠/ \ / \
# X   Y   Z
#
# This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are
# allowed triples.
#
#
#
# Example 2:
#
# Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C !=
# D.
#
#
#
# Note:
#
# bottom will be a string with length in range [2, 8].
# allowed will have length in range [0, 200].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E',
# 'F', 'G'}.
#
#
#
from collections import deque


class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """

        def genereate_combinations(arr):
            if len(arr) <= 1:
                return arr[0]
            last = arr.pop()
            second_last = arr.pop()
            arr.append([x + y for x in second_last for y in last])
            return genereate_combinations(arr)

        table = {}
        for a in allowed:
            key, value = ''.join(a[:2]), a[-1]
            if key not in table:
                table[key] = []
            table[key].append(value)
        if len(bottom) == 1:
            return True
        q = [bottom]
        seen = {bottom}
        while q:
            s = q.pop()
            ns = []
            for i in range(1, len(s)):
                rep = ''.join(s[i - 1:i + 1])
                if rep in table:
                    ns.append(table[rep])
                else:
                    break
            else:
                nss = genereate_combinations(ns)
                for ss in nss:
                    if len(ss) == 1:
                        return True
                    elif ss not in seen:
                        seen.add(ss)
                        q.append(ss)
        return False
