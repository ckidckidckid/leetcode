#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (32.11%)
# Total Accepted:    199.3K
# Total Submissions: 620.6K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
#
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        intervals.sort(key = lambda x : x.start)
        s,e = intervals[0].start, intervals[0].end
        res = []
        for interval in intervals[1:]:
            sn = interval.start
            en = interval.end
            if sn>e:
                res.append(Interval(s,e))
                s=sn
                e = en
            e = max(e,en)
            # for i in res:
            #     print(i.start, i.end, end = '..')
            # print('')
        res.append(Interval(s,e))
        return res
