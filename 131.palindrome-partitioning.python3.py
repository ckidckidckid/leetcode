#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (35.96%)
# Total Accepted:    121.5K
# Total Submissions: 337.7K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
#
#
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        def helper(st, curr):
            if st is None or len(st) == 0:
                ans.append(curr[:])
            else:
                for i in range(len(st)):
                    substring = st[:i+1]
                    if substring == substring[::-1]:
                        curr.append(substring)
                        helper(st[i+1:], curr)
                        curr.pop()
        helper(s, [])
        return ans
