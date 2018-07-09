#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (20.43%)
# Total Accepted:    73.6K
# Total Submissions: 359.6K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right)
# justified.
#
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
#
# Note:
#
#
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
#
#
# Example 1:
#
#
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#
#
# Example 2:
#
#
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be",
# because the last line must be left-justified instead of fully-justified.
# ⁠            Note that the second line is also left-justified becase it
# contains only one word.
#
#
# Example 3:
#
#
# Input:
# words =
# ["Science","is","what","we","understand","well","enough","to","explain",
# "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#
#
#
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        acc = []
        num_in_acc = 0
        ans = []
        for word in words:
            if num_in_acc + len(word) - 1 >= maxWidth:
                num_in_acc -= 1
                extra_spaces = maxWidth - num_in_acc
                uniform_add = (extra_spaces // (len(acc)-1)) if len(acc) > 1 else 0
                non_uniform_add = (extra_spaces % (len(acc)-1)) if len(acc) > 1 else 0
                for j in range(len(acc)-1):
                    acc[j] += ' '*uniform_add + (' ' if non_uniform_add > 0 else '')
                    non_uniform_add-=1
                line = ' '.join(acc)
                line += ' '*(maxWidth - len(line))
                ans.append(line)
                acc = []
                num_in_acc = 0
            acc.append(word)
            num_in_acc += len(word) + 1
        line = ' '.join(acc)
        line += ' '*(maxWidth - len(line))
        ans.append(line)
        return ans
