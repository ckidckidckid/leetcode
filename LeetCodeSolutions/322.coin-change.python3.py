#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (26.61%)
# Total Accepted:    95.5K
# Total Submissions: 358.9K
# Testcase Example:  '[1]\n0'
#
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
#
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
#
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        table = [False] * (amount+1)
        ans = 0
        curr_values = [0]
        new_values = []
        while curr_values:
            ans += 1
            for v in curr_values:
                for c in coins:
                    nv = v + c
                    if nv == amount:
                        return ans
                    elif nv > amount:
                        continue
                    elif not table[nv]:
                        table[nv] = True
                        new_values.append(nv)
            curr_values, new_values = new_values, []
        return -1
