#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (24.98%)
# Total Accepted:    82.3K
# Total Submissions: 329.2K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
#
#
#
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # =====================================================================
        # Trying iterative version
        # https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space./112629
        # =====================================================================
        n = len(s)
        dp = [x for x in range(n)]

        for i in range(n):
            st, en = i,i
            while st >= 0 and en < n and s[st] == s[en]:
                dp[en] = min(dp[en], 1 + dp[st-1] if st > 0 else 0)
                st-=1
                en+=1

            st, en = i-1,i
            while st >= 0 and en < n and s[st] == s[en]:
                dp[en] = min(dp[en], 1 + dp[st-1] if st > 0 else 0)
                st-=1
                en+=1

        return dp[n-1]

        # =====================================================================
        # Recursive O(n^2) space ;; slower than iteratie version. beats only 9%
        # =====================================================================
        # def helper(st):
        #     if st in table:
        #         return table[st]
        #     ans = float('inf')
        #     if len(st) <= 1 or st == st[::-1]:
        #         ans = 0
        #     else:
        #         n = len(st)
        #         for i in range(n):
        #             head = st[:i+1]
        #             if head == head[::-1]:
        #                 ans = min(ans, 1 + helper(st[i+1:]))
        #     table[st] = ans
        #     return ans
        # table = {}
        # return helper(s)
