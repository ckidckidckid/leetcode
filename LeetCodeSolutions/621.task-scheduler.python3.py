#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (42.57%)
# Total Accepted:    40.1K
# Total Submissions: 94.2K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks.Tasks could
# be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing different
# tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
#
# Example 1:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#
#
#
# Note:
#
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
#
#
#
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Idea from
        # https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        ctr = Counter(tasks)
        num_max = 1
        max_val = -float('inf')
        for k in ctr:
            if ctr[k] == max_val:
                num_max+=1
            if ctr[k] > max_val:
                max_val = ctr[k]
                num_max=1
        part_count = max_val - 1
        part_length = n-(num_max-1)
        empty_slots = part_count*part_length
        available_tasks = len(tasks) - num_max*max_val
        idles = max(0, empty_slots-available_tasks)
        ans = len(tasks) + idles
        return ans
