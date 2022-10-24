#
# [777] Toeplitz Matrix
#
# https://leetcode.com/problems/toeplitz-matrix/description/
#
# algorithms
# Easy (57.61%)
# Total Accepted:    18.8K
# Total Submissions: 32.6K
# Testcase Example:  '[[1,2,3,4],[5,1,2,3],[9,5,1,2]]'
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
# same element.
#
# Now given an M x N matrix, return True if and only if the matrix is
# Toeplitz.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: True
# Explanation:
# 1234
# 5123
# 9512
#
# In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2,
# 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the
# answer is True.
#
#
# Example 2:
#
#
# Input: matrix = [[1,2],[2,2]]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.
#
#
# Note:
#
#
# matrix will be a 2D array of integers.
# matrix will have a number of rows and columns in range [1, 20].
# matrix[i][j] will be integers in range [0, 99].
#
#
#
#
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            se = matrix[i][0]
            x,y=i,0
            while True:
                if x==m or y==n:
                    break
                if matrix[x][y] != se:
                    return False
                x+=1
                y+=1

        for i in range(n):
            se = matrix[0][i]
            x,y=0,i
            while True:
                if x==m or y==n:
                    break
                if matrix[x][y] != se:
                    return False
                x+=1
                y+=1
                
        return True
