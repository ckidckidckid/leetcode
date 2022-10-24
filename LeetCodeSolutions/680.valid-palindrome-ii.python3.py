#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (32.29%)
# Total Accepted:    30.8K
# Total Submissions: 95.3K
# Testcase Example:  '"aba"'
#
#
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
#
#
# Example 1:
#
# Input: "aba"
# Output: True
#
#
#
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
#
#
# Note:
#
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
#
#
#
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Trying O(n) two pointer method
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        n = len(s)
        i,j=0,n-1
        while i<=j:
            if s[i] != s[j]:
                t1 = s[i+1:j+1]
                t2 = s[i:j]
                return t1 == t1[::-1] or t2 == t2[::-1]
            else:
                i+=1
                j-=1
        return True

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Brute Force O(n^2) times out
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # n = len(s)
        # for i in range(n):
        #     ss = s[:i]+s[i+1:]
        #     if ss == ss[::-1]:
        #         return True
        # return False
