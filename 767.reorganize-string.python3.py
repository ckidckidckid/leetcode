#
# [778] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (35.95%)
# Total Accepted:    6.3K
# Total Submissions: 17.4K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty
# string.
#
# Example 1:
#
#
# Input: S = "aab"
# Output: "aba"
#
#
# Example 2:
#
#
# Input: S = "aaab"
# Output: ""
#
#
# Note:
#
#
# S will consist of lowercase letters and have length in range [1, 500].
#
#
#
#
import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Priority Queue with One element skip
        # i.e we append the previously popped element from PQ rather than current element
        # This ensures that no two same elements are added consecutively
        
        ctr = Counter(S)
        pq = [(-v, k) for k,v in ctr.items()]
        heapq.heapify(pq)
        ans = ''
        p_char, p_cnt = '', 0
        while pq:
            cnt, char = heapq.heappop(pq)
            cnt *= -1
            ans += char
            if p_cnt > 1:
                heapq.heappush(pq, (-(p_cnt-1), p_char))
            p_char, p_cnt = char, cnt
        return ans if len(ans) == len(S) else ''
