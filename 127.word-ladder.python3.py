#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (20.19%)
# Total Accepted:    165.7K
# Total Submissions: 820.4K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#
from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        # =====================================================================================
        # Another single ended BFS ;  https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95
        # =====================================================================================

        def create_graph(wordlist):
            graph = {}
            for word in wordList:
                for i in range(len(word)):
                    tr = word[:i] + '_' + word[i+1:]
                    if tr not in graph:
                        graph[tr] = set()
                    graph[tr].add(word)
            return graph

        def bfs(graph, beginWord, endWord):
            q = deque()
            visited = {beginWord}
            q.append((beginWord, 1))
            while q:
                w, l = q.popleft()
                if w == endWord:
                    return l
                for i in range(len(w)):
                    tr = w[:i] + '_' + w[i+1:]
                    if tr not in graph:
                        continue
                    for child in graph[tr]:
                        if child not in visited:
                            visited.add(child)
                            q.append((child, l+1))
            return 0

        wordList = set(wordList)
        graph = create_graph(wordList | {beginWord, endWord})
        return bfs(graph, beginWord, endWord)

        # =====================================================================================
        # BFS approach; correct but times out. O(n^2) where n = number of words in wordslist
        # =====================================================================================
        # cache = {}
        # def diff(str1, str2):
        #     key = (str1, str2)
        #     if key in cache:
        #         return cache[key]
        #     c = 0
        #     if str1 != str2:
        #         for ch in 'abcdefghijklmnopqrstuvwxyz':
        #             for idx in range(len(str1)):
        #                 new_word = str1[:idx] + ch + str1[idx+1:]
        #                 if new_word == str2:
        #                     c = 1
        #                     cache[key] = c
        #                     return c
        #     cache[key] = 2
        #     return c
        #
        # if endWord not in wordList:
        #     return 0
        # graph = {}
        # n = len(wordList)
        # graph[beginWord] = set()
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if diff(wordList[i], wordList[j]) == 1:
        #             if wordList[i] not in graph:
        #                 graph[wordList[i]] = set()
        #             if wordList[j] not in graph:
        #                 graph[wordList[j]] = set()
        #             graph[wordList[i]].add(wordList[j])
        #             graph[wordList[j]].add(wordList[i])
        #     if diff(beginWord, wordList[i]) == 1:
        #             graph[beginWord].add(wordList[i])
        #             if wordList[i] not in graph:
        #                 graph[wordList[i]] = set()
        #             graph[wordList[i]].add(beginWord)
        # q = deque()
        # q.append((beginWord, 1))
        # visited = set()
        # while q:
        #     word, dist = q.popleft()
        #     if word == endWord:
        #         return dist
        #     visited.add(word)
        #     for child in graph[word]:
        #         if child not in visited:
        #             q.append((child, dist+1))
        # return 0
