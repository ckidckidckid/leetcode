#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (41.31%)
# Total Accepted:    101.9K
# Total Submissions: 246.6K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
#
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        next_pos = {
            'r' : lambda x,y: (x,y+1),
            'd' : lambda x,y: (x+1,y),
            'l' : lambda x,y: (x,y-1),
            'u' : lambda x,y: (x-1,y),
        }

        should_change_dir = {
            'r' : lambda x,y,matrix: y==n-1 or matrix[x][y+1] != -1,
            'd' : lambda x,y,matrix: x==n-1 or matrix[x+1][y] != -1,
            'l' : lambda x,y,matrix: y==n-1 or matrix[x][y-1] != -1,
            'u' : lambda x,y,matrix: x==n-1 or matrix[x-1][y] != -1
        }

        next_state = {'r':'d', 'd':'l', 'l':'u', 'u':'r'}

        current_dir = 'r'
        matrix = [[-1 for _ in range(n)] for _ in range(n)]

        i=j=0
        c=1
        while c <= n*n:
            matrix[i][j] = c
            c+=1
            if should_change_dir[current_dir](i,j,matrix):
                current_dir = next_state[current_dir]
            i,j = next_pos[current_dir](i, j)
        return matrix
