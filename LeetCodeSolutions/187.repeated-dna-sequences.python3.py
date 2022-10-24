#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (33.19%)
# Total Accepted:    95.8K
# Total Submissions: 288.4K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
#
# Example:
#
#
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
#
#
#
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # =====================================================================
        # Idea based on concept of rolling hash @
        # https://leetcode.com/problems/repeated-dna-sequences/discuss/53902/Short-Java-%22rolling-hash%22-solution
        # =====================================================================

        table = {'A':1, 'C':2, 'G':3, 'T':4}
        hashes = set()
        rhash = 0
        ans = set()
        for i in range(min(10, len(s))):
            rhash = rhash*10 + table[s[i]]
        hashes.add(rhash)
        for i in range(10, len(s)):
            rhash -= (10**9)*table[s[i-10]]
            rhash = rhash*10 + table[s[i]]
            if rhash in hashes:
                ans.add(s[i-9:i+1])
            else:
                hashes.add(rhash)
        return list(ans)
