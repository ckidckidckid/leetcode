#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (33.77%)
# Total Accepted:    97.3K
# Total Submissions: 288.2K
# Testcase Example:  '[]'
#
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
#
#
#
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
#
#
#
# For example, given citations = [3, 0, 6, 1, 5], which means the researcher
# has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations
# respectively. Since the researcher has 3 papers with at least 3 citations
# each and the remaining two with no more than 3 citations each, his h-index is
# 3.
#
#
#
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # O(nlog(n)) solution | about 40 ms / 63.3%
        # citations.sort(reverse=True)
        # for i,val in enumerate(citations):
        #     if citations[i] < i+1:
        #         return i
        # return len(citations)

        # O(n) with O(n) space solution; from
        # leetcode.com/problems/h-index/discuss/70810/A-Clean-O(N)-Solution-in-Java/73014

        n = len(citations)
        citation_counts = [0 for _ in range(n+1)]
        for c in citations:
            citation_counts[min(n, c)]+=1
        total = 0
        for i in range(n, -1, -1):
            total += citation_counts[i]
            if total >= i:
                return i
        return 0
