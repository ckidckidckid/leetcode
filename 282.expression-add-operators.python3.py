#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (30.66%)
# Total Accepted:    47.8K
# Total Submissions: 155.9K
# Testcase Example:  '"123"\n6'
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
#
# Example 1:
#
#
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"]
#
#
# Example 2:
#
#
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
#
# Example 3:
#
#
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
#
# Example 4:
#
#
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
#
#
# Example 5:
#
#
# Input: num = "3456237490", target = 9191
# Output: []
#
#
#
class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def helper(s, acc_str, bal, multi):
            # print('(', s, acc_str, bal, multi, ')')
            if len(s) == 0:
                if multi is not None:
                    bal -= multi
                if bal == 0:
                    ans.add(acc_str[1:])
            else:
                for i in range(len(s)-1, -1, -1):
                    head = s[:i]
                    tail = s[i:]
                    if len(tail) > 1 and tail[0] == '0':
                        continue
                    if multi is None:
                        helper(head, '+' + tail + acc_str, bal - int(tail), None)
                        if len(head) > 0:
                            helper(head, '-' + tail + acc_str, bal + int(tail), None)
                            helper(head, '*' + tail + acc_str, bal, int(tail))
                    else:
                        helper(head, '+' + tail + acc_str, bal - (int(tail)*multi), None)
                        if len(head) > 0:
                            helper(head, '-' + tail + acc_str, bal + (int(tail)*multi), None)
                            helper(head, '*' + tail + acc_str, bal, int(tail)*multi)

            pass

        ans = set()
        helper(num, '', target, None)
        return list(ans)
