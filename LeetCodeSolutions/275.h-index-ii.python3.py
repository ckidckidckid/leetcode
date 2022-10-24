#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (34.93%)
# Total Accepted:    62.4K
# Total Submissions: 178.7K
# Testcase Example:  '[]'
#
#
# Follow up for H-Index: What if the citations array is sorted in ascending
# order? Could you optimize your algorithm?
#
#
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        rc = [c for c in citations[::-1] if c > 0]
        for i,val in enumerate(rc):
            if rc[i] < i+1:
                return i
        return len(rc)
