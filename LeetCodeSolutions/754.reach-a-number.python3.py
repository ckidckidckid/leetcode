#
# [755] Reach a Number
#
# https://leetcode.com/problems/reach-a-number/description/
#
# algorithms
# Medium (27.45%)
# Total Accepted:    3.7K
# Total Submissions: 13.5K
# Testcase Example:  '1'
#
#
# You are standing at position 0 on an infinite number line.  There is a goal
# at position target.
#
# On each move, you can either go left or right.  During the n-th move
# (starting from 1), you take n steps.
#
# Return the minimum number of steps required to reach the destination.
#
#
# Example 1:
#
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
#
#
#
# Example 2:
#
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.
#
#
#
# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].
#
#
class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # There exists a O(1) solution too :(  . .
        # The below solution is O(n); Original Idea
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        reach = 1
        target = abs(target)
        for i in range(1,target+2):
            if reach%2==target%2 and target<=reach:
                return i
            else:
                reach += (i+1)
        return -1
