#
# [807] Custom Sort String
#
# https://leetcode.com/problems/custom-sort-string/description/
#
# algorithms
# Medium (59.92%)
# Total Accepted:    9K
# Total Submissions: 15K
# Testcase Example:  '"cba"\n"abcd"'
#
# S and T are strings composed of lowercase letters. In S, no letter occurs
# more than once.
#
# S was sorted in some custom order previously. We want to permute the
# characters of T so that they match the order that S was sorted. More
# specifically, if x occurs before y in S, then x should occur before y in the
# returned string.
#
# Return any permutation of T (as a string) that satisfies this property.
#
#
# Example :
# Input:
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b",
# and "a".
# Since "d" does not appear in S, it can be at any position in T. "dcba",
# "cdba", "cbda" are also valid outputs.
#
#
#
#
# Note:
#
#
# S has length at most 26, and no character is repeated in S.
# T has length at most 200.
# S and T consist of lowercase letters only.
#
#
#
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        table = [0]*26
        for c in T:
            table[ord(c) - ord('a')] += 1
        ans = ''
        for c in S:
            diff = ord(c) - ord('a')
            cnt = table[diff]
            ans += chr(ord('a')+diff)*cnt
            table[diff] = 0
        for i,v in enumerate(table):
            ans += chr(ord('a')+i)*v
        return ans
