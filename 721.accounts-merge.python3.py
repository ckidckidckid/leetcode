#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (33.14%)
# Total Accepted:    10.1K
# Total Submissions: 30.6K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list accounts, each element accounts[i] is a list of strings, where
# the first element accounts[i][0] is a name, and the rest of the elements are
# emails representing emails of the account.
#
# Now, we would like to merge these accounts.  Two accounts definitely belong
# to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name, they may belong to
# different people as people could have the same name.  A person can have any
# number of accounts initially, but all of their accounts definitely have the
# same name.
#
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order.  The accounts themselves can be returned in any
# order.
#
# Example 1:
#
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
# 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
# "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email
# "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
#
#
#
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
#
#
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = {}
        email_name_lookup = {}

        # Build the graph
        for i,account in enumerate(accounts):
            name,email_1,*emails = account

            if email_1 not in graph:
                graph[email_1] = set()
            if email_1 not in email_name_lookup:
                email_name_lookup[email_1] = name

            prev = email_1
            for email in emails:
                if email not in email_name_lookup:
                    email_name_lookup[email] = name
                if email not in graph:
                    graph[email] = set()
                graph[email].add(prev)
                graph[prev].add(email)
                prev = email

        def dfs(email):
            res = [email]
            for child in graph[email]:
                if child not in email_name_lookup:
                    continue
                del email_name_lookup[child]
                res.extend(dfs(child))
            return res

        # Do DFS traversal
        ans = []
        for email in graph:
            if email not in email_name_lookup:
                continue
            name = email_name_lookup[email]
            del email_name_lookup[email]
            email_list = dfs(email)
            ans.append([name] + sorted(email_list))
        return ans

# Problem can be solved with both UnionFind  and DFS/BFS traversal. I solved ^ using
# DFS traversal after constructing the graph as it is simpler.

# Good discussions on DFS traversal
# https://leetcode.com/problems/accounts-merge/discuss/109162/Summary-for-DFS-Templates
# https://leetcode.com/problems/accounts-merge/discuss/109158/Java-Solution-(Build-graph-+-DFS-search)
