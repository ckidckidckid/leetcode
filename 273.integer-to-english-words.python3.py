#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (22.83%)
# Total Accepted:    60.4K
# Total Submissions: 264.6K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
#
# Input: 123
# Output: "One Hundred Twenty Three"
#
#
# Example 2:
#
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
#
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
#
#
#
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        words = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        words_skip = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        word_tens = ['','-','Twenty', 'Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        word_dec = ['','Thousand', 'Million', 'Billion']

        def three_dig_helper(p):
            p = int(p)
            uni = p%10
            ten = (p//10)%10
            hun = (p//100)%10
            ans = []
            if hun>0:
                ans.append(words[hun])
                ans.append('Hundred')
            if ten==1:
                ans.append(words_skip[uni])
            else:
                if ten>0:
                    ans.append(word_tens[ten])
                if uni>0:
                    ans.append(words[uni])
            return ' '.join(ans)

        ss = format(num, ',').split(',')[::-1]
        ans = []
        for i,sub in enumerate(ss):
            next = three_dig_helper(sub)
            if next:
                if i>0:ans.append(word_dec[i])
                ans.append(next)
        ans = ans[::-1]
        ans_str = ' '.join(ans) or 'Zero'
        return ans_str
