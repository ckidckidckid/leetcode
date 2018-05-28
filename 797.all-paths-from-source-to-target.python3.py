#
# [813] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (68.05%)
# Total Accepted:    7.2K
# Total Submissions: 10.6K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
#
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
#
#
# Example:
# Input: [[1,2], [3], [3], []]
# Output: [[0,1,3],[0,2,3]]
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#
#
# Note:
#
#
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
#
#
#
class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(node, visited, path):
            if node == len(graph)-1:
                ans.append(path[:])
            else:
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        path.append(child)
                        dfs(child, visited, path)
                        path.pop()
                        visited.remove(child)

        ans = []
        dfs(0, {0}, [0])
        return ans
