#
# [768] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (64.61%)
# Total Accepted:    14.1K
# Total Submissions: 21.9K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
#
# A string S of lowercase letters is given.  We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.
#
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
#
#
#
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
#
#
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        table = [0]*26
        for idx, c in enumerate(S):
            table[ord(c)-ord('a')] = idx
        i = j = 0
        st = -1
        ans = []
        while i<len(S):
            j = max(j, table[ord(S[i])-ord('a')])
            if j==i:
                ans.append(j-st)
                st=j
            i+=1
        return ans
