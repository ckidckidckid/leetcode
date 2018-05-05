#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (28.55%)
# Total Accepted:    103.8K
# Total Submissions: 363.3K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
#
# Example:
#
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
#
#
#
class Solution:
    def restoreIpAddresses(self, s, fields = 4):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        if fields == 0 or s is None or len(s)<fields or len(s)>3*fields:
            return ans
        def safecheck(x,s):
            return x>=0 and x<=255 and ((x<10 and len(s) == 1) or s[0] != '0')

        if fields == 1:
            val = int(s)
            if safecheck(val,s):
                ans.append(s)
        else:
            for i in range(1,4):
                subs = self.restoreIpAddresses(s[i:], fields-1)
                for sub in subs:
                    val = s[0:i]
                    ival = int(val)
                    if safecheck(ival, val):
                        ans.append( val + "." + sub)
        return ans
