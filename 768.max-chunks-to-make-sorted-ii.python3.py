#
# [779] Max Chunks To Make Sorted II
#
# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/
#
# algorithms
# Hard (43.09%)
# Total Accepted:    4.5K
# Total Submissions: 10.4K
# Testcase Example:  '[5,4,3,2,1]'
#
# This question is the same as "Max Chunks to Make Sorted" except the integers
# of the given array are not necessarily distinct, the input array could be up
# to length 2000, and the elements could be up to 10**8.
#
#
#
# Given an array arr of integers (not necessarily distinct), we split the array
# into some number of "chunks" (partitions), and individually sort each chunk.
# After concatenating them, the result equals the sorted array.
#
# What is the most number of chunks we could have made?
#
# Example 1:
#
#
# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3],
# which isn't sorted.
#
#
# Example 2:
#
#
# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks
# possible.
#
#
# Note:
#
#
# arr will have length in range [1, 2000].
# arr[i] will be an integer in range [0, 10**8].
#
#
#
#
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Extremely elegant O(n) time ; O(n) space solution ;
        # Explanation at https://leetcode.com/problems/max-chunks-to-make-sorted-ii/discuss/113462/Java-solution-left-max-and-right-min.
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
        n = len(arr)
        right_min = [float('inf')]*n
        left_max = [0]*n
        ans = 0

        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], arr[i+1])
        for i in range(n):
            left_max[i] = max(arr[i], left_max[i-1] if i>0 else -float('inf'))
        for i in range(n):
            ans += 1 if left_max[i] <= right_min[i] else 0
        return ans
