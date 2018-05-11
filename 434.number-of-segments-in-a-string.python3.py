#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (36.57%)
# Total Accepted:    38.6K
# Total Submissions: 105.7K
# Testcase Example:  '"Hello, my name is John"'
#
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5
#
#
#
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = -1
        ans = 0
        for c in s:
            if c!= ' ':
                if st == -1:
                    st = 1
                    ans += 1
            else:
                if st != -1:
                    st = -1
        return ans
