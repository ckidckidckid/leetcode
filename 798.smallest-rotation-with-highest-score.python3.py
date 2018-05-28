#
# [814] Smallest Rotation with Highest Score
#
# https://leetcode.com/problems/smallest-rotation-with-highest-score/description/
#
# algorithms
# Hard (32.74%)
# Total Accepted:    1.9K
# Total Submissions: 5.7K
# Testcase Example:  '[2,3,1,4,0]'
#
#  Given an array A, we may rotate it by a non-negative integer K so that the
# array becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ...,
# A[K-1].  Afterward, any entries that are less than or equal to their index
# are worth 1 point. 
#
# For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes
# [1, 3, 0, 2, 4].  This is worth 3 points because 1 > 0 [no points], 3 > 1 [no
# points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].
#
# Over all possible rotations, return the rotation index K that corresponds to
# the highest score we could receive.  If there are multiple answers, return
# the smallest such index K.
#
#
# Example 1:
# Input: [2, 3, 1, 4, 0]
# Output: 3
# Explanation:
# Scores for each K are listed below:
# K = 0,  A = [2,3,1,4,0],    score 2
# K = 1,  A = [3,1,4,0,2],    score 3
# K = 2,  A = [1,4,0,2,3],    score 3
# K = 3,  A = [4,0,2,3,1],    score 4
# K = 4,  A = [0,2,3,1,4],    score 3
#
#
# So we should choose K = 3, which has the highest score.
#
#
#
#
# Example 2:
# Input: [1, 3, 0, 2, 4]
# Output: 0
# Explanation:  A will always have 3 points no matter how it shifts.
# So we will choose the smallest K, which is 0.
#
#
# Note:
#
#
# A will have length at most 20000.
# A[i] will be in the range [0, A.length].
#
#
#
class Solution:
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 1:
            return 0
        cnt = [0]*n
        for i, num in enumerate(A):
            if num <= i:
                st = 0
                en = i-num
                cnt[st] += 1
                if en+1 < n:
                    cnt[en+1] -= 1
                if i+1 < n:
                    cnt[i+1] += 1
            else:
                if num >= n:
                    continue
                st = i+1
                en = i - num + n
                if st < n:
                    cnt[st] += 1
                if en+1 < n:
                    cnt[en+1] -= 1
        m_idx, m_val = 0, cnt[0]
        for i in range(1,n):
            cnt[i] += cnt[i-1]
            if cnt[i] > m_val:
                m_val = cnt[i]
                m_idx = i
        return m_idx

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # O(n^2) solution; Times out                                          #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # def cal_score(idx, arr):
        #     ans = 0
        #     for i,a in zip(idx, arr):
        #         if a<=i:
        #             ans+=1
        #     return ans
        #
        # n = len(A)
        # idx = [x for x in range(n)]
        # ans = 0
        # best_score = -float('inf')
        # for i in range(n):
        #     score = cal_score(idx, A)
        #     if score > best_score:
        #         best_score = score
        #         ans = i
        #     for j in range(n):
        #         idx[j] = (idx[j]-1)%n
        # return ans
