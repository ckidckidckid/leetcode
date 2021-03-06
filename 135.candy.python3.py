#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (25.38%)
# Total Accepted:    78.9K
# Total Submissions: 310.7K
# Testcase Example:  '[1,0,2]'
#
# There are N children standing in a line. Each child is assigned a rating
# value.
#
# You are giving candies to these children subjected to the following
# requirements:
#
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
#
# What is the minimum candies you must give?
#
# Example 1:
#
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
#
#
# Example 2:
#
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# ⁠            The third child gets 1 candy because it satisfies the above two
# conditions.
#
#
#
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # ============================================================
        # Even better  O(n) time, O(1) space, one pass solution
        # https://leetcode.com/problems/candy/discuss/42795/Two-C++-solutions-given-with-explanation-(both-with-O(N)-time-one-with-O(1)-space-the-other-with-O(N)-space)
        # https://leetcode.com/problems/candy/discuss/42770/One-pass-constant-space-Java-solution
        # ============================================================


        # ============================================================
        # O(n) time , O(n) space solution;
        # idea from https://leetcode.com/problems/candy/discuss/42794/Simple-O(n)-Java-solution-with-comments
        # ============================================================

        n = len(ratings)
        table = [1]*n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                table[i] = max(table[i], table[i-1]+1)
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                table[i] = max(table[i], table[i+1]+1)
        return sum(table)

        # ============================================================
        # O(nlog(n)) solution; Accepted; but not very fast; beats 19%
        # ============================================================

        # inp = [(r,i) for i,r in enumerate(ratings)]
        # inp.sort()
        # n = len(ratings)
        # table = [1]*n
        # for (r,i) in inp:
        #     if i>0 and r > ratings[i-1]:
        #         table[i] = max(table[i], table[i-1]+1)
        #     if i<n-1 and r > ratings[i+1]:
        #         table[i] = max(table[i], table[i+1]+1)
        # return sum(table)
