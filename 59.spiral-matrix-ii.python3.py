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

        current_dir = 'r'
        next_pos = {
            'r' : lambda x,y: (x,y+1),
            'd' : lambda x,y: (x+1,y),
            'l' : lambda x,y: (x,y-1),
            'u' : lambda x,y: (x-1,y),
        }

        change_dir = {
            'r' : lambda x,y: (x,y+1),
            'd' : lambda x,y: (x+1,y),
            'l' : lambda x,y: (x,y-1),
            'u' : lambda x,y: (x-1,y),
        }

        matrix = [[-1 for _ in range(n)] for _ in range(n)]
        i=j=0
        c=1
        while c <= n*n:
            matrix[i][j] = c
            c+=1
            if current_dir=='r' and (j==n-1 or matrix[i][j+1] != -1):
                current_dir = 'd'
            elif current_dir=='d' and (i==n-1 or matrix[i+1][j] != -1):
                current_dir = 'l'
            elif current_dir=='l' and (j==0 or matrix[i][j-1] != -1):
                current_dir = 'u'
            elif current_dir=='u' and (i==0 or matrix[i-1][j] != -1):
                current_dir = 'r'
            i,j = next_pos[current_dir](i, j)
        return matrix
