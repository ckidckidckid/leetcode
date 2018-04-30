#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (33.51%)
# Total Accepted:    103.6K
# Total Submissions: 309.2K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# ⁠Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
#
# Examples:
#
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
#
#
#
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
#
#
# Credits:Special thanks to @minglotus6 for adding this problem and creating
# all test cases.
#
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ps = {}
        sp = {}
        p = list(pattern)
        s = str.split(' ')
        if len(p) != len(s):
            return False
        for (x,y) in zip(p, s):
            if x in ps:
                if ps[x] != y:
                    return False
            else:
                ps[x] = y

            if y in sp:
                if sp[y] != x:
                    return False
            else:
                sp[y] = x
        return True
