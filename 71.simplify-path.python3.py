#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (26.42%)
# Total Accepted:    113.6K
# Total Submissions: 430K
# Testcase Example:  '"/home/"'
#
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
# Corner Cases:
#
#
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together,
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
#
#
#
import re
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # path = path.replace('//', '/').replace('/./', '/')
        # path = re.sub(r'/+$', '', path)
        # path = re.sub(r'.?/', '', path)
        # print(path)
        splits = path.split('/')
        i = len(splits)-1
        ans = []
        skip=0
        # print(splits)
        while i>=0:
            if not splits[i] or splits[i] == '.':
                pass
            elif splits[i] == '..':
                skip+=1
            else:
                if skip==0:
                    ans.append(splits[i])
                else:
                    skip-=1
            i-=1
        comp_path = '/' + '/'.join(ans[::-1])
        return comp_path
