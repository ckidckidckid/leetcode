#
# [165] Compare Version Numbers
#
# https://leetcode.com/problems/compare-version-numbers/description/
#
# algorithms
# Medium (20.93%)
# Total Accepted:    101.2K
# Total Submissions: 483.2K
# Testcase Example:  '"0.1"\n"1.1"'
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise
# return 0.
#
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
#
# Example 1:
#
#
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
#
# Example 2:
#
#
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
#
# Example 3:
#
#
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1
#
#
class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        n1 = len(v1)
        n2 = len(v2)
        v1 += '0'*(max(n1,n2) - n1)
        v2 += '0'*(max(n1,n2) - n2)
        for x,y in zip(v1, v2):
            x,y = int(x), int(y)
            if x == y:
                continue
            elif x>y:
                return 1
            else:
                return -1
        return 0
