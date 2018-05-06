#
# [839] Short Encoding of Words
#
# https://leetcode.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (39.77%)
# Total Accepted:    2.6K
# Total Submissions: 6.5K
# Testcase Example:  '["time", "me", "bell"]'
#
# Given a list of words, we may encode it by writing a reference string S and a
# list of indexes A.
#
# For example, if the list of words is ["time", "me", "bell"], we can write it
# as S = "time#bell#" and indexes = [0, 2, 5].
#
# Then for each index, we will recover the word by reading from the reference
# string from that index until we reach a "#" character.
#
# What is the length of the shortest reference string S possible that encodes
# the given words?
#
# Example:
#
#
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
#
#
# Note:
#
#
# 1 <= words.length <= 2000.
# 1 <= words[i].length <= 7.
# Each word has only lowercase letters.
#
#
#
class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = len, reverse = True)
        # words = [word + '#' for word in words]
        s = ''
        for word in words:
            st = word+'#'
            if st not in s:
                s += st
        return(len(s))
