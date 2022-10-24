#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.20%)
# Total Accepted:    93.9K
# Total Submissions: 617.5K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
# Example 2:
#
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#
#
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # O(n^2) solution ; explained at
        # https://leetcode.com/problems/max-points-on-a-line/discuss/47124/16ms28ms-C++-Solutions-with-Explanations

        def gcd(x,y):
            if y==0:
                return x
            else:
                return gcd(y, x%y)

        ans = 0
        n = len(points)
        for i in range(n):
            slopes_from_i = {}
            co_incident_with_i = 0
            for j in range(i+1, n):
                if points[i].x==points[j].x and points[i].y == points[j].y:
                    co_incident_with_i+=1
                elif points[i].x == points[j].x:
                    slopes_from_i[(0,0)] = 1 + slopes_from_i.get((0,0), 0)
                else:
                    dy = points[j].y - points[i].y
                    dx = points[j].x - points[i].x
                    g = gcd(dy, dx)
                    key = (dy//g, dx//g)
                    slopes_from_i[key] = 1 + slopes_from_i.get(key, 0)
            this_ans = max(slopes_from_i.values() or [0]) + co_incident_with_i + 1
            ans = max(ans, this_ans)
        return ans
