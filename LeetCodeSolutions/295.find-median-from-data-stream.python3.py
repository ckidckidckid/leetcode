#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (30.01%)
# Total Accepted:    61.9K
# Total Submissions: 206.3K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
#
# [2,3,4] , the median is 3 
#
# [2,3], the median is (2 + 3) / 2 = 2.5 
#
# Design a data structure that supports the following two operations:
#
#
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
#
#
# Example:
#
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
#
#
from heapq import heappush, heappushpop

class MedianFinder:

    # ==========================================================================
    # Idea from dietpepsi;s solution at
    # https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find
    # ==========================================================================

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_max = []
        self.large_min = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        l1 = len(self.small_max)
        l2 = len(self.large_min)
        if l1 == l2:
            _,val = heappushpop(self.small_max, (-num, num))
            heappush(self.large_min, (val, val))
        else:
            _,val = heappushpop(self.large_min, (num, num))
            heappush(self.small_max, (-val, val))

    def findMedian(self):
        """
        :rtype: float
        """
        l1 = len(self.small_max)
        l2 = len(self.large_min)
        if l1 == 0 and l2 == 0:
            return None
        if l2 > l1:
            return self.large_min[0][1]*1.0
        else:
            return (self.small_max[0][1] + self.large_min[0][1])/2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
