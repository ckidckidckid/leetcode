#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (34.62%)
# Total Accepted:    159.4K
# Total Submissions: 460.3K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Example 1:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#
#
# Example 2:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
#
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not any(matrix):
            return False

        m=len(matrix)
        n=len(matrix[0])

        lo = 0
        hi = m*n-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                lo=mid+1
            else:
                hi=mid-1
        return False
