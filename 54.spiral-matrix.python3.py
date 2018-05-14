#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (27.43%)
# Total Accepted:    144.4K
# Total Submissions: 526.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not any(matrix):
            return []

        m = len(matrix)
        n = len(matrix[0])
        next_pos = {
            'r' : lambda x,y: (x,y+1),
            'd' : lambda x,y: (x+1,y),
            'l' : lambda x,y: (x,y-1),
            'u' : lambda x,y: (x-1,y),
        }

        should_change_dir = {
            'r' : lambda x,y,matrix: y==n-1 or matrix[x][y+1] is None,
            'd' : lambda x,y,matrix: x==m-1 or matrix[x+1][y] is None,
            'l' : lambda x,y,matrix: y==n-1 or matrix[x][y-1] is None,
            'u' : lambda x,y,matrix: x==m-1 or matrix[x-1][y] is None
        }

        next_state = {'r':'d', 'd':'l', 'l':'u', 'u':'r'}

        current_dir = 'r'

        i=j=0
        c=1
        ans = []
        while c <= m*n:
            ans.append(matrix[i][j])
            matrix[i][j] = None
            c+=1
            if should_change_dir[current_dir](i,j,matrix):
                current_dir = next_state[current_dir]
            i,j = next_pos[current_dir](i, j)
        return ans
