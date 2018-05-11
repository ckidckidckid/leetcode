#
# [717] 1-bit and 2-bit Characters
#
# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
#
# algorithms
# Easy (49.49%)
# Total Accepted:    19.4K
# Total Submissions: 39.2K
# Testcase Example:  '[1,0,0]'
#
# We have two special characters. The first character can be represented by one
# bit 0. The second character can be represented by two bits (10 or 11).
#
# Now given a string represented by several bits. Return whether the last
# character must be a one-bit character or not. The given string will always
# end with a zero.
#
# Example 1:
#
# Input:
# bits = [1, 0, 0]
# Output: True
# Explanation:
# The only way to decode it is two-bit character and one-bit character. So the
# last character is one-bit character.
#
#
#
# Example 2:
#
# Input:
# bits = [1, 1, 1, 0]
# Output: False
# Explanation:
# The only way to decode it is two-bit character and two-bit character. So the
# last character is NOT one-bit character.
#
#
#
# Note:
# 1 .
# bits[i] is always 0 or 1.
#
#
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # Optimal : looks only at the tail of the array
        n = len(bits)
        if bits[-1] == 1:
            return False
        count = 0
        for i in range(n-2, -1, -1):
            if bits[i] != 1:
                break
            count+=1
        return count%2 == 0

        # =======================================================
        # original 36ms; 94% solution; but scans the entire array
        # =======================================================
        # n = len(bits)
        # i=0
        # while i < n:
        #     if i==n-1:
        #         return True
        #     if bits[i] == 1:
        #         i+=2
        #     else:
        #         i+=1
        # return False
