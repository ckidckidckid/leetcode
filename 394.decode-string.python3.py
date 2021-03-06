#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (42.18%)
# Total Accepted:    60.1K
# Total Submissions: 142.6K
# Testcase Example:  '"3[a]2[bc]"'
#
#
# Given an encoded string, return it's decoded string.
#
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
#
#
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
#
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
#
#
#
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Easy explanation at
        # https://leetcode.com/problems/decode-string/discuss/87563/Share-my-Python-Stack-Simple-Solution-(Easy-to-understand)
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

        st = [['', 1]]
        nums = ''
        for c in s:
            if c.isdigit():
                nums+=c
            elif c == '[':
                st.append(['', int(nums)])
                nums = ''
            elif c == ']':
                ss, cnt = st.pop()
                st[-1][0] += ss*cnt
            else:
                st[-1][0] += c
        ans, _ = st.pop()
        return ans
