#
# [815] Champagne Tower
#
# https://leetcode.com/problems/champagne-tower/description/
#
# algorithms
# Medium (29.34%)
# Total Accepted:    3.4K
# Total Submissions: 11.7K
# Testcase Example:  '1\n1\n1'
#
# We stack glasses in a pyramid, where the first row has 1 glass, the second
# row has 2 glasses, and so on until the 100th row.  Each glass holds one cup
# (250ml) of champagne.
#
# Then, some champagne is poured in the first glass at the top.  When the top
# most glass is full, any excess liquid poured will fall equally to the glass
# immediately to the left and right of it.  When those glasses become full, any
# excess champagne will fall equally to the left and right of those glasses,
# and so on.  (A glass at the bottom row has it's excess champagne fall on the
# floor.)
#
# For example, after one cup of champagne is poured, the top most glass is
# full.  After two cups of champagne are poured, the two glasses on the second
# row are half full.  After three cups of champagne are poured, those two cups
# become full - there are 3 full glasses total now.  After four cups of
# champagne are poured, the third row has the middle glass half full, and the
# two outside glasses are a quarter full, as pictured below.
#
#
#
# Now after pouring some non-negative integer cups of champagne, return how
# full the j-th glass in the i-th row is (both i and j are 0 indexed.)
#
#
#
#
# Example 1:
# Input: poured = 1, query_glass = 1, query_row = 1
# Output: 0.0
# Explanation: We poured 1 cup of champange to the top glass of the tower
# (which is indexed as (0, 0)). There will be no excess liquid so all the
# glasses under the top glass will remain empty.
#
# Example 2:
# Input: poured = 2, query_glass = 1, query_row = 1
# Output: 0.5
# Explanation: We poured 2 cups of champange to the top glass of the tower
# (which is indexed as (0, 0)). There is one cup of excess liquid. The glass
# indexed as (1, 0) and the glass indexed as (1, 1) will share the excess
# liquid equally, and each will get half cup of champange.
#
#
#
#
# Note:
#
#
# poured will be in the range of [0, 10 ^ 9].
# query_glass and query_row will be in the range of [0, 99].
#
#
#
#
#
class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        # =====================================================================
        # O(mn) space and time; Accpeted because it is iterative
        # =====================================================================

        n = query_row+1
        grid = [[[0,0] for _ in range(i)] for i in range(1,n+2)]
        grid[0][0] = [0,poured]
        for i in range(n):
            for j in range(i+1):
                fil,bal = grid[i][j]
                n_fil = min(1, fil + bal)
                grid[i][j][0] = n_fil
                if i==query_row and j==query_glass:
                    return n_fil
                bal -= n_fil - fil
                grid[i+1][j+1][1] += bal/2
                grid[i+1][j][1] += bal/2
        return grid[query_row][query_glass][0]

        # =====================================================================
        # Recursive Call ; O(mn) space and time; Times out (mostly because it is recursive)
        # =====================================================================

        # def dist(i,j, bal):
        #     if bal>0:
        #         orig = grid[i][j]
        #         grid[i][j] = min(1.0,bal + grid[i][j])
        #         bal -= grid[i][j] - orig
        #         if i==query_row:
        #             return
        #         dist(i+1, j, bal/2)
        #         dist(i+1, j+1, bal/2)
        #
        # n = query_row+1
        # grid = [[0.0 for _ in range(i)] for i in range(1,n+1)]
        # dist(0,0,poured)
        # return grid[query_row][query_glass]
