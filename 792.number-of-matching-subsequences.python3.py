#
# [808] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (36.12%)
# Total Accepted:    6.1K
# Total Submissions: 16.9K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
#
#
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
#
#
# Note:
#
#
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
#
#
from bisect import bisect_left
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # O(nwlog(s)) solution ==> w : avg length of word
        # Credits to https://leetcode.com/problems/number-of-matching-subsequences/discuss/117578/Simple-Python-solution
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        table = {}
        for i,c in enumerate(S):
            if c not in table:
                table[c] = []
            table[c].append(i)
        ans = 0
        for word in words:
            match  = 0
            covered = 0
            for c in word:
                if c not in table:
                    break
                idx = bisect_left(table[c], covered)
                if idx >= len(table[c]):
                    break
                covered = table[c][idx]+1
                match+=1
            if match == len(word):
                ans +=1
        return ans

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # O(ns) where n-> number of words, s -> length of S
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # def isSubsequence(ss):
        #     n = len(ss)
        #     if n>len(S):
        #         return False
        #     if n ==0:
        #         return True
        #     i=0
        #     for c in S:
        #         if ss[i] == c:
        #             i+=1
        #         if i==n:
        #             return True
        #     return False
        #
        # ans = [x for x in words if isSubsequence(x)]
        # return len(ans)
