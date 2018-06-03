#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (41.38%)
# Total Accepted:    20.8K
# Total Submissions: 50.2K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two
# words have the same frequency, then the word with the lower alphabetical
# order comes first.
#
# Example 1:
#
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
#
#
#
# Example 2:
#
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
# "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
#
#
#
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
#
#
#
# Follow up:
#
# Try to solve it in O(n log k) time and O(n) extra space.
#
#
#
from collections import Counter
from functools import total_ordering
import heapq

@total_ordering
class HeapElement:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        ctr = Counter(words)
        table = [(count,word) for word,count in ctr.items()]
        h = [HeapElement('', -float('inf')) for _ in range(k)]
        for item in table:
            heapq.heappushpop(h,HeapElement(item[1], item[0]))
        h.sort(reverse = True)
        return [x.word for x in h]
