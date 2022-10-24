#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (52.96%)
# Total Accepted:    15K
# Total Submissions: 28.3K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
#
# Given a list of daily temperatures, produce a list that, for each day in the
# input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
#
# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73],
# your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
#
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
#
#
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        st = []
        ans = [0]*n
        for idx in range(n-1, -1, -1):
            t = temperatures[idx]
            while len(st) > 0 and t >= st[-1][0]:
                st.pop()
            ans[idx] = st[-1][1]-idx if len(st)>0 else 0
            st.append((t, idx))
        return ans
