#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (22.78%)
# Total Accepted:    45K
# Total Submissions: 197.7K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i
# to val.
#
# Example:
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#
#
#
# Note:
#
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
#
#
#


class NumArray:

    # Trivial solutions is accepted i.e O(1) update/O(n) aggregation
    # https://leetcode.com/submissions/detail/154001816/
    # Better solution O(log(n)) for both update/aggregation based on Binary INdexed Tree
    # https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation
    def _set_bit(self, i, val):
        i+=1
        while(i<=self.n):
            self.BIT[i] += val
            i += i&-i

    def _get_cum_sum(self, i):
        sum=0
        while i>0:
            sum += self.BIT[i]
            i -= i&-i
        # print(i,sum)
        return sum

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = nums
        self.BIT = [0]*(self.n+1)
        for i,val in enumerate(nums):
            self._set_bit(i, val)
        # print(self.BIT)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val-self.nums[i]
        self.nums[i] = val
        self._set_bit(i, diff)



    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._get_cum_sum(j+1) - self._get_cum_sum(i)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
