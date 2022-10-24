#
# [822] Unique Morse Code Words
#
# https://leetcode.com/problems/unique-morse-code-words/description/
#
# algorithms
# Easy (74.57%)
# Total Accepted:    13.1K
# Total Submissions: 17.5K
# Testcase Example:  '["gin", "zen", "gig", "msg"]'
#
# International Morse Code defines a standard encoding where each letter is
# mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps
# to "-...", "c" maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet is
# given below:
#
#
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#
# Now, given a list of words, each word can be written as a concatenation of
# the Morse code of each letter. For example, "cab" can be written as
# "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call
# such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.
#
#
# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation:
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# There are 2 different transformations, "--...-." and "--...--.".
#
#
#
#
# Note:
#
#
# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# ⁠   words[i] will only consist of lowercase letters.
#
#
#
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique_codes = set()
        for word in words:
            m_word = ''.join([code[ord(c)-ord('a')] for c in word])
            unique_codes.add(m_word)
        return len(unique_codes)
