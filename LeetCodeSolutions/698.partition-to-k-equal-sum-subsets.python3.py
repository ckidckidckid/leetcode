#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (38.17%)
# Total Accepted:    17.6K
# Total Submissions: 46K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
#
# Example 1:
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4 ==> [1,2,2,3,3,4,5]
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
#
#
#
# Note:
# 1 .
# 0 < nums[i] < 10000.
#
#
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(A,target,num,k):
            if k==1:         # if previous k-1 subset has the average value, then the sum of the rest must be the average
                return True
            n=len(A)
            for i in range(n):
                B=A[:i]+A[i+1:]
                if num+A[i]==target:
                    if dfs(B,target,0,k-1):  # if sum of previous number and current number is the average, the step plus 1,
                        return True
                elif num+A[i]<target:
                    if dfs(B,target,num+A[i],k):
                        return True
                elif num==0: return False  #if any single num is great than the average, return false immediately
            return False

        n,total=len(nums),sum(nums)
        if total%k!=0: return False
        target=total//k
        nums.sort(reverse=True)     # reverse  sort to check bigest number first
        res=dfs(nums,target,0,k)
        return res

        # Correct but TLE ; ;
        # ts = sum(nums)
        # if k <= 0 or ts % k != 0:
        #     return False
        # n = len(nums)
        # visited = [False]*n
        # target = ts//k
        # def dfs(start_pos, acc, k):
        #     if k==1:
        #         return True
        #     if acc==target:
        #         return dfs(0, 0, k-1)
        #     for i in range(start_pos, len(nums)):
        #         if not visited[i]:
        #             visited[i] = True
        #             if dfs(start_pos+1, acc+nums[i], k):
        #                 return True
        #             visited[i] = False
        #     return False
        # return dfs(0, 0, k)
