#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (18.16%)
# Total Accepted:    64.8K
# Total Submissions: 356.7K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
#
# Example 1:
#
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
#
# Example 2:
#
#
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
#
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
#
#
#
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator*denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        n, rem = divmod(numerator, denominator)
        result = [sign + str(n), '.']
        table = {}
        idx=2
        while rem not in table:
            table[rem] = idx
            idx+=1
            n,rem = divmod(rem*10, denominator)
            result.append(str(n))
        result.insert(table[rem], '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')
